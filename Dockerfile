FROM python:3.7

RUN apt-get update \
    && pip install psycopg2-binary