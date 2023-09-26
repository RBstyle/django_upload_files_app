#!/bin/sh

until cd upload_app
do
    echo "Waiting for server volume..."
done

celery -A upload_app worker --loglevel=info