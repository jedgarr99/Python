# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:19:47 2019

@author: dai
"""

from bd import conexion

try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO peliculas(titulo, year) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, ("Volver al futuro 1", 1985))
        cursor.execute(consulta, ("Pulp Fiction", 1994))
        cursor.execute(consulta, ("It", 2017))
        cursor.execute(consulta, ("Ready Player One", 2018))
        cursor.execute(consulta, ("Spider-Man: un nuevo universo", 2018))
        cursor.execute(consulta, ("Avengers: Endgame", 2019))
        cursor.execute(consulta, ("John Wick 3: Parabellum", 2019))
        cursor.execute(consulta, ("Toy Story 4", 2019))
        cursor.execute(consulta, ("It 2", 2019))
        cursor.execute(consulta, ("Spider-Man: lejos de casa", 2019))

except Exception as e:
    print("Ocurrió un error al insertar: ", e)
#finally:
 #   conexion.close() 
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO cines(nombre, direc) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, ("cinemex polanco", "polanco"))
        cursor.execute(consulta, ("cinemex loreto", "loreto"))
        cursor.execute(consulta, ("cinepolis san angel", "san angel"))
        cursor.execute(consulta, ("cinepolis pedregal", "pedregal"))
        
except Exception as e:
    print("Ocurrió un error al insertar: ", e)
#finally:
 #   conexion.close()
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO pelicula_cines(idPel, idCine) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (1,1))
        cursor.execute(consulta, (2,2))
        cursor.execute(consulta, (3,3))
        cursor.execute(consulta, (4,4))
        cursor.execute(consulta, (5,4))
        cursor.execute(consulta, (6,3))
        cursor.execute(consulta, (7,2))
        cursor.execute(consulta, (8,1))
        cursor.execute(consulta, (9,1))
        cursor.execute(consulta, (10,1))
        
except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()

#CRUD
#Read
#seleccionar toda la información de la tabla películas
try:
    with conexion.cursor() as cursor:
        cursor.execute("select idPel, titulo, year from peliculas")
        peliculas = cursor.fetchall()
        for pelicula in peliculas:
            print(pelicula)
except Exception as e:
    print("Ocurrió un error al consultar peliculas: ", e)
finally:
    conexion.close
    
#uso where
#seleccionar todas las películas donde el año sea mayor a 2000
try:
    with conexion.cursor() as cursor:
        consulta = "select idPel, titulo, year from peliculas where year>?"
        cursor.execute(consulta,(2000))
        peliculas = cursor.fetchall()
        for pelicula in peliculas:
            print(pelicula)
except Exception as e:
    print("Ocurrió un error al consultar peliculas: ", e)
finally:
    conexion.close    
    
#where y like
#seleccionar todas las películas que tengan en el nombre las letras endg    
 try:
    with conexion.cursor() as cursor:
        consulta = "select idPel, titulo, year from peliculas where titulo like ?"
        palabra = "endg"
        cursor.execute(consulta,("%"+palabra+"%"))
        peliculas = cursor.fetchall()
        for pelicula in peliculas:
            print(pelicula)
except Exception as e:
    print("Ocurrió un error al consultar peliculas: ", e)
finally:
    conexion.close      
    
#uso del order by
#seleccionar toda la informacion del cine ordenado por precio de manera descendiente
try:
    with conexion.cursor() as cursor:
        cursor.execute("select * from cines order by precio desc")
        cines = cursor. fetchall()
        for c in cines:
            print(c)
except Exception as e:
    print("Ocurrió un error al consultar cines: ", e)
finally:
    conexion.close   
    
#where in
#seleccionar toda la informacion del cine que tenga como direccion polanco y pedregal    
try:
    with conexion.cursor() as cursor:
        consulta = "select * from cines where direc in (?,?)"
        cursor.execute(consulta,("polanco", "pedregal"))
        cines = cursor.fetchall()
        for c in cines:
            print(c)
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close       
    
#CRUD
#update
try:
    with conexion.cursor() as cursor:
        consulta = "update peliculas set titulo = ? where idPel= ?"
        nuevoTitulo = "diego va al banco"
        idR = 2
        cursor.execute(consulta,(nuevoTitulo, idR))
        conexion.commit()
        
except Exception as e:
    print("Ocurrió un error al update: ", e)
finally:
    conexion.close   
    
#DELETE
try:
    with conexion.cursor() as cursor:
        consulta = "delete from pelicula_cines where idCine =?"
        idC = 2
        cursor.execute(consulta,(idC))
        #el commit es para que se realicen los cambios en la BD
        conexion.commit()
except Exception as e:
    print("Ocurrió un error al delete: ", e)
finally:
    conexion.close     
    
    