# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

print("hola mundo DAI")

x=10
y=12.5
z='100'

type(x)

xy=x+y
xz1=str(x)+z
xz2=x+int(z)

a=10
b=3
division=a/b
cociente=a//b
residuo=a%b
#

c=1234.56789
d=100

import math

help("keywords")
print(c, d, math.pi)

# lista - mutable
strA='AAA'
listA=['a', 'e', 'i', 'o', 'u']
listB=[100, listA, 10, 20, strA]
print(listB)

strA='aaaa'
listB[3]='woow'

print(listB)

# tuplas - inmutable

tupla={1, 'python', true}

print(type(tupla))
print(tupla)

#conjunto - mutable

conj2=set{}