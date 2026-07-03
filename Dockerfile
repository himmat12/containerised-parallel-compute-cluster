FROM python:3.11-slim

WORKDIR /app

RUN pip install -r ./requirements.py

COPY . .

CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]