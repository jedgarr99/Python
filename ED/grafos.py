# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:12:10 2019

@author: Edgar
"""

#LISTA DE ADYACENCIA 

#(Implementada con diccionarios)

#librerías importadas para graficar el grafo:
import networkx as nx
import matplotlib as plt
import heapdict as hp
import numpy as np

#Definición de la clase:
class Grafo:
    
  #Atributos:
  G={}
  visitados={}

  #Constructor:
  def __init__(self):
    self.G={}
    self.visitado={}

  #Métodos:
  def inserta(self,v1, v2, peso=0):
    G=self.G
    if v1 not in G:
      G[v1] = {}
    if v2 not in G:
      G[v2] = {}
    G[v1][v2] = peso
  
  def insertaSimetrico(self, v1, v2, peso=0):
    self.inserta(v1, v2, peso)
    self.inserta(v2, v1, peso)
  
  def toString(self):
    G=self.G
    for v1 in G:
      for v2 in G[v1]:
        print(v1, "-->", v2, G[v1][v2])

  #getGrafo--> método que regresa el grafo como un diccionario con listas, con la intención futura de
  #pasarle este objeto al graficador de la libreria networkx: 'grafo=nx.DiGraph(G.getGrafo())'
  def getGrafo(self):
    G=self.G
    G2={}
    for v1 in G:
      G2[v1] = []
      for v2 in G[v1]:
        G2[v1] += [v2]      #así concatenas elementos a una lista. ej. a=[]  ;  a+= [3]
    return G2


  #Recorrido a profundidad:  (Depht First Search)
  def profundidad(self):
    G= self.G
    visitados = self.visitados
    #Inicializa todos los valores de los nodos en falso, pues no han sido visitados:
    for v1 in G:
      visitados[v1] = False
    recorrido=[]
    for v1 in G:
      if not visitados[v1]:
        self.DFS(v1, recorrido)
    return recorrido

  def DFS(self, v1, recorrido):  #Depth First Search
    if self.visitados[v1]:
      return
    self.visitados[v1] = True
    recorrido+= [v1]
    for v2 in self.G[v1]:
      self.DFS(v2, recorrido)
    
  def BFS(self):
      
  
        # Mark all the vertices as not visited 
        visitados = self.visitados
        G= self.G
        for v1 in G:
            visitados[v1] = False
            
      
        v1=list(self.G.keys())[0]
        
  
        # Create a queue for BFS 
        cola = [] 
        recorrido=[]
  
        # Mark the source node as  
        # visited and enqueue it 
        cola.append(v1) 
        visitados[v1] = True
  
        while cola: 
  
            # Dequeue a vertex from  
            # queue and print it 
            v1 = cola.pop(0) 
            recorrido+=v1
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.G[v1]: 
                if visitados[i] == False: 
                    cola.append(i) 
                    visitados[i] = True
        return recorrido
  

  #Método Prim
  def prim(self, v):
    G = self.G
    papa = {}
    visitado = self.visitado 
    Q = hp.heapdict()
    for u in G :
      papa[u] = None
      visitado[u] = False
      Q[u] = np.inf
    Q[v] = 0
    i = 0
    l = len(Q)
    while i<l:
      i += 1
      v1, peso = Q.popitem()
      visitado[v1] = True
      for v2 in G[v1]:
        if not visitado[v2] and G[v1][v2] < Q[v2]:
          papa[v2] = v1
          Q[v2] = G[v1][v2]
    return papa
  
  #DIXTRA
  def masCortoDeVerticeAVertice(self, v):
    G = self.G
    papa = {}
    visitado = self.visitado 
    Q = hp.heapdict()
    for u in G :
      papa[u] = None
      visitado[u] = False
      Q[u] = np.inf
    Q[v] = 0
    i = 0
    l = len(Q)
    while i<l:
      i += 1
      v1, peso = Q.popitem()
      visitado[v1] = True
      for v2 in G[v1]:
        if  visitado[v2] and G[v1][v2] + G[v1][v2] < Q[v2]:
          papa[v2] = v1
          Q[v2] = G[v1][v2] 
    return papa

G=Grafo()
G.insertaSimetrico("a", "b", 4)
G.insertaSimetrico("a","b",4)
G.insertaSimetrico("a","h",8)
G.insertaSimetrico("b","h",11)
G.insertaSimetrico("c","i",2)
G.insertaSimetrico("i","h",7)
G.insertaSimetrico("b","c",8)
G.insertaSimetrico("g","i",6)
G.insertaSimetrico("h","g",1)
G.insertaSimetrico("d","c",7)
G.insertaSimetrico("g","f",2)
G.insertaSimetrico("c","f",4)
G.insertaSimetrico("d","e",9)
G.insertaSimetrico("f","d",14)
G.insertaSimetrico("e","f",10)


print('getGrafo() --> ', G.getGrafo())
print('\n')
print('Recorrido a profundidad: ', G.profundidad())
print('\n')
print('Grafo toString: ')
G.toString()

print('\n')
print('Grafo graficado con networkx y matplotlib: ')
grafo=nx.DiGraph(G.getGrafo())
nx.draw(grafo, with_labels=True)

print("Solución del prim: ")
print('\n')
G.prim('a')

print('Recorrido anchura: ', G.BFS())
