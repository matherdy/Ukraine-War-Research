#!/usr/bin/env bash

# Sourcing secrets if present
FILE=../.secrets/environment.env
if test -f "$FILE"; then
    echo "$FILE exist"
    source ${FILE}
    export $(cut -d= -f1 $FILE)
    cd ..
fi

# Run unit tests
nosetests -v -a '!slow'
