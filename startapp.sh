#!/bin/sh

if [ $# != 1 ] ; then
    echo "Usage: startapp.sh application-name"
elif [ -e apps/$1 ] ; then
    echo "App '$1' already exists."
else
    modulename=$(echo $1 | sed 's/-/_/g')
    bin/django startapp $modulename && \
    #cp --preserve=mode -r apps/.skeleton apps/$1 && \ <-- please don't be GNU fan respect unix family too
    cp -R -p apps/.skeleton apps/$1 && \
    mv project/$modulename apps/$1/$modulename
   

    sed -i -e 's/$(date)/'$(date +%Y-%m-%d)'/g' apps/$1/CHANGES.txt
    sed -i -e 's/$(author)/'$USER'/g'           apps/$1/docs/conf.py apps/$1/setup.py
    sed -i -e 's/$(name)/'$1'/g'                apps/$1/docs/conf.py apps/$1/setup.py
    sed -i -e 's/$(date)/'$(date +%Y-%m-%d)'/g' apps/$1/docs/index.rst

fi

