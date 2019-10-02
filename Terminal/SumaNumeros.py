# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:21:07 2019

@author: Edgar
"""
import sys
n=sys.argv
i=1
for x in range(0, int(sys.argv[1])):
    
    print("La suma de", sys.argv[2*i], "y", sys.argv[2*i+1], "es", int(sys.argv[2*i])+ int(sys.argv[2*i+1]))
    i=i+1