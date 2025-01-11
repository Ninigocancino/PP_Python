
animales = {
    'Perro' : {'Habitad': 'Domestico', 'Genero': 'Canino', 'Tipo' : 'Terrestre', 'Social' : True },
    'Gato' : {'Habitad' : 'Domestico', 'Genero': 'Felino', 'Tipo': 'Terrestre', 'Social': False},
    'Coyote' : {'Habitad': 'Salvaje', 'Genero': 'Canino', 'Tipo': 'Terrestre', 'Social': False}
}

print("")
print("Diccionario: ")
print(animales)

print("")
print("Imprimir primer nivel del diccionario: ")
gato = animales['Gato']
print(gato)
gato = animales['Gato']['Genero']
print("Imprimir el segundo nivel del dicionario")
print(gato)

print("")