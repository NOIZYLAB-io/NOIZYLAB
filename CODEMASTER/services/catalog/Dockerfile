FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /data/catalog

EXPOSE 8001

CMD ["uvicorn", "catalog_service:app", "--host", "0.0.0.0", "--port", "8001"]
