
#
# Dockerfile for Development
#

FROM python:3
ENV PYTHONUNBUFFERED 1

# Setup project
RUN mkdir -p /code
COPY . /code

WORKDIR /code
RUN pip3 install -r requirements/development.txt

