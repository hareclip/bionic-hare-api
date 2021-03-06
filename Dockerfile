FROM python:3.6-alpine

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libffi-dev bash build-base py-pip jpeg-dev zlib-dev

RUN python3 -m pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .