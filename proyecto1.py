# LIBRERÍAS
    # para limpiar pantalla
from os import system
    # para generar requests
import requests
    # para lidiar con jsons
import json

# Limpiar pantalla
system("cls")
print("Buena noche mi señor")

# Probemos a llamar una API
response = requests.get("https://api.jikan.moe/v4/anime?q=hunterxhunter&sfw")
#print(response.json())

respuesta = response.json()
#print(respuesta)

print(json.dumps(respuesta,indent=10))