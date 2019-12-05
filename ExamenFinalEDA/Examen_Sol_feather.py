# Estructuras de Datos Avanzadas
#
# Pre examen sobre pandas y visualización
# Temática: Employees
#
# Paso 0) Definición de la variable con la trayectoria para los archivos y programas
#

#trayDatBin = "D:/user/A_A_MD/Employees/EjercicioPandas/EmployeesBin352/"
#trayProgs  = "D:/user/A_A_MD/Employees/EjercicioPandas/"

# Se leen los datos en binario de las tablas del conjunto "Employees"
#
#Se importan las librerías pandas, numpy, pickle y pyplot
import feather as fea
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Se pide a pandas que los datos de tipo float con solo dos digitos después del punto decimal
pd.options.display.float_format = '{:,.2f}'.format

trayf="D:/user/A_A_MD/Employees/EjercicioPandas/EmployeesFeather/"

#Se cargan las variables con ayuda de open() y pickle.load()
emp = fea.read_dataframe(trayf + "emp.feather")
print("Leido el archivo Employees.dat en el dataframe emp")

dept = fea.read_dataframe(trayf + "dept.feather")
print("Leido el archivo Departments.dat en el dataframe dept")

dept_emp = fea.read_dataframe(trayf + "dept_emp.feather")
print("Leido el archivo Dept_emp.dat en el dataframe dept_emp")

dept_manager = fea.read_dataframe(trayf + "dept_manager.feather")
print("Leido el archivo Dept_manager.dat en el dataframe dept_manager")

salaries = fea.read_dataframe(trayf + "salaries.feather")
print("Leido el archivo Salaries.dat en el dataframe salaries")

titles = fea.read_dataframe(trayf + "titles.feather")
print("Leido el archivo Titles.dat en el dataframe titles")

#======================================Preguntas=================================================

#######
####### Ejercicio 1) Obtener el histograma del numero de registros de sueldo de
####### los empleados y el número de empleados con 1,2,3,4,... registros de sueldo
#######
######
####### Primeramente obtenemos la cantidad de registros por empleado en la tabla salaries
######
#######s_ejer_1 = salaries.groupby(['emp_no']).from_date.count()
######
#######
####### Obtenemos el histograma y lo graficamos
#######
######
######fig_1 = plt.figure()
######gr1 = fig_1.add_subplot(1,1,1)
######gr1.hist(s_ejer_1,bins=list(range(1,20)),align='left')
######gr1.legend(loc='best')
######fig_1.suptitle('Número de Empleados por número de registros de sueldo',fontsize=16)
######fig_1.show()
######
#######
####### ...y obtenemos los datos numéricos...
#######
######c1_min = s_ejer_1.min()
######c1_max = s_ejer_1.max()
######w_1 = [[x,list(s_ejer_1).count(x)] for x in set(list(range(c1_min,c1_max+1)))]
######
#######print(w_1)
######for x in list(range(0,len(w_1))):
######    print("hay "  + str(w_1[x][1]) + " empleados con " + str(w_1[x][0]) + " registros de sueldo")
######
####### Ejercicio 2) Obtener la gráfica de los sueldos obtenidos por un empleado con al menos 10 registros de sueldo 
#######
####### Obtenemos el primer (y segundo) empleados con las características solicitadas
#######
######
######emp_no_20 = s_ejer_1[s_ejer_1>=10].index[0]
######s20       = salaries[salaries.emp_no==emp_no_20]
######
######emp_no_21 = s_ejer_1[s_ejer_1>=10].index[1]
######s21       = salaries[salaries.emp_no==emp_no_21]
######
#######
####### Lo graficamos
#######
######
######fig_2 = plt.figure()
######gr2 = fig_2.add_subplot(1,1,1)
######gr2.plot(s20.from_date,s20.salary,'bo',label="empleado no. " + str(emp_no_20))
######gr2.plot(s21.from_date,s21.salary,'ro',label="empleado no. " + str(emp_no_21))
######gr2.legend(loc='best')
######fig_2.suptitle('Ejemplo de gráfico de la evolución de los sueldos de dos empleados',fontsize=16)
######fig_2.show()
#
# ---------------- Soluciones al examen final -------------------------
#
#   Ejericio 1) cantidad de empledos que estén o hayan estado en cada uno de los depatamentos
#
# va por la económica:
#
empPorDept = dept_emp.groupby('dept_no').emp_no.count()

print('Empleados por clave de departamento:\n' + str(empPorDept))

#
# !!!El Dataframe plot.bar no funciona en el idle!!!
#
##fig_exf1 = plt.figure()
##grexf1 = fig_exf1.add_subplot(1,1,1)
##grexf1 = pd.DataFrame({'depto': empPorDept.index.values,'cuantos':empPorDept.values}).plot.bar(x='depto',y='cuantos',rot=0)
##grexf1.legend(loc='best')
##fig_exf1.suptitle('Empleados por clave de depto',fontsize=16)
##fig_exf1.show()
#
# Eliminar la gráfica una vez desplegada:

##pd.DataFrame({'depto': empPorDept.index.values,'cuantos':empPorDept.values}).plot.bar(x='depto',y='cuantos',rot=0)
##plt.show()

#
# Forzado a mano
#
##fig_exf1 = plt.figure()
##grexf1 = fig_exf1.add_subplot(1,1,1)
##x=tuple(range(0,empPorDept.size))
##grexf1 = plt.bar(left=x,height=empPorDept.values,align = 'center')
##plt.xticks(x,tuple(empPorDept.index.values))
###grexf1.plot.xticks(x,tuple(empPorDept.index.values))
##fig_exf1.suptitle('Empleados por clave de depto',fontsize=16)
##fig_exf1.show()

#
# con el kind el df.plot lo forza
#
fig_exf1 = plt.figure()
grexf1 = fig_exf1.add_subplot(1,1,1)
empPorDept.plot(kind='bar')
fig_exf1.suptitle('Empleados por clave de depto',fontsize=16)
fig_exf1.show()

#
# Ejercicio 2) Registros de salario de 5 empleados que hayan iniciado en un departamento y tengan al menos 10 registros de salario
#
#
# Obtengamos los empleados que inician en el depto_no == 'd001'
#
emps_inic_d001 = dept_emp[dept_emp['dept_no']=='d001'].merge(emp,left_on=['emp_no','from_date'],right_on=['emp_no','hire_date'])
#
# y obtengamos la cantidad de registros de sueldo que tiene cada uno de ellos
#
regs_por_empleado = salaries.merge(pd.DataFrame(emps_inic_d001.emp_no),left_on=['emp_no'],right_on=['emp_no'])
#
# y los cuento
#
cant_regs_por_empleado = regs_por_empleado.groupby(by=['emp_no']).emp_no.count()
#
# y los que me interesan
#
arr_emp_interes = cant_regs_por_empleado[cant_regs_por_empleado >= 10].index.values
#
#
#
fig_3 = plt.figure()
gr3   = fig_3.add_subplot(1,1,1)

se=[]
for k in list(range(0,5)):
    se.append( salaries[salaries.emp_no==arr_emp_interes[k]])
    gr3.plot(se[k].from_date,se[k].salary,'o',label='emp_no:' + str(arr_emp_interes[k]))
    print(se[k])
fig_3.suptitle('Evolución de sueldos de (algunos) empledos \n que iniciaron en el depto ' + dept[dept.dept_no=='d001'].dept_name[::][0], fontsize=16)
gr3.legend(loc='best')
fig_3.show()


