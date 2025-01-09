

planeta = {
    'Nombre':'Tierra',
    'Gravedad': '1g',
    'Galaxia': 'Sistema Solar',
    'Tipo orbita': 'Elipsoide'
}

print("")
print("Diccionario original")
print(planeta)

print("")
print("Agregar un nuevo par clave-valor")
planeta['Nucleo']= 'Caliente'
planeta['Atmosfera'] = True
print(planeta)

print("")
print("Cambiar el valor de la clave 'Atmosfera' ")
planeta['Atmosfera']=False
print(planeta)

print("")
print("Eliminar el par clave-valor 'Atmosfera' usando 'del' ")
del planeta['Atmosfera']
print(planeta)
print("")

print("")
print("Eliminar el par clave-valor 'Nucleo' usando el metódo 'pop' ")
nucleo = planeta.pop('Nucleo')
print(planeta)
print()