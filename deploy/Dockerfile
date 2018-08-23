FROM python:3.6-alpine

MAINTAINER anudeepsamaiya@gmail.com

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy project
COPY ./app /Project/app

# Copy Pipfile
COPY ./Pipfile* /Project/

# Set work directory
WORKDIR /Project/app

# Install dependencies
RUN pip install --upgrade pip && pip install pipenv \
    && pipenv install --system --deploy --dev
