# -*- coding: utf-8 sympy.sqrt((j-i)**2 +(p[i]-p[j])**2)%sympy.sqrt(2)==0:-*-
def per( p, disp, k,n):
    if k>n :
        print(p[1:])
    else:
        for w in range (1,n+1):
            if disp[w] ==1:
                disp[w] =0
                p[k]=w
                per(p,disp,k+1, n)
                disp[w]=1

def permuta(n):
    p=[0]*(n+1)
    d=[1]*(n+1)
    per(p,d,1,n)

def reina( p, disp, k,n):
    if k>n :
        ban=True
        i=1
        while ban and i<n:
            j=i+1
            while ban and j<=n:

                if p[j]==p[i]+ (j-i) or p[j]==p[i]- (j-i):
                    
                    ban=False
                j+=1
            i+=1
        
        if ban:
            print(p[1:])
 
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