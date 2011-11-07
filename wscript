#!/usr/bin/env python
# encoding: utf-8

import codecs
import functools
import os
import re
import shutil
import socket
import subprocess
import sys

from waflib import Context, Logs

top = '.'
out = '.'

def options(ctx):
    ctx.load('compiler_c python ruby')

    gr = ctx.get_option_group('configure options')
    gr.add_option('--project-name', action='store', default='project',
                  help='project name')

    gr.add_option('--production', action='store_true', default=False,
                  help='build production environment')

    gr.add_option('--server-name', action='store',
                  default='127.0.0.1:8000',
                  help='server domain name, example: www.example.com')

    gr.add_option('--server-admin', action='store', default='%s@%s' % (
                        os.getlogin(), socket.gethostname()),
                  help='server admin email address')

    gr.add_option('--use-sqlite', action='store_true',
                  help='force Sqlite database in production')

    gr.add_option('--wsgi-user', action='store',
                  help='the user that the daemon processes should be run as')

    gr.add_option('--wsgi-group', action='store',
                  help='the primary group that the daemon processes should be run as')

    gr.add_option('--languages', action='store', default='en',
                  help='comma separated list of two letter languages codes')

    gr.add_option('--use-jquery', action='store', default='1.7',
                  help='jQuery version, or empty if you don\'t want to use it')


def configure(ctx):
    ctx.find_program('buildout', mandatory=False)
    ctx.find_program('hg')
    ctx.find_program('git')
    ctx.find_program('virtualenv')

    ctx.load('compiler_c python ruby')

    ctx.check_python_version((2,6))
    ctx.check_python_module('PIL')
    ctx.check_python_headers()

    ctx.check_ruby_version((1,8,0))
    ctx.check_ruby_ext_devel()

    ctx.env.TOP = ctx.path.abspath()
    ctx.env.PROJECT_NAME = ctx.options.project_name
    ctx.env.PRODUCTION = ctx.options.production
    ctx.env.USE_SQLITE = ctx.options.use_sqlite
    ctx.env.LANGUAGES = ctx.options.languages.split(',') or ['en']
    ctx.env.LANGUAGE_CODE = ctx.env.LANGUAGES[0]
    ctx.env.SERVER_ADMIN = ctx.options.server_admin
    ctx.env.SERVER_NAME = ctx.options.server_name
    ctx.env.JQUERY_VERSION = ctx.options.use_jquery

    ctx.env.WSGI_USER = ctx.options.wsgi_user
    ctx.env.WSGI_GROUP = ctx.options.wsgi_group

    if ctx.env.PRODUCTION:
        ctx.env.DEVELOPMENT = False
    else:
        ctx.env.DEVELOPMENT = True


def _subst(task):
    from Cheetah.Template import Template

    infilename = task.inputs[0].abspath()
    outfilename = task.outputs[0].abspath()

    c = {
        'NOTE': 'DO NOT MODIFY! This file is generated from %s '
                'template.' % infilename,
    }
    t = Template(file=infilename, searchList=[c, dict(task.generator.env)])

    outfile = codecs.open(outfilename, encoding='utf-8', mode='w')
    outfile.write(unicode(t))
    outfile.close()


def build(ctx):
    import babel

    ctx.env.LANG_NAMES = {}
    for lang in ctx.env.LANGUAGES:
        ctx.env.LANG_NAMES[lang] = babel.Locale(lang).english_name

    p = ctx.env.PROJECT_NAME
    glob = ctx.path.ant_glob
    bld = functools.partial(ctx, update_outputs=True)

    if ctx.env.PRODUCTION:
        bld(rule=_subst, source='config/apache.conf c4che/_cache.py',
            target='var/etc/apache.conf')

    bld(rule=_subst, source='config/buildout.cfg c4che/_cache.py',
        target='buildout.cfg')

    bld(rule=_subst, source='config/settings.py c4che/_cache.py',
        target='%s/settings.py' % p)

    bld(rule=_subst, source='config/urls.py c4che/_cache.py',
        target='%s/urls.py' % p)

    bld(rule=_subst, source='config/initial_data.json c4che/_cache.py',
        target='initial_data.json')

    bld(rule='${PYTHON} bootstrap.py --distribute', target='bin/buildout',
        source='buildout.cfg')

    bld(rule='bin/buildout -N', name='buildout', target='bin/django',
        source='bin/buildout buildout.cfg %s/settings.py' % p)

    bld(rule='bin/django syncdb --all --noinput && bin/django migrate --fake',
        source='bin/django %s/settings.py initial_data.json' % p,
        target='var/development.db')

    bld(rule='bin/django importsassframeworks',
        target='var/sass-frameworks/_compass.scss',
        after='buildout')

    bld(rule='bin/django generatemedia',
        source=(glob('%s/static/**/*' % p) +
                ['var/sass-frameworks/_compass.scss']),
        after='buildout')

    for lang in ctx.env.LANGUAGES:
        s = (p, lang)
        if os.path.exists('%s/locale/%s'):
            bld(rule='cd %s ; ../bin/django compilemessages -l %s' % s,
                source='%s/locale/%s/LC_MESSAGES/django.po' % s,
                target='%s/locale/%s/LC_MESSAGES/django.mo' % s,
                after='django')




