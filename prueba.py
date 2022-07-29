
    ### para generar requests
import requests
import pandas as pd
nombre="hunter"
genero=""
year="0"

#response = requests.get("https://api.jikan.moe/v4/anime?q="+str(nombre)+"&genres="+str(genero)+"&order_by=score&sort=desc&start_date="+str(year))
response = requests.get("https://api.jikan.moe/v4/anime?q="+str(nombre)+"&genres="+str(genero)+"&order_by=score&sort=desc&start_date="+str(year))
respuesta = response.json()
df=pd.DataFrame.from_dict(respuesta["data"])
print(df)