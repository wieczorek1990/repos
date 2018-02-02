FROM python:3
RUN apt-get update &&\
 apt-get install -y postgresql-client &&\
 rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
WORKDIR /srv
ADD requirements.txt /srv
RUN pip install -r requirements.txt
CMD bin/wait postgres --\
 python repositories/manage.py migrate &&\
 python repositories/manage.py runserver 0.0.0.0:8000