def distclean(ctx):
    for pth in [
        # buildout generated files
        'bin', 'develop-eggs', '.installed.cfg', '.mr.developer.cfg',

        # waf generated files
        '.lock-wafbuild', 'config.log', 'c4che', Context.DBFILE,

        # project specific generated files
        '.sass-cache', 'buildout.cfg', '%s/settings.py' % ctx.env.PROJECT_NAME,
        'var',
    ]:
        if os.path.exists(pth):
            Logs.info('cleaning: %s' % pth)
            if os.path.isdir(pth):
                shutil.rmtree(pth, ignore_errors=True)
            else:
                os.unlink(pth)

    cleanpyc(ctx)


def cleanpyc(ctx):
    "Clean *.pyc files from sources."
    Logs.info('cleaning: *.pyc')
    for pth in ctx.path.ant_glob('%s/**/*.pyc' % ctx.env.PROJECT_NAME):
        os.unlink(pth.abspath())


def _get_platform():
    import platform

    python_version = sys.version[:3]
    kernel = os.uname()[0].lower()
    if kernel == 'linux':
        if python_version > '2.6':
            name, release = platform.linux_distribution()[:2]
        else:
            name, release = platform.linux_distribution()[:2]
        if name and release:
            return (name.lower(), release)
    return ('', '')


def _sh(cmd):
    print(cmd)
    return subprocess.call(cmd, shell=True)


class PackageSet(set):
    def replace(self, *args):
        if not isinstance(args[0], tuple):
            args = (args[0:2],)
        for old, new in args:
            self.remove(old)
            self.add(new)

    def replace_all(self, search, replace):
        repl = re.compile(search)
        for old in self:
            new = repl.sub(replace, old)
            if old != new:
                self.replace(old, new)


def setup(ctx):
    """Install all required dependencies."""

    if not os.geteuid()==0:
        sys.exit("Only root can run this script.")

    name, release = _get_platform()

    packages = PackageSet([
        # Build
        'build-essential',

        # Gettext
        'gettext',

        # VCS
        'bzr',
        'git',
        'mercurial',
        'subversion',

        # Python
        'python-dev',
        'python-virtualenv',

        # Ruby (used for gems)
        'ruby',
        'ruby-dev',

        # Other development headers
        'libfreetype6-dev',
        'libicu-dev',
        'libjpeg62-dev',
        'libxslt1-dev',
    ])


    if name == 'ubuntu' or name == 'debian':
        packages.replace('git', 'git-core')
        _sh('apt-get install %s' % ' '.join(packages))

    elif name == 'fedora':
        packages.remove('build-essential')
        packages.replace(
                ('libfreetype6-dev', 'freetype-devel'),
                ('libjpeg62-dev', 'libjpeg-turbo-devel'),
                ('libxslt1-dev', 'libxslt-devel')
            )
        packages.replace_all('-dev$', '-devel')
        _sh('yum groupinstall "Development Tools"')
        _sh('yum install %s' % ' '.join(packages))
    
    elif name == 'darwin':
        packages.remove('build-essential', 'python-dev')
        packages.replace(
                ('git', 'git-core')
                ('python-virtualenv', 'py-virtualenv')
                ('libfreetype6-dev', 'freetype')
                ('libicu-dev', 'icu')
                ('libjpeg62-dev', 'jpeg')
                ('libxslt1-dev', 'libxslt')
        )
        _sh('port -v install %s' % ' '.join(packages))
        
# --------
# Hack to pass ``BuildContext`` to commands other than ``build``.
from waflib.Build import BuildContext
def use_build_context_for(*cmds):
    for cmd in cmds:
        type('BldCtx_' + cmd, (BuildContext,), {'cmd': cmd, 'fun': cmd})
use_build_context_for('distclean', 'cleanpyc')
# --------
