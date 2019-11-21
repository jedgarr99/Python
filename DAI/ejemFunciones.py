# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:18:04 2019

@author: dai
"""
import math as m

def suma(a, b):
    return a+b

def suma (a=1, b=None):
    if b== None:
        return a
    else:
        return a+b
    
def circulo(radio):
    return m.pi*radio**2,m.pi*2*radio

def saludar(idioma):
    def esp():
        print('hola')
    def ing():
        print('hello')
    def fran():
        print('salut')
    idiomaFun={'es':esp,
               'in':ing,
               'fr':fran}
    return idiomaFun[idioma]

resta=lambda x,y:x-y

def cubo(x):
    return x**3

lista=[1,2,3,4,5]

print(list(map(cubo, lista)))

def lee(archivo):
    id=open(archivo, 'r')
    contenido= id.read()
    listaRes=contenido.split('\n')
    id.close
    return listaRes