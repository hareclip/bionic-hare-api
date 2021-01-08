# Bionic Hare

A port of [the Hare's API](https://github.com/mli25782/umd-hare) to Django

## Setup

Create virtual environment and install dependences:

    python -m venv ./venv
    
    # UNIX
    source ./venv/bin/activate

    # Windows
    ./venv/Scripts/activate

    pip install -r requirements.txt

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

Run with:

    # UNIX
    gunicorn thehare.wsgi

    # Windows
    waitress-serve thehare.wsgi:application

## Deploy with Docker

    docker-compose up --build

## Deploy on Heroku

Create new Heroku app and attach Heroku Postgres resource.

Insert `.env` credentials into Heroku config vars.

Deploy with:

    heroku push origin master

Set up database:

    heroku run python manage.py migrate
    heroku run python manage.py loaddata categories.yaml

## Project Layout
  - `core`: Core models
  - `v1`: Hare-compatible API