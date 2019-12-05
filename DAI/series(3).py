# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""



#series con Pandas
#unidimensional-- contiene datos de cualquier tipo

import pandas as pd #nomenclatura universal

#crear una serie vacía
s = pd.Series()
print(s)

#crear una serie de un arreglo con índices determinados
import numpy as np #biblioteca para manejar arreglos en python
data = np.array(['a', 'b', 'c', 'd'])
sa = pd.Series(data)
print (data) #lista de cosas
print(sa) #columna de cosas (visualmente más friendly)

#crear una serie pero con índices dados; i.e. nosotros decidimos cuál es el indice
data = np.array(['a', 'b', 'c', 'd'])
sai = pd.Series(data, index = [100,200,300,400]) #datos, indices
print(sai)

#crear una serie desde un diccionario
data={'a' : 0, 'b':1, 'c':2}
sd = pd.Series(data)
print (sd)

#los datos erróneos son None, NaN
data = data={'a' : 0, 'b':1, 'c':2}
sd2 = pd.Series(data, index = ['a', 'c', 'd', 'b'])
print (sd2)

#crear una serie con un escalar
se = pd.Series(5, index =[1,2,3])
print (se)

#CRUD create read update delete
#accesar los datos de una serie
#posición
sEjemplo = pd.Series([1,2,3,4,5], index = ['a', 'b', 'c', 'd', 'e'])
print(sEjemplo)

#acceso al elemento cero con índice y con número
print(sEjemplo[0]) #conserva el índice numérico
print(sEjemplo['a'])


#sí sirve slicing
print(sEjemplo[['a', 'b', 'c']])
print(sEjemplo[:3])
print(sEjemplo[-3:])

print(sEjemplo.iloc[0]) #por posición
print(sEjemplo.loc['a']) #por etiqueta

#Update
sEjemplo['a'] = 100
print(sEjemplo)

#delete
del(sEjemplo['a'])
print(sEjemplo)

#métodos de las series
sEjemplo2 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(sEjemplo2)

print(sEjemplo2.count()) #cuenta cuántos elementos hay en total en la serie
print(sEjemplo2.value_counts())
print(sEjemplo2.unique()) #regresa una lista con los valores únicos

#estadísticas
print(sEjemplo2.mean())
print(sEjemplo2.median())
print(sEjemplo2.describe()) #todos los datos estadísticos rápidamente
print(sEjemplo2.min())
print(sEjemplo2.idxmin())
print(sEjemplo2.max())
print(sEjemplo2.idxmin())
print(sEjemplo2.sort_index())
print(sEjemplo2.sort_values())
print(sEjemplo2.var()) 
print(sEjemplo2.std())

#mascara
mask = sEjemplo2 > sEjemplo2.mean()
mask

sEjemplo2[mask]

#gráfica de una serie
import matplotlib.pyplot as plt
fig = plt.figure()
sEjemplo2.plot()
sEjemplo2.plot(kind = 'bar', color = 'k', alpha  = .2)
