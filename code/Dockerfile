# Dockerfile
FROM python:3.9-slim
# Don't write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE=1
# Force the stdout and stderr streams to be unbuffered
ENV PYTHONUNBUFFERED=1
# Upgrade pip tool
RUN pip install --upgrade pip
# Change workdir
WORKDIR /app
# Copy requirements.txt to 
COPY requirements.txt /app/
# Install dependencies
RUN pip install -r requirements.txt
COPY . /app/