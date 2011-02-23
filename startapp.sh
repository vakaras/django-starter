#!/bin/sh

if [ $# != 1 ] ; then
    echo "Usage: startapp.sh application-name"
elif [ -e apps/$1 ] ; then
    echo "App '$1' already exists."
else
    modulename=$(echo $1 | sed 's/-/_/g')
    bin/django startapp $modulename && \
    cp -R -p apps/.skeleton apps/$1 && \
    mv project/$modulename apps/$1/$modulename && \
    sed -i \
        -e 's/$(name)/'$1'/g' \
        -e 's/$(author)/'$USER'/g' \
        -e 's/$(date)/'$(date +%Y-%m-%d)'/g' \
            apps/$1/CHANGES.txt \
            apps/$1/docs/conf.py \
            apps/$1/docs/index.rst \
            apps/$1/setup.py 

fi
