#!/usr/bin/make

PROJECT=project


.PHONY: all
all: c4che env
	env/bin/python waf

.PHONY: run
run: all
	bin/django runserver

c4che:
	./waf configure --project-name=$(PROJECT)

env:
	virtualenv --no-site-packages env
	env/bin/pip install Cheetah Babel


# Helpers

.PHONY: clean
clean:
	./waf distclean

.PHONY: tags
tags:
	bin/ctags -v

.PHONY: sass
sass:
	bin/sass --watch $(PROJECT)/sass:var/sass/css

.PHONY: setup-ubuntu
setup-ubuntu:
	sudo apt-get install \
	    build-essential \
	    python-virtualenv \
	    python-dev \
	    libicu-dev \
	    libxslt1-dev \
	    libfreetype6-dev \
	    libjpeg62-dev \
	    ruby \
	    ruby-dev \
	    gettext \
	    mercurial \
	    git
