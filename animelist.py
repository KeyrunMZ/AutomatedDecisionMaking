### LIBRERÍAS
    ### para generar requests
import requests
    ### para lidiar con dataframes
import pandas as pd

### PEDIR NOMBRE DEL ANIME
def AnimeName():
    print("Cómo se llama el anime a buscar?")
    nombre = input()
    AnimeList(nombre)

### MOSTRAR LISTA DE ANIMES
def AnimeList(nombre):
    ### Probemos a llamar una API
    response = requests.get("https://api.jikan.moe/v4/anime?q="+str(nombre)+"&sfw")
    #print(response.json())

    respuesta = response.json()
    #print(respuesta)

    ### Para ver todo el contenido de la API
    #print(json.dumps(respuesta["data"][1],indent=10))

    #for anime in respuesta["data"]:
    #    print("Título: " + str(anime["title"]) + " -> Calificación: " + str(anime["score"]))

    df=pd.DataFrame.from_dict(respuesta["data"])
    df=df.sort_values(by=['score'],ascending=False)

    ### Desanidamos la lista de diccionarios de la columna generos
    df2=pd.concat([pd.DataFrame(x) for x in df['genres']], keys=df['title']).reset_index(level=1,drop=True).reset_index()
    #print(df2)

    ### Concatenamos los diferentes generos según el título
    df2['name'] = df2.groupby(['title'])['name'].transform(lambda x : ' '.join(x))
    df2 = df2[['title','name']].drop_duplicates()   
    # print(df2)

    ### Realizamos un join con tabla de titulos y calificaciónes
    df3=pd.merge(df[['title','score']],df2,how='left')
    df3.columns=['Titulo','Calificacion','Generos']
    print(df3)
