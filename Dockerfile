FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-gi \
    python3-gi-cairo \
    gir1.2-webkit2-4.0 \
    python3-dev \
    pkg-config \
    libcairo2-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"] 