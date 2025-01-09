

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
