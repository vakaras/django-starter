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


Installing on Ubuntu Server
===========================

All installation instructions will use these names, that must be substituted
according to your needs:

``<server-name>``
    Your web site domain name, example: www.example.com

``<server-admin-email>``
    Web site administrator email, this email address will be used everywhere in
    system, when sending emails. Example: info@example.com

``<mysql-dbname>``
    MySQL database name.

``<mysql-user>``
    MySQL database user name.

``<mysql-password>``
    MySQL database user password.

All described commands must be executed from directory with ``Makefile`` and
``waf`` files inside.

You need to follow these installation steps:

1. Make sure, that locale packages are installed for all languages, that you
   planing to use::

       sudo apt-get install language-support-en

2. Install and configure MySQL, create new database::

       sudo apt-get install mysql-server
       mysql -u<mysql-user> -p \
             -e 'CREATE DATABASE <mysql-dbname> CHARACTER SET utf8;'

3. Install Apache with mod_wsgi::

       sudo apt-get install apache2 libapache2-mod-wsgi
   
   Make sure, that Apache locale settings are correct. ``LANG`` environment
   variable in ``/etc/apache2/envvars`` file must be set to ``en_US.UTF-8``,
   but not to ``C``.

   Information about how to configure Apache, will be provided in next steps.

3. Install and configure outgoing mail server.

4. Install all required build dependencies using this command::

       sudo ./waf setup --production

   This command will install needed packages using ``apt-get`` command. To see
   what command will be executed use ``--dry-run`` flag::

       ./waf setup --production --dry-run

5. Configure project with configuration options that are described in
   ``./waf --help`` command output.

   Here is example how project can be configured::

       ./waf configure \
           --production \
           --server-name=<server-name> \
           --server-admin=<server-admin-email> \
           --mysql-dbname=<mysql-dbname> \
           --mysql-username=<mysql-user> \
           --mysql-password=<mysql-password>

   All your configuration options will be stored in ``configure`` file, if you
   made a mistake, you can edit this file and configure project again using
   this command::

       ./configure

   If you manually run ``./waf configure`` command, existing ``./configure``
   file will not be overwritten.

6. Finally build project using this command::

       make

7. Make sure, that ``var`` folder is writable for Apache user::

       sudo chown -R www-data:www-data var

8. Configure Apache using these commands::

       echo "include $PWD/var/etc/apache.conf" | sudo tee \
           /etc/apache2/sites-available/<server-name>.conf
       sudo a2ensite <server-name>.conf

9. Restart Apache::

       sudo service apache2 restart

10. Create administrator user account::

       bin/django createsuperuser
