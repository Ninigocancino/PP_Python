
animales = {
    'Reptiles' : ['Boa','Cocodrilo','Tortuga','Lagarto'],
    'Mamiferos' : ['Perro','Gato','Lobo','León'],
    'Anfibios' : ['Rana','Sapo']
}

print("")
print("Diccionario animales")
print(animales)
print("")

print("Acceder a los valores de las claves")
print(animales['Reptiles'])
mamiferos = animales['Mamiferos']
print(mamiferos)
print(animales['Anfibios'])
print("")

print("Acceder a los valores especificos del diccionario 'animales' ")
print(animales['Reptiles'][3])
print(animales['Mamiferos'][0])
anfibios = animales['Anfibios'][0]
print(anfibios)
print("")