# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#Se importan las librerías pandas, numpy y pickle
import pandas as pd 
import numpy as np 
import pickle as pck 
import feather as fea
 
#Se pide a pandas que los datos de tipo float con solo dos digitos después del punto decimal
pd.options.display.float_format = '{:,.2f}'.format

trayf="C:/Users/JRODRIGUORT/Desktop/Employees/FeatherFormat/"

emp = fea.read_dataframe(trayf + "Employees.fea")
print("Leido el archivo Employees.dat en el dataframe emp")

dept = fea.read_dataframe(trayf + "Departments.fea")
print("Leido el archivo Departments.dat en el dataframe dept")

dept_emp = fea.read_dataframe(trayf + "dept_emp.fea")
print("Leido el archivo Dept_emp.dat en el dataframe dept_emp")

dept_manager = fea.read_dataframe(trayf + "dept_manager.fea")
print("Leido el archivo Dept_manager.dat en el dataframe dept_manager")

salaries = fea.read_dataframe(trayf + "salaries.fea")
print("Leido el archivo Salaries.dat en el dataframe salaries")

titles = fea.read_dataframe(trayf + "titles.fea")
print("Leido el archivo Titles.dat en el dataframe titles")

emp.dtypes


#1 Considere la última fecha de contratación, salida, cambio de status. ¿Cuál es esa fecha? 
#Se juntan las fechas con la ayuda de pandas.concat() 
allDates=pd.concat([dept_emp.from_date, dept_emp.to_date, emp.hire_date, salaries.from_date, salaries.to_date, dept_manager.from_date, dept_manager.to_date, titles.to_date, titles.from_date]) 
print(allDates)
print('\n Pregunta 1:') 
print("La última fecha de contratación, salida, cambio de status es:"+(str)(allDates.max())) 


#2  ¿A qué edad(es) contrata más personal la empresa? 
#Se añade una serie (columna) al DataFrame emp donde se calcula la edad a la que el empleado fue contratado 
#se divide entre un intervalo de tiempo (np.timedelta64) de un año para poder redondear la edad al año y se convierte a entero (np.int64) para que tenga el formato correcto 
emp['hire_age']=((emp.hire_date - emp.birth_date)/np.timedelta64(1,'Y')).astype(np.int64) 
emp.head()

#Se cuentan las edades de los empleados y se ordenan a los empleados por edad de mayor a menor y 
#se sacan los índices, después, se sacan el índice y los valores de la primera edad. 
maxAgeIndex=emp.groupby(['hire_age']).hire_age.count().sort_values(ascending=False)[:1].index[0]
print(maxAgeIndex)

#3  ¿Cuál(es) es(son) la(s) edad(es) a la que se contratan más los hombres? 
#Se cuentan las edades a las que fueron contratados los empleados y se ordenan de mayor a menor 
x=emp.groupby(['gender','hire_age']).hire_age.count().sort_values(ascending=False) 

print(x)
xm=x['M'] 
print(xm)
print('\n Pregunta 3:') 
print('La empresa contrata más a los hombres de: '+str(xm.sort_values(ascending=False).index[0])+" años") 


#4  ¿Cuál(es) es(son) la(s) edad(es) a la que se contratan más las mujeres? 
#Se filtran para solo tener a las mujeres 
xf=x['F'] 
print('\n Pregunta 4:') 
print('La empresa contrata más a las mujeres de: '+str(xf.sort_values(ascending=False).index[0])+" años") 

#5 ¿Cuántos empleados tiene actualmente la empresa? 
#Se solicita como entreda la fecha actual 
date=pd.to_datetime(input('\nDame la fecha de hoy (aaaa-mm-dd): \n')) 

#Mediante filtros se excluyen a los empleados que no están activos (que la fecha de #cuando el empleado ingresó al departamento donde trabaja sea menor a la fecha actual #o que la fecha de cuando se fue del departamento sea mayor a la fecha dada o que sea #nula, ya que sigue estando en ese departamento) 
f1 = dept_emp.from_date < date 
f2_1 = dept_emp.to_date >= date 
f2_2 = dept_emp.to_date.isnull() 
f2 = f2_2 | f2_1 
f3 = f2 == f1

#Se le pide al DataFrame los índices que corresponden al filtro y se cuentan los datos 
p5v1 = dept_emp[f3].emp_no.count() 
print('\n Pregunta 5 versión 1:') 
print('Actualmente la empresa tiene '+str(p5v1)+' empleados') 

