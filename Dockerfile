FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /django-project/app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "reciepts.wsgi:application", "--bind 0.0.0.0:8000"]
