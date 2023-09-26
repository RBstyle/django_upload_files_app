#!/bin/sh

until cd /upload_app/upload_app/
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


python /upload_app/upload_app/manage.py runserver 0.0.0.0:8000