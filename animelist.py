### LIBRERÍAS
    ### para generar requests
import requests
    ### para lidiar con dataframes
import pandas as pd
from os import system

### ANIME MENU
def AnimeMenu():
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

### PEDIR NOMBRE DEL ANIME
def AnimeName():
    name = input("Cómo se llama el anime a buscar? ")
    AnimeRequest(nombre=name,genero="",year="0")

### PEDIR GENERO DEL ANIME
def AnimeGenero():
    print("Cuál es el género del anime a buscar?")
    ### Primero debemos mostrar la lista de generos
    response = requests.get("https://api.jikan.moe/v4/genres/anime")
    respuesta = response.json()
    i=0
    for genero in respuesta["data"]:
        if i == 5:
            i=0
            print()
        print(str(genero["mal_id"])+". "+str(genero["name"]), end="\t")
        i+=1
    print()
    genre=input("Ingresa el número del género: ")
    AnimeRequest(nombre="",genero=genre,year="0")

def AnimeYear():
    year = input("De qué año es el anime a buscar?")
    AnimeRequest(nombre="",genero="",year=year)

### MOSTRAR LISTA DE ANIMES
def AnimeRequest(nombre,genero,year):
    response = requests.get("https://api.jikan.moe/v4/anime?q="+str(nombre)+"&genres="+str(genero)+"&order_by=score&sort=desc&start_date="+str(year))
    respuesta = response.json()
    #print(respuesta["data"])
    df=pd.DataFrame.from_dict(respuesta["data"])

    ### Desanidamos la lista de diccionarios de la columna generos
    df2=pd.concat([pd.DataFrame(x) for x in df['genres']], keys=df['title']).reset_index(level=1,drop=True).reset_index()

    ### Concatenamos los diferentes generos según el título
    df2['name'] = df2.groupby(['title'])['name'].transform(lambda x : ' '.join(x))
    df2 = df2[['title','name']].drop_duplicates()  

    ### Realizamos un join con tabla de titulos y calificaciónes
    df3=pd.merge(df[['title','score']],df2,how='left')
    df3.columns=['Titulo','Calificacion','Generos']
    print(df3)