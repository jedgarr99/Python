# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:42:53 2019

@author: dai
"""

import pandas as pd

# CRUD
# crear un dataFrame desde un diccionario
datos={'nombre': ['Diego', 'Sebastian', 'Luisa'], 'Calificaciones':['10', '9', '9'], 'Deportes':['futbol', 'basquetbol', 'tenis'], 'Materias': ['DAI', 'ap', 'ap']}
df=pd.DataFrame(datos)
print(df)
print(df.info())

nuevo=pd.DataFrame(datos2)
