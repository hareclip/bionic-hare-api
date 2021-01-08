# Bionic Hare

A port of the Hare's API to Django

## Setup

Create virtual environment and install dependences:

    python -m venv ./venv
    ./venv/Scripts/activate
    pip install requirements.txt

### Development

Set up database:

    python manage.py migrate --settings thehare.development_settings
    python manage.py loaddata categories.yaml --settings thehare.development_settings

Run development server with:

    python manage.py runserver --settings thehare.development_settings

### Production

Create S3 bucket and AWS service user, keeping track of the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

Create `.env` from `sample.env` and insert credentials.

Set up database:

    python manage.py migrate --settings thehare.production_settings
    python manage.py loaddata categories.yaml --settings thehare.production_settings

#### Run production on UNIX

    gunicorn thehare.wsgi

#### Run production on Windows

    waitress-serve thehare.wsgi:application

## Deploy with Docker

    docker-compose up --build

## Deploy on Heroku

Create new Heroku app and attach Heroku Postgres resource.

Insert `.env` credentials into Heroku config vars.

Deploy with:

    heroku push origin master

Set up database:

    heroku run bash
    python manage.py migrate --settings thehare.production_settings
    python manage.py loaddata categories.yaml --settings thehare.production_settings

## Project Layout
  - `core`: Core models
  - `v1`: Hare-compatible API