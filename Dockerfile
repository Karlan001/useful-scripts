FROM python:3.10

WORKDIR /django-site/receipt

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY reciepts .
