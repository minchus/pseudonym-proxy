FROM python:3.12.4-alpine

RUN apk add curl

ADD ./app /code/app
ADD requirements.txt /code/requirements.txt

WORKDIR /code

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000
HEALTHCHECK CMD curl --fail http://localhost:5000/

CMD ["sh", "-c", "gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5000 --log-file - app:app"]

