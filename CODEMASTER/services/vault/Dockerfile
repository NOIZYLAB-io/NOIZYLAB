FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY . .

# Create data directories
RUN mkdir -p /data/vault /data/logs

EXPOSE 8000

CMD ["uvicorn", "vault_service:app", "--host", "0.0.0.0", "--port", "8000"]
