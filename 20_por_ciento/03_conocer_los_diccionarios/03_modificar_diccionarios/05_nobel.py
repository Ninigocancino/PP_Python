
ganadores_2024 = {
    'Literatura': 'Han Kang',
    'Fisica' : 'Geoffri Hinton, John Holpfield',
    'Medicina': 'Victor Ambros, Garu Ruvkun',
    'Economía': 'James A. Robinson, Simon Johnson, Daron Acemoglu',
    'Paz' : 'Nihon Hidankyo',
    'Quimica': 'Demis Hassabis, David Baker, John Jumper'
}

print("")
print("Diccionario original")
print(ganadores_2024)
print("")

print("")
print("Agregar un nuevo par clave-valor")
ganadores_2024['Matematicas']="Desconocido"
print(ganadores_2024)

print("")
print("Cambiar el valor de la clave 'Matematicas' ")
ganadores_2024['Matematicas']="No se entregan premios Nobel en Matématicas"
print(ganadores_2024)

ganadores_2024['Pintura']="No se entregan premios Nobel en Pintura"

print("")
print("Eliminar un par clave-valor usando del")
del ganadores_2024['Matematicas']
print(ganadores_2024)

print("")
print("Eliminar un par clave-valor usando el método pop")
pintura = ganadores_2024.pop('Pintura')
print(ganadores_2024)

print()