#Se le aplica la función .where() al DataFrame y se cuentan los datos  
f5 = dept_emp.where(f3) 
p5v2 = f5.emp_no.count() 
print('\n Pregunta 5 versión 2:') 
print('Actualmente la empresa tiene '+str(p5v2)+' empleados') 

#6  Obtenga la distribución actual de las edades. 
#Se le añade una serie (columna) a solo los datos filtrados del DataFrame de empleados.
#En esta serie se calcula la edad del empleado en la fecha dada 
emp['actual_age']=((date - emp.birth_date)/np.timedelta64(1,'Y')).astype(np.int64)[f3] 
emp.head()
#Se juntan los DataFrames dept_emp y dept con la ayuda de pd.merge() a partir de su clave única 
m1 = pd.merge(dept_emp, dept, on='dept_no', how = 'left') 

#Este DataFrame generado se junta con emp con solo los datos de los empleados actuales 
f8 = pd.merge(m1, emp, on = 'emp_no')[f3] 
#Se cuentan y agrupan las edades actuales 
p6 = f8.groupby(['actual_age']).actual_age.count() 
print('\n Pregunta 6:') 
print('La distribución actual de las edades: \n'+str(p6)) 


#7  ¿Cuál es el departamento con más empleados? 
#Se cuentan y ordenan de mayor a menor a los empleados y se ordenan por número de
#departamento pidiendo la información del primer dato para después ver en dept cómo se #llama este departamento 
f6 = f5.groupby(['dept_no']).emp_no.count().sort_values(ascending=False)[:1].index[0] 
f7 = dept.where(dept.dept_no == f6) 
p7 = f7.dept_name.sort_values(ascending=False)[:1].values[0] 
print('\n Pregunta 7: ') 
print(p7+' es el departamento con más empleados') 


#8 Obtenga la distribución actual de hombres y mujeres por departamento. 
#Se cuenta el genero de los empleados que trabajan en ese momento y se agrupan por departamento 
p8 = f8.groupby(['dept_name', 'gender']).gender.count() 
print('\n Pregunta 8:') 
print('La distribución actual de hombres y mujeres por departamento es: \n'+ str(p8)) 


#9  Obtenga el importe del total del sueldo anual (el que aparece en los datos es sueldo anual) y sueldo promedio por departamento clasificado por género. 
#Se filtran los salarios actuales 
f9_1 = salaries.from_date < date 
f9_21 = salaries.to_date >= date 
f9_22 = salaries.to_date.isnull() 
f9_2 = f9_21 | f9_22 
f9_3 = f9_2 == f9_1 
f9 = salaries[f9_3] 
#Se juntas los Dataframes de los salarios actuales con la información de los empleados y su #departamento, en este nuevo DataFrame se calcula la suma de los salarios y su promedio #y se concatenan los resultados 
m3 = pd.merge(f9, f8, on = 'emp_no', suffixes = ('_dep', '_salaries')) 
p9_1 = m3.groupby(['dept_name', 'gender']).salary.sum() 
p9_2 = m3.groupby(['dept_name', 'gender']).salary.mean() 
p9 = pd.concat([p9_1, p9_2], axis = 1) 
print('\n Pregunta 9:') 
print('El importe es: \n' + str(p9)) 
 
#10 Obtenga el sueldo promedio por puesto (“title”). Obtenga el sueldo promedio por puesto (“title”). 
#Se juntan los títulos y los salarios por el número de empleado y se calcula el sueldo #promedio por puesto 
m4 = pd.merge(titles, salaries, on = 'emp_no', suffixes = ('_titles', '_salaries')) 
p10 = m4.groupby(['title']).salary.mean() 
print('\n Pregunta 10:') 
print('El sueldo promedio por puesto es : \n'+str(p10)) 

#11 Verifique si actualmente todo “manager” de un departamento es empleado de ese departamento. 
#Se filtran a los "managers" actuales, se buscan en la tabla dept_emp y se verifica que los 
#"managers" actuales estén como empleados actuales 
f11_11 = dept_manager.to_date.isnull() 
f11_1 = dept_manager[f11_11] 
m5 = f5[f5.emp_no.isin(f11_1.emp_no)] 
f12 = m5.emp_no.values == f11_1.emp_no.values 
f13 = m5.dept_no.values == f11_1.dept_no.values 
p11 = (False in f12) and (False in f13) 
print('\n Pregunta 11: ') 
if(not p11): 
    print('Actualmente todo “manager” de un departamento es empleado de ese departamento') 
else: 
    print('Actualmente no todo “manager” de un departamento es empleado de ese departamento') 



