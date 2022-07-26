# LIBRERÍAS
    # para limpiar pantalla
from http.client import SWITCHING_PROTOCOLS
from os import system
    # para ver la hora del sistema
import datetime

    # animelist.py
from animelist import AnimeGenero, AnimeName, AnimeYear

def MenuInicio():
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

    # Creamos un menú
    print("Selecciona el # de una de las siguientes opciones:")
    print("1. Buscar anime por nombre")
    print("2. Buscar anime por género")
    print("3. Buscar anime por año de salida")
    print("0. Salir")
    seleccion = input("Ingrese su selección: ")

    system("cls")
    if seleccion == '1':
        print("Buscar anime por nombre")
        # Llamamos la función de lista de animes por nombre
        AnimeName()
    elif seleccion == '2':
        print("Buscar anime por género")
        # Llamamos la función de lista de animes por género
        AnimeGenero()
    elif seleccion == '3':
        print("Buscar anime por año")
        # Llamamos la función de lista de animes por año
        AnimeYear()
    elif seleccion == '0':
        # Terminamos el programa
        print("Hasta pronto!")
    else:
        # Llamamos la función de menú
        print("Debes ingresar una de las opciones")
        print("Presiona cualquier tecla para volver al menú")
        input()
        MenuInicio()

if __name__ == '__main__':
    MenuInicio()
