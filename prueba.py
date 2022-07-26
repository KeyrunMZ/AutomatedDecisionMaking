from turtle import left
import requests
import pandas as pd
from os import system
import json

system("cls")

def AnimeRequest(nombre,genero,year):
    peticion=str("https://api.jikan.moe/v4/anime?q="+nombre+"&genres="+genero+"&start_date="+year+"&order_by=score&sort=desc")
    #peticion=str("https://api.jikan.moe/v4/anime?q="+nombre+"&genres="+genero+"&order_by=score&sort=desc")
    print(peticion)
    response = requests.get(peticion)
    respuesta = response.json()

AnimeRequest("","","2000")