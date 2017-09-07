FROM python:2-alpine3.6

ENV PYTHONPATH "$PYTHONPATH:/usr/lib/python2.7/site-packages/"

RUN apk update && apk add git py-unbound py-ipaddr py-pip openssl openssl-dev musl-dev gcc && \
        pip install m2crypto && \
        mkdir /swede && \
        git clone https://github.com/pieterlexis/swede.git /swede && \
        apk del py-pip openssl-dev musl-dev gcc git && \
    rm -rf /var/cache/apk/*

ENTRYPOINT  [ "python", "/swede/swede" ]
