# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:30:15 2019

@author: Edgar
"""

import sys
f = open ('datos.txt','r')
n=sys.argv
i=1

for x in range(0, int(f.readline())):
    a=int(f.readline())
    b=int(f.readline())
    print("La suma de", a, "y", b, "es", a+b)
    i=i+1

f.close()