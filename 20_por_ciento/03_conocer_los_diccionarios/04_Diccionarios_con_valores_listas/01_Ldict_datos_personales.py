
datos = {
    'nombres' : ['María', 'Ana', 'Luis'],
    'edad' : [20,24,23],
    'ciudad' : ['Dubai','Tokyo','Viena']
}

print("")
print(datos)
print()

print("Acceder a los valores de las claves")
nombres=datos['nombres']
print(nombres)
print(datos['edad'])
ciudad = datos['ciudad']
print(ciudad)
print("")

print("Acceder a valores correspondientes a Ana en el diciconario")
print(datos['nombres'][1])
edad_ana = datos['edad'][1]
print(edad_ana)
print(datos['ciudad'][1])
print("")