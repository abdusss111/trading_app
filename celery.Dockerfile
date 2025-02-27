FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Start Celery worker
CMD ["celery", "-A", "mini_proj", "worker", "--loglevel=info"]
