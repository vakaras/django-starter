.PHONY: all run tags test syncdb app clean

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

test:
	bin/django test

syncdb:
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

app:
	@if [ "" = "$(name)" ] ; then \
	    echo "Usage: make $@ name=myappname" ; \
	    echo "or" ; \
	    echo "Usage: make $@ name=mynamespace.myappname" ; \
	elif [ -e apps/$(name) ] ; then \
	    echo "App '$(name)' already exists." ; \
	else \
	    cp --preserve=mode -r apps/.skeleton apps/$(name) ; \
	    lastname=$$(echo $(name) | egrep -o '[^.]+$$') ; \
	    if [ "$$lastname" = "$(name)" ] ; then \
		namespace= ; \
		path=$(name) ; \
	    else \
		namespace=$$(echo $(name) | sed 's/\./\//g') ; \
		namespace=$$(dirname $$namespace) ; \
		path=$(name)/$$namespace ; \
		mkdir apps/$$path ; \
		echo "__import__('pkg_resources').declare_namespace(__name__)" \
		    > apps/$$path/__init__.py ; \
	    fi ; \
	    bin/django startapp $$lastname ; \
	    mv project/$$lastname apps/$$path/$$lastname ; \
	    sed -i \
	        -e 's/$$(name)/$(name)/g' \
	        -e 's/$$(author)/'$$USER'/g' \
	        -e 's/$$(date)/'$$(date +%Y-%m-%d)'/g' \
	        -e 's/$$(namespace)/"'$$namespace'"/g' \
	            apps/$(name)/CHANGES.txt \
	            apps/$(name)/docs/conf.py \
	            apps/$(name)/docs/index.rst \
	            apps/$(name)/setup.py ; \
	fi
