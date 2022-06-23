FROM python:3.10

WORKDIR /app

RUN pip3 install django

ENV PYTHONUNBUFFERED 1

ADD . /app

CMD python3 manage.py runserver 0.0.0.0:80
