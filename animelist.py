### LIBRERÍAS
    ### para generar requests
import requests
    ### para lidiar con dataframes
import pandas as pd
    ### para lidiar con jsons
import json

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

### MOSTRAR LISTA DE ANIMES V3
def AnimeRequest(nombre,genero,year):
    response = requests.get("https://api.jikan.moe/v4/anime?q="+str(nombre)+"&genres="+str(genero)+"&start_date="+str(year)+"&order_by=score&sort=desc")
    respuesta = response.json()
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