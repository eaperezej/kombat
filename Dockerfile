FROM python:3.10-alpine

WORKDIR /kombat

COPY . .

RUN pip install -r requirements.txt
