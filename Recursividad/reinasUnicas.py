# -*- coding: utf-8 -*-
import numpy as np
"""
Created on Wed Sep 11 20:11:56 2019
            global cont
            global a
            a=np.vstack((a,p))
            cont+=1
            print(cont, p[1:])
@author: Edgar
"""
cont=0
a = np.zeros( (1,8+1), dtype=np.int )
def reina( p, disp, k,n):
    global a
    if k>n :
        ban=True
        este=True
        i=1
        while ban and i<n:
            j=i+1
            while ban and j<=n:

                if p[j]==p[i]+ (j-i) or p[j]==p[i]- (j-i):
                    
                    ban=False
                j+=1
            i+=1
        
        #Rotacion AB
        if ban:
            este=False
            r=1
            while not este and r<a.shape[0]:
                h=1
                este=True
                while este and h<=n:
                    if a[r][p[h]]==n+1-h:
                        h+=1
                    else:
                        este=False
                r+=1  
        
        #Rotacion AC
        if not este:
            este=False
            r=1
            while not este and r<a.shape[0]:
                h=1
                este=True
                while este and h<=n:
                    if a[r][n+1-h]==n+1-p[h]:
                        h+=1
                    else:
                        este=False 
                r+=1
                
        #Rotacion AD
        if not este:
            este=False
            r=1
            while not este and r<a.shape[0]:
                h=1
                este=True
                while este and h<=n:
                    if a[r][n+1-p[h]]==h:
                        h+=1
                    else:
                        este=False
                r+=1
        #giro derecha
        if not este:
            este=False
            r=1
            while not este and r<a.shape[0]:
                h=1
                este=True
                while este and h<=n:
                    if a[r][h]==9-p[h]:
                        h+=1
                    else:
                        este=False
                r+=1
        
        
        
        #giro abajo
        if not este:
            este=False
            r=1
            while not este and r<a.shape[0]:
                h=1
                este=True
                while este and h<=n:
                    if a[r][9-h]==p[h]:
                        h+=1
                    else:
                        este=False
                r+=1
                
       
        #giro diagonal -
        if not este:
            este=False
            r=1
            while not este and r<a.shape[0]:
                h=1
                este=True
                while este and h<=n:
                    if a[r][9-p[h]]==9-h:
                        h+=1
                    else:
                        este=False
                r+=1
                
        #giro diagonal +
        if not este:
            este=False
            r=1
            while not este and r<a.shape[0]:
                h=1
                este=True
                while este and h<=n:
                    if a[r][p[h]]==h:
                        h+=1
                    else:
                        este=False
                r+=1

        if not este :
            global cont
            a=np.vstack((a,p))
            cont+=1
            print(cont,p[1:])
 
    else:
        for w in range (1,n+1):
            if disp[w] ==1:
                disp[w] =0
                p[k]=w
                reina(p,disp,k+1, n)
                disp[w]=1
  
def reinas(n):
    p=[0]*(n+1)
    d=[1]*(n+1)
    reina(p,d,1,n)
    
