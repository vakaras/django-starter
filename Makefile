# Default target

.PHONY: all

all: develop


###############
# Development #
###############

.PHONY: develop run tags todo test flake8 syncdb clean

develop: bootstrap.py \
         bin/buildout \
         bin/django \
         var/development.db \
         docs/build/html \
         var/htdocs/static

run:
	bin/django runserver

tags:
	bin/ctags -v

todo:
	@egrep -n 'FIXME|TODO' $$(find apps -iname '*.py' ; \
	                          find project -iname '*.py')

test:
	bin/django test avatars avatarplugin_email wora profiles

flake8:
	@bin/flake8 \
	    apps/avatarplugin-email/avatarplugin_email/ \
	    apps/avatars/avatars/ \
	    apps/wora/wora/ \
	    project/

syncdb:
	test ! -f var/development.db || rm var/development.db
	bin/django syncdb --all --noinput
	bin/django migrate --fake
	bin/django loaddata initial_data.json

# circo dot fdp neato nop nop1 nop2 twopi
graph:
	bin/django graph_models \
	    --group-models \
	    --all-applications \
	    -o var/graph.png
	xdg-open var/graph.png

clean:
	hg purge --all

bin/django: bin/buildout buildout.cfg, development.cfg apps/*/setup.py
	bin/buildout -c development.cfg -N
	touch $@

var/development.db:
	bin/django syncdb --all --noinput
	bin/django migrate --fake
	bin/django loaddata initial_data.json

docs/build/html: $(find docs -type f -not -wholename 'docs/build/*')
	cd docs ; make html


##############
# Deployment #
##############

.PHONY: deploy

deploy: bootstrap.py \
	bin/buildout \
	bin/django.wsgi \
	project/production.py \
	var/production.db \
	var/htdocs/static

bin/django.wsgi: bin/buildout buildout.cfg apps/*/setup.py
	bin/buildout -N
	touch $@

project/production.py:
	@echo
	@echo "project/production.py settings file is missing."
	@echo "Create this file and run make deploy again."
	@echo
	@echo "Here is example, how to prepare MySQL database:"
	@echo
	@echo "    CREATE USER '<user>'@'localhost' IDENTIFIED BY '<password>';"
	@echo "    GRANT ALL ON *.* TO '<user>'@'localhost';"
	@echo "    CREATE DATABASE <dbname> CHARACTER SET utf8;"
	@echo
	@echo "Use generated sample file: etc/my.cnf and specify "
	@echo "database connection credentials. You can use this file,"
	@echo "to connect to database:"
	@echo
	@echo "    mysql --defaults-extra-file=etc/my.cnf"
	@echo
	@echo "Use generated sample file: etc/production.py and "
	@echo "adjust your production server settings:"
	@echo
	@echo "    cp etc/production.py project/production.py"
	@echo "    vi project/production.py"
	@echo
	@exit 1

var/production.db:
	bin/django syncdb --all --noinput
	bin/django migrate --fake
	bin/django loaddata initial_data.json
	touch $@


###########
# General #
###########

bootstrap.py:
	mkdir -p eggs downloads
	wget http://www.python-distribute.org/bootstrap.py

bin/buildout:
	python bootstrap.py

var/htdocs/static:
	bin/django build_static --noinput

