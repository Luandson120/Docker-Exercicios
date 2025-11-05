# Etapa base
FROM python:3.11-alpine AS base
WORKDIR /app
RUN apk add --no-cache gcc musl-dev postgresql-dev
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa de desenvolvimento
FROM base AS dev
COPY src/ ./src
WORKDIR /app/src
EXPOSE 3000
CMD ["flask", "--app", "app.py", "run", "--host=0.0.0.0", "--port=3000", "--debug"]

# Etapa de produção
FROM base AS prod
COPY src/ ./src
WORKDIR /app/src
EXPOSE 3000
CMD ["python", "app.py"]
