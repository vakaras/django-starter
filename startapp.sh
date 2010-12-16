#! /bin/sh

if [ $# != 2  ]; then
    echo "Usage: registerapp.sh application-name index-server"
elif [ !-f apps/$1/setup.py ]; then
    echo "Application '$1' does not exist."
else
    cd apps/$1
    python setup.py register -r $2 sdist upload -r $2
    cd ../..
fi
