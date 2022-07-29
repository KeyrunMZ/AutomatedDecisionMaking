# LIBRERÍAS
    # para limpiar pantalla
from http.client import SWITCHING_PROTOCOLS
from os import system
    # para ver la hora del sistema
import datetime

from animelist import AnimeMenu
from snake import SnakeGame

def Menu():
        
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
    print("1. Buscar Anime")
    print("2. Jugar Snake")
    print("0. Salir")
    seleccion = input("Ingrese su selección: ")

    system("cls")
    if seleccion == '1':
        print("Buscar anime")
        # Llamamos la función de lista de animes por nombre
        AnimeMenu()
    elif seleccion == '2':
        print("Jugar Snake")
        # Llamamos la función de lista de animes por género
        SnakeGame()
    elif seleccion == '0':
        # Terminamos el programa
        print("Hasta pronto!")
    else:
        # Llamamos la función de menú
        print("Debes ingresar una de las opciones")
        print("Presiona cualquier tecla para volver al menú")
        input()
        Menu()

    

if __name__ == '__main__':
    Menu()
