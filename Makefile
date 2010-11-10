.PHONY: all run tags test syncdb app clean

all: bootstrap.py \
     bin/buildout \
     bin/django \
     project/production.py \
     development.db \
     docs/build/html

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
	    -o graph.png
	xdg-open graph.png

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

development.db:
	bin/django syncdb --all --noinput
	bin/django migrate --fake
	bin/django loaddata initial_data.json

docs/build/html: $(find docs -type f -not -wholename 'docs/build/*')
	cd docs ; make html

app:
	@if [ "" = "$(name)" ] ; then \
	    echo "Usage: make $@ name=myappname" ; \
	elif [ -e apps/$(name) ] ; then \
	    echo "App '$(name)' already exists." ; \
	else \
	    cp --preserve=mode -r apps/.skeleton apps/$(name) ; \
	    bin/django startapp $(name) ; \
	    mv project/$(name) apps/$(name)/ ; \
	    sed -i \
		-e 's/$$(name)/$(name)/g' \
		-e 's/$$(author)/'$$USER'/g' \
		-e 's/$$(date)/'$$(date +%Y-%m-%d)'/g' \
		    apps/$(name)/CHANGES.txt \
		    apps/$(name)/docs/conf.py \
		    apps/$(name)/docs/index.rst \
		    apps/$(name)/setup.py ; \
	fi
