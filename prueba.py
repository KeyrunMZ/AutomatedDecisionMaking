from turtle import left
import requests
import pandas as pd
from os import system

system("cls")
response = requests.get("https://api.jikan.moe/v4/anime?q=hunter x hunter&sfw")
respuesta = response.json()
df=pd.DataFrame.from_dict(respuesta["data"])
df=df.sort_values(by=['score'],ascending=False)
# print(df[['title','genres','score']])

df2=pd.concat([pd.DataFrame(x) for x in df['genres']], keys=df['title']).reset_index(level=1,drop=True).reset_index()
# print(df2)

df2['name'] = df2.groupby(['title'])['name'].transform(lambda x : ' '.join(x))
df2 = df2[['title','name']].drop_duplicates()   
# print(df2)

df3=pd.merge(df[['title','score']],df2,how='left')
df3.columns=['Titulo','Calificacion','Generos']
print(df3)