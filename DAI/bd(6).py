# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:14:25 2019

@author: dai
"""

import pyodbc 

direccion_servidor = 'CC102-16\SA'
nombre_bd = 'baseCine'
nombre_usuario = 'sa'
password = 'adminadmin'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("\n"*2)
    print("conexión exitosa")
    
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
    

