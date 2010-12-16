.PHONY: all run tags test todo syncdb app clean

all: bootstrap.py \
     bin/buildout \
     bin/django \
     project/production.py \
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
	bin/django test

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

bootstrap.py:
	mkdir -p eggs downloads
	wget http://www.python-distribute.org/bootstrap.py

bin/buildout:
	python bootstrap.py

bin/django: bin/buildout buildout.cfg
	bin/buildout -N
	touch $@

project/production.py:
	cp project/development.py project/production.py

var/development.db:
	bin/django syncdb --all --noinput
	bin/django migrate --fake
	bin/django loaddata initial_data.json

var/htdocs/static:
	bin/django build_static --noinput

docs/build/html: $(find docs -type f -not -wholename 'docs/build/*')
	cd docs ; make html
