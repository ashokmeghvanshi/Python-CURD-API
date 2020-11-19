FROM python:3.6.8-alpine

LABEL image for simple flask API application

WORKDIR /flask_app

COPY . .

RUN ["pip3", "install", "pipenv"]

RUN ["pipenv", "install"]

RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 8000
CMD pipenv run python app.py

