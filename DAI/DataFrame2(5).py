# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:36:32 2019

@author: dai
"""

import pandas as pd
import numpy as np

#CRUD
#crear dataFrame vacío

dfv = pd.DataFrame()
print(dfv)

#crear de una lista

data = [1,2,3,4,5]
dfl = pd.DataFrame(data)
print(dfl)

#crear de varias listas
data = [['ALEX',10], ['BOB', 12], ['PEDRO', 15]]
dfl2 = pd.DataFrame(data, columns = ['Nombre', 'Edad'], dtype = float)
print(dfl2)

print(dfl2.dtypes)

datos = {'Nombre' : ['Diego', 'Sebastian', 'Luisa'], 
         'Calificaciones': ['10', '9', '9',],
         'Deportes:' : ['futbol', 'basquetbol', 'tenis'],
         'Materias': ['DAI', 'AP', 'AP']}
dfd = pd.DataFrame(datos)
print(dfd)

#valores dataframe
print('\n'*2)
print(dfd.values)
print('\n'*2)
print(dfd.columns)
print('\n'*2)
print(dfd.index)

#conocendo dataframe
print(dfd.shape)
print(dfd.dtypes)
print(dfd.info())

#mostrar los datos
print(dfd.head(1))
print(dfd.tail(1))
print(dfd.sample(2))


dfd['Calificaciones']
dfd.Calificaciones
dfd['Calificaciones'] = 9
print(dfd)
dfd['arribaProm'] = dfd['Calificaciones'] >= dfd['Calificaciones'].mean()
print(dfd['arribaProm'])

#manejo de datos como si fuera SQL
url = ('https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv')
tips = pd.read_csv(url)
tips.head()
print(tips.shape)

#Select

#select * from tips LIMIT 5;
tips.head(5)

#select total_bill, tip, smoker, time from tips limit 5;
tips[['total_bill', 'tip','smoker', 'time']].head(5)

#where
#select * from tips where time = 'Dinner' limit 5

tips[tips['time']=='Dinner'].head(5)

#esto mismo pero paso a paso

is_dinner = tips['time'] == ' Dinner'
is_dinner.value_counts()
tips[is_dinner].head(5)

#AND & OR |
#select * from tips where time = 'Dinner' and tip>5.0

tips[(tips['time'] == ' Dinner') & (tips['tip'] > 5.0)]

tips[(tips['size']>= 5) | (tips['total_bill'] >45)]

#usando datos null notna(), isna()



dfn = pd.DataFrame({'col1':['A','B',np.NAN, 'C','D'],
                    'col2':['F',np.NAN,'G', 'H','I']
                    })

print(dfn)

#select * from dfn where col2 is null
dfn[dfn['col2'].isna()]

#select * from dfn where col1 is not null

dfn[dfn['col1'].notna() & dfn['col2'].notna() ]

#group by
#select sex, count(*) from tips grup by sex;
tips.groupby('sex').size()

tips.groupby('sex').count()

tips.groupby('sex')['total_bill'].count()

#select day, avg(tip) from tips group by day

tips.groupby('day').agg({'tip':np.mean, 'day': np.size})

#select smoker, dat, count(*), avg(tip) from tips group by smoker, day

tips.groupby(['smoker', 'day']).agg({'tip':[np.size, np.mean]})

#join

df1 = pd.DataFrame({'key' :['A', 'B', 'C', 'D'],
                    'value': np.random.randn(4)})

df2 = pd.DataFrame({'key' :['E', 'F', 'G', 'H'],
                    'value': np.random.randn(4)})

print(df1)
print('\n')
print(df2)


#select * from dfl inner join df2 on df1.key = df2.key

pd.merge(df1,df2, on = 'key')

#select * from df1 left join df2 on df1.key = df2.key

pd.merge(df1, df2, on ='key', how = 'left')

#select * from df1 right join df2 on df1.key = df2.key

pd.merge(df1, df2, on ='key', how = 'right')

#full join


pd.merge(df1, df2, on ='key', how = 'outer')

#union
pd.concat([df1,df2]).drop_duplicates()





