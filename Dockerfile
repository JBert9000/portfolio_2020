# pull official base image
FROM python:3.7-alpine

# set work directory
WORKDIR /portfolio_2020_container

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# add and run as non-root user
RUN adduser -D john
USER john

# run gunicorn
CMD gunicorn portfolio_2020.wsgi:application --bind 0.0.0.0:$PORT
