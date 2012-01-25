``django-starter`` is a django project template, that includes all best
practices for configuring, developing, deploying and maintaining you
project.

Features:

* Powerful build tools: waf, zc.buildout, make.

* Powerful development tools: South, django-debug-toolbar, django-
  extensions, django-test-utils, ipdb, ipython, ctags.

* Mainstream web development libraries: jQuery, Modernizr, SASS with Compass
  support, django-mediagenerator, solr-thumbnails.

* Best known configuration for Apache, HTML and CSS using HTML5 Boilerplate.

* Excellent documentation with documented best practices how to do things...

All these features combined in to one consistent and working project
environment, that is easily customizable.

Home page:
    https://bitbucket.org/sirex/django-starter

Documentation:
    http://django-starter.readthedocs.org/

Quick start
===========

Creating new django projects based on django-starter is easy::

    sudo apt-get install git
    git clone git://github.com/vakaras/django-starter.git my-new-project
    cd my-new-project
    git remote rename origin template
    git remote add origin my-new-project-git-repository
    git push -u origin master
    sudo ./waf setup
    make run

... thats all, now you can start to work on your new project without
thinking about various project infrastructure related things.
