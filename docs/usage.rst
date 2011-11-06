#####
Usage
#####

How to create new project
=========================

If you want to start new project based on ``django-starter``, fallow these
steps:

1. Get copy of ``django-starter`` and rename ``django-starter`` folder name to
   name of your new project (here I will use ``my-new-project`` name)::

       hg clone https://bitbucket.org/sirex/django-starter my-new-project

   All commands in following steps must be executed from ``my-new-project``
   folder, so change you current working directory to ``my-new-project``::

       cd my-new-project

2. Then you need to make some cleaning::

       ./clean.sh

   ``clean.sh`` helper script cleans all ``django-starter`` related files like
   ``README.rst``, ``LICENCE.txt``, ``docs`` and etc. Your project probably
   will used different licence, docs and etc. ``clean.sh`` script also removes
   it self.

That's all! Continue reading `Running your project`_.

Running your project
====================

To be able to run your project, first you need to make sure, that all required
packages are installed on your system. You can easily do this using helper
tools: ``make setup-<your system name>``. Example::

    make setup-ubuntu

This command automatically installs all needed packages, thus required you to
enter root password. This is single place, where you need root password, all
other commands must be executed with you home use permissions.

When all requirements are installed you can run your project with single
command::

    make run

This command checks your environment, downloads all needed dependencies and
finally starts development server.
