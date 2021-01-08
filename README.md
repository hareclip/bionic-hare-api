# Bionic Hare

A port of the Hare's API to Django

## Setup

Create `.env` from `sample.env` and insert credentials.

Create virtual environment, install dependences, and migrate models:

    python -m venv ./venv
    ./venv/Scripts/activate
    pip install requirements.txt
    python manage.py migrate

### Development

Run development server with:

    python manage.py runserver

### Production

Run production with:

    TODO

## Project Layout
  - `core`: Core models
  - `v1`: Hare-compatible API