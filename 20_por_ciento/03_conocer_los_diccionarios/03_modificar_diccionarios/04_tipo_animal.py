
tipo_animal = {
    'Pato': 'Acuatico, Terrestre, Volador',
    'Perro' : 'Terrestre',
    'Trucha': 'Acuatico',
    'Murcielago': 'Volador'
}

print("")
print("Diccionario original")
print(tipo_animal)
print("")

print("Agregar un nuevo par clave-valor")
tipo_animal['Delfin']= 'Acuatico'
print(tipo_animal)

print("")
print("Modificar el valor de la clave 'Delfin' ")
tipo_animal['Delfin']= 'Acuatico-marino'
tipo_animal['Terodactilo'] = 'Volador-dinosaurio'
print(tipo_animal)


print("")
print()