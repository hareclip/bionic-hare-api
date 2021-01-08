# Bionic Hare

A port of the Hare's API to Django

## Setup

Create `.env` from `sample.env` and insert credentials.

Create virtual environment and install dependences:

    python -m venv ./venv
    ./venv/Scripts/activate
    pip install requirements.txt

Set up database:

    python manage.py migrate
    python manage.py loaddata categories.yaml

### Development

Run development server with:

    python manage.py runserver

### Production

Run production with:

    TODO

## Project Layout
  - `core`: Core models
  - `v1`: Hare-compatible API