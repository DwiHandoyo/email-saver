FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

COPY requirements.txt /app

# RUN apt install libpq-dev python-dev

RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./app /app

EXPOSE 5000