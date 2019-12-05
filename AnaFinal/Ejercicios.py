# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:16:31 2019

@author: dai
"""

#1.	Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
#Ejemplo:
#Frase= 'fin de curso de DAI'
#Resultado= {'fin': 3, 'de': 2, 'curso': 5, 'DAI': 3}

def cuantas(frase):
    palabras=frase.split()
    tamaño=map(len,palabras)
    return dict(zip(palabras,tamaño))

def cuantas2(frase):
    return{palabra:len(palabra)for palabra in frase.split()}
    
print (cuantas("fin de curso DAI"))
#2.	Ejercicio de pandas
#Carga los datos de titulos.csv a un dataframe llamado datos
#Muestra los primeros datos para conocer el dataframe
#Cuántos datos tiene el dataframe (cuántas peliculas hay)
# En que años se presentó "Batman" 
# Cuáles son las peliculas mas antiguas 
# Listar todas las peliculas que contengan la palabra "Exorcist"  ordenadas de la más vieja a la más reciente.
# Cuántas películas fueron hechas de 1950 a 1959
#cuántas películas hay por año
import pandas as pd
datos=pd.read_csv('titulos.csv')

datos.head()
print(datos['title'].count())
len(datos)

datos[datos.title=="Batman"]

datos.sort_values('year').head()

datos[datos.title.str.contains('Exorcist')].sort_values('year')
#3.	Ejercicio con la base de datos Consar
##con la base de datos de SQL: Consar19
#muestra en una lista la información de la tabla de personas
##inserta dos ahorros a Rodolfo
#muestra todos los montos de Rodolfo
