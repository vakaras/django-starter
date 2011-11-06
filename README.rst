django-starter
==============

``django-starter`` is a django project template, that includes all best
practices for configuring, developing, deploying and maintaining you project.

Features:

* Powerful build tools: waf, zc.buildout, make.

* Powerful development tools: django-debug-toolbar, django-extensions,
  django-test-utils, ipdb, ipython, ctags, SASS with Compass support.

* Mainstream web development libraries: jQuery, Modernizr, Markdown, South,
  django-mediagenerator, solr-thumbnails.

* Best known configurations for Apache, HTML and CSS using HTML5 Boilerplate.

* Excellent documentation with documented best practices how to do things...

All these features combined in to one consistent and working project
environment, that is easily customizable.

Quick start
===========

Creating new django projects based on django-starter is easy::

   hg clone https://bitbucket.org/sirex/django-starter my-new-project
   cd my-new-project
   ./clean.sh
   make setup-ubuntu
   make run

... thats all, now you can start to work on your new project without thinking
about various project infrastructure related things.
