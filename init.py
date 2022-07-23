# LIBRERÍAS
    # para limpiar pantalla
from os import system
    # para ver la hora del sistema
import datetime

    # animelist.py
from animelist import AnimeName


# Limpiar pantalla
system("cls")

# Capturamos la hora del sistema
hora=datetime.datetime.now().hour

# Saludo
if (hora > 6 and hora <= 12):
    print("Buen día mi señor")
elif (hora > 12 and hora <= 18):
    print("Buena tarde mi señor")
else:
    print("Buena noche mi señor")

# Llamamos la función de lista de animes
AnimeName()