FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask mysql-connector-python celery redis

CMD ["flask", "run", "--host=0.0.0.0"]
