FROM python:3.13-bullseye

# Environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Up Workspace
WORKDIR /code

# Dependenci Installation
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .