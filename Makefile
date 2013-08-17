#!/usr/bin/make

PROJECT=project
TESTS = 
COVERAGE_INCLUDES = --include=project/*


.PHONY: all
all: c4che env bootstrap.py
	env/bin/python waf

.PHONY: run
run: all
	bin/django runserver_plus

c4che:
	./waf configure --project-name=$(PROJECT)

.virtualenv:
	mkdir -p .virtualenv
	wget -c \
		https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.10.tar.gz \
		-O .virtualenv/archive.tar.gz
	tar -xvf .virtualenv/archive.tar.gz
	mv virtualenv-* .virtualenv/source

env: .virtualenv
	./waf virtualenv

# Helpers

.PHONY: clean
clean:
	./waf distclean

.PHONY: clean
messages:
	./waf makemessages

.PHONY: tags
tags: all
	bin/ctags -v

.PHONY: todo
todo:
	@egrep -nirI 'FIXME|TODO|XXX' $(PROJECT) config wscript

test: all
	bin/django test $(TESTS)

coverage: all
	bin/coverage run $(COVERAGE_INCLUDES) bin/django test $(TESTS)
	bin/coverage html -d var/htmlcov/ $(COVERAGE_INCLUDES)
	bin/coverage report $(COVERAGE_INCLUDES)
	@echo "Also try xdg-open var/htmlcov/index.html"

graph: all
	bin/django graph_models \
	    --group-models \
	    --all-applications \
	    -o var/graph.png
	xdg-open var/graph.png

bootstrap.py:
	wget http://downloads.buildout.org/2/bootstrap.py
