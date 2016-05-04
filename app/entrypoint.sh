#!/bin/sh
set -e

# Put your entrypoint code here.
# This example waits for PostgreSQL to start.
#
# until netcat -z -w 2 db 5432; do
#     echo 'Waiting for the database to start.'
#     sleep 2
# done

exec "$@"
