FROM python:3.11-alpine AS base

WORKDIR /app

RUN apk add --no-cache gcc musl-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 3000

CMD ["python", "app/app.py"]
