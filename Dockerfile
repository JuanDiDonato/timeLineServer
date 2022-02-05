# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=3ohero32892hdfweufhr392hfwhfwoefhẃqofehqfqehr832
ENV ACCESS_TOKEN_LIFETIME=15
ENV REFRESH_TOKEN_LIFETIME=1

WORKDIR /code
COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

