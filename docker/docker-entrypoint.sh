#!/bin/sh

cd upload_app

celery -A upload_app worker