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
	./waf virtualenv


# Helpers

.PHONY: clean
clean:
	./waf distclean

.PHONY: tags
tags:
	bin/ctags -v
