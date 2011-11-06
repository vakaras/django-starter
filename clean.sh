#!/bin/sh

# Helper script, to clean all ``django-starter`` related files, that are not
# needed for new projects based on ``django-starter`` template.

rm -r \
    .hg \
    .hgignore \
    AUTHORS.rst \
    LICENCE.txt \
    README.rst \
    clean.sh \
    docs
