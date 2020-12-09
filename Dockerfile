FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update && \
  apk add bash py-pip && \
  apk add --virtual=build gcc libffi-dev musl-dev openssl-dev python3-dev make && \
  pip --no-cache-dir install -U pip && \
  apk del --purge build

RUN apk add --update \
    supervisor \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev \
    postgresql-dev \
    gcc 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./docker_entrypoint.sh

ENTRYPOINT [ "./docker_entrypoint.sh" ]