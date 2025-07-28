FROM python:3.10-slim

# Librerie di sistema necessarie per OpenCV e DeepFace
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia requirements separatamente per caching intelligente
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia solo il codice
COPY . .

CMD ["python", "main.py"]