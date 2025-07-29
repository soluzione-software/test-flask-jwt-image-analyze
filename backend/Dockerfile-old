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

COPY tests/dataset/img1.jpg tests/dataset/img1.jpg
RUN python -c "from deepface import DeepFace; DeepFace.analyze(img_path='tests/dataset/ride.jpg', actions=['emotion'])" || true


# Copia solo il codice
COPY . .

EXPOSE 5000

# Avvio con server WSGI
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "main:app"]
