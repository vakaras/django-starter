``django-starter`` is prepared buildout environment for django project with
reusable and installable django applications in mind.

Using in development
=======================================

To prepare development environment of your project use this command::

    make

Using in production
======================================

To prepare production environment of your project use this command::

    make deploy

Features
========

``django-starter`` provides to different environment, one for development,
other for production use.

Environment independent features:

* Well prepared buildout configuration files.

* Well prepared Makefile, that lets you do most things just by running ``make``
  command.

* ``South`` for database migrations.

* ``mr.developer`` lets you add packages to buildout environment directly from
  source repositories. All major VCS's are supported.

Features in development environment:

* ``ctags`` - you can build tags file from all eggs added to buildout
  environment.

* ``shpinx`` - ``django-starter`` has prepared ``docs`` folders for writing
  documentations using ``sphinx``, ``sphinx`` is also included, so you can
  build documentations just running ``make html`` command in ``docs`` folder.

* ``ipython`` and ``ipdb`` are also included and you will get ``ipython`` shell
  using ``bin/django shell`` command. Use ``import ipdb ; ipdb.set_trace()``
  for excellent ``ipdb`` debugger.

* ``django-toolbar`` for inspecting page requests.

* ``django-extensions`` and ``django-test-utils`` are also included, these
  packages provides lots of useful django management commands.

Features in production environment:

* wsgi script out of the box

* prepared apache configuration file, that can be simply included from apache
  main configuration with ``Include /path/to/your/project/etc/apache.conf``.

* MySQL configuration hits.

Project layout
==============

``project/``
    Folder for django project. Here goes only settings and project related
    templates, urls routing.

``apps/``
    Reusable django apps, even if your app directly related to your project and
    can be reused should be added here.

``docs/``
    Fully prepared ``Sphinx`` documentation template.

``Makefile``
    Provides simple and useful command.

``buildout.cfg``
    Main buildout configuration file. Here comes all environment independent
    settings.

``development.cfg``
    Buildout configuration file for development environment.

``initial_data.json``
    Initial data.

``startapp.sh``
    Creates new django app template.

Commands from ``Makefile``:

``make``
    Prepares development environment and does everything that is needed.

``make run``
    Runs django development web sever.

``make tags``
    Builds ``tags`` file from all eggs included in buildout environment.

``make test``
    Runs all unit tests.

``make coverage``
    Generates unit tests code coverage reports.

``make syncdb``
    Removes development database and creates it from scratch.

``make graph``
    Generates graphical representation of your models.

``make clean``
    Cleans some generated files.
