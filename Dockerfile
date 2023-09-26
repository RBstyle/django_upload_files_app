FROM python:3.10.12-bullseye

WORKDIR /upload_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./docker/backend/worker-entrypoint.sh /worker-entrypoint.sh
COPY ./docker/backend/server-entrypoint.sh /server-entrypoint.sh

RUN chmod +x /worker-entrypoint.sh
RUN chmod +x /server-entrypoint.sh

COPY . .