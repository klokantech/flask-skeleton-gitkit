#!/bin/sh
set -e

if [ "$1" = "development" ]; then
    (cd /venv/app; /venv/bin/python setup.py develop)
elif [ "$1" = "release" ]; then
    (cd /venv/app; /venv/bin/python setup.py install)
else
    echo "Invalid setup mode: $1"
    exit 1
fi
