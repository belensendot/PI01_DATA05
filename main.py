from fastapi import FastAPI , Path, UploadFile, File
from typing import Optional
from pydantic import BaseModel
import shutil
import pandas as pd
import numpy as np

app=FastAPI(title='Consultas por Streaming',
description= ' En esta API se podran realizar consultas a los datos de las plataformas de streaming Amazon, DisneyPlus, Hulu y Netflix',
version='1.1.1.1')

df_total=pd.read_csv('general.csv')
df_genero=pd.read_csv('generos.csv')
df_actores=pd.read_csv('actores.csv')


@app.get('/get_max_duration')
async def get_max_duration(año:int, plataforma:str, tipo_duracion:str):
    return {df_total[(df_total['Ano_realizacion']==año)&(df_total['Plataforma']==plataforma)&(df_total['tipo (min-Seasons)']== tipo_duracion)]['Duracion'].max().tolist()}
    
    
@app.get('/get_count_plataform')
async def get_count_plataform(plataforma:str):   
    return{f"Cantidad de películas en {plataforma} es":df_total[(df_total['Plataforma']==plataforma)&(df_total['Tipo_film']=='movie')]['Tipo_film'].count().tolist(),
    f"Cantidad de series en {plataforma} es":df_total[(df_total['Plataforma']==plataforma)&(df_total['Tipo_film']=='tv show')]['Tipo_film'].count().tolist()}

@app.get('/get_listedin')
async def get_listedin(genero:str):
    list_genero = []
    for plataforma in df_total['Plataforma'].unique():
        list_genero.append(df_genero[(df_genero['genero']==genero)&(df_genero['plataforma']==plataforma)].shape[0])
    
    maximo = max(list_genero)
    if list_genero.index(maximo)==0:
        return {'amazon': maximo}
    elif list_genero.index(maximo)==1:
        return {'disney': maximo}
    elif list_genero.index(maximo)==2:
        return {'hulu': maximo}
    elif list_genero.index('netflix',maximo)==2:
        return {'netflix': maximo}

@app.get('/get_actor')
async def get_actor(plataforma:str, año:int):
    data = df_actores[(df_actores['year']==año)&(df_actores['plataforma']==plataforma)]['actor']
    # return {data.value_counts().max()}
    if data.value_counts().index[0] == 'sin dato':
        return {data.value_counts().index[1]:data.value_counts()[1].tolist()}
    elif data.value_counts().index[0] != 'sin dato':
        return {data.value_counts().index[0]:data.value_counts()[0].tolist()}
