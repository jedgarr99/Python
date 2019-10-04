# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:56:49 2019

@author: Jorge Edgar 
"""

class Conta:
    def __init__(self, empresa): # constructor
        self.name=empresa
        self.partes= [None]*6 # el lugar [0] no se usa
        self.partes[1]=ParteConta(1, 'Activo ', 'D')
        self.partes[2]=ParteConta(2, 'Pasivo ', 'A')
        self.partes[3]=ParteConta(3, 'Kapital ', 'A')
        self.partes[4]=ParteConta(4, 'Ingresos ', 'A')
        self.partes[5]=ParteConta(5, 'Egresos ', 'D')
       
    def __str__(self):
        strRes= 'Choro al invocar el método string de los objetos Conta'
        for x in range(1,6):
            strRes=strRes+str(self.partes[4])
        return strRes
   
    def altaCta(self, numCta, nombreCta, natCta):
        dig=numCta//10000
        # // es floor division
        if 1<=dig<=5:
            #print('se pasa la chamba a la parte contable '+str(dig))
            self.partes[dig].altaCta(numCta, nombreCta, natCta)
        else:
            raise Exception('Error al dar de alta la cuenta num '+ str(numCta))
           
class ParteConta:
    def __init__(self, numParte, nombreParte, natParte):
        self.num=numParte
        self.nombre=nombreParte
        # falta validar
        self.nat= natParte
        self.colCtas={}
       
        def __str__(self):
            strRes= 'Parte Contable: '+str(self.num)+' '+self.nombre+' '+self.nat+')'
            for x in self.colCtas.values:
                strRes=strRes+x
            return strRes
       
        def altaCta(self, numCta, nombreCta, natCta):
            #print(self.nombre +' dando de alta la cuenta '+str(numCta)+' '+nombreCta+' {'+natCta+'}')
            if self.colCtas.get(str(numCta)) is None:
                self.colCtas[str(numCta)]=CuentaConta(numCta, nombreCta, natCta)
            else:
                raise Exception('La cuenta ' +str(numCta)+' ya existe')
 
class CuentaConta:
    def __init__(self, numCta, nombreCta, natCta):
        self.num=numCta
        self.nombre=nombreCta
        self.nat=natCta
       
    def __str__(self):
        return 'Cuenta Contable: '+str(self.num)+' '+self.nombre+' '+self.nat+')'
    
    
class PolizaContable:
    def _init_(self, fecha, descripcion):
        self.fecha=fecha
        self.descripcion=descripcion
        self.colMovtos =[]
    def cargo(self,numCta,monto) :
        pass
    def abono(self,numCta,monto):
        pass
    def _str_(self):
        strRes = self.fecha +"  " + self.descripcion
        for m in self.colMovtos:
            strRes += str(m)
            return strRes
    
    def altaMovimientoContable(self, nat, monto):
        print('se pasa la chamba a Movimiento COntable '+str(nat)+"   " +str(monto)) 
       
         
#=========== Programa Principal ==========
conta=Conta('MiEmpre S.A.')
try:
    conta.altaCta(100100, 'Bancos', 'D')
    conta.altaCta(100200, 'Clientes', 'D')
    conta.altaCta(100300, 'Inventario', 'D')
    conta.altaCta(100100, 'Bancos', 'D')
    conta.altaCta(200100, 'Proveedores', 'A')
    conta.altaCta(300000, 'Kapital', 'A')
    conta.altaCta(100100, 'Ventas', 'A')
    conta.altaCta(100100, 'Costo de lo vendido', 'D')
except Exception as e:
    print(str(e))
   
print(conta) # balance
cta=CuentaConta(100100, 'Bancos', 'D')
print(cta)