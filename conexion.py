

import mysql.connector
conexion = mysql.connector.connect(
    user='root', password='Jj73576237',
    host='localhost',
    database='cursodb',
    port='3306'
    )


print('Mi primera conexión de base de datos:  ', conexion)
print('     ')
print('     ')
print('ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')

visual=conexion.cursor()
visual.execute("select Nombre,Direccion from alumnos")
for Nombre, Direccion in visual.fetchall():
    print (Nombre, "  |   ",Direccion)
print('     ')
print('     ')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ')
visu=conexion.cursor()
visu.execute("select Nombres,Generos from basicos")
for Nombres, Generos in visu.fetchall():
    print (Nombres, "  |   ",Generos)
print('     ')
print('     ')
print('***************************************************************************************************  ')

conexion.close

