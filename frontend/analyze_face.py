import requests
import matplotlib.pyplot as plt

# Endpoint delle API
LOGIN_URL = 'http://localhost:5000/login'
ANALYZE_URL = 'http://localhost:5000/analyze'

# Credenziali di login
credentials = {
    'username': 'admin',
    'password': 'admin123'
}

# 1. Richiesta di login per ottenere il token
response = requests.post(LOGIN_URL, json=credentials)
response.raise_for_status()
token = response.json().get('token')

if not token:
    raise ValueError("Token non trovato nella risposta!")

# 2. Caricamento immagine e invio a /analyze con token Bearer
headers = {
    'Authorization': f'Bearer {token}'
}
files = {
    # 'image': open('images/face.png', 'rb')
    'image': open('images/ride.jpg', 'rb')
}

response = requests.post(ANALYZE_URL, headers=headers, files=files)
response.raise_for_status()
result = response.json()

# 3. Disegno del grafico a linea
labels = list(result.keys())
values = list(result.values())

plt.figure(figsize=(10, 5))
plt.plot(labels, values, marker='o', linestyle='-')
plt.title('Risultati analisi emozioni')
plt.xlabel('Emozioni')
plt.ylabel('Percentuale')
plt.grid(True)
plt.tight_layout()
plt.show()
