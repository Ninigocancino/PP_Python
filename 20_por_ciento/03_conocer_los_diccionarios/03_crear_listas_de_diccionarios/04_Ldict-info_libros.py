
#Manejar el diciconario Libros usando listas como valores de las claves

libros = {
    'titulos' : ['Sapiens','Hyperfocus','Así se domina el mundo'],
    'autores' : ['Yuval Noha Harari','Chris Bailey', 'Pedro Baños'],
    'tema': ['Filosfía','Productividad','Geopolitica']
}

print()
print("Diciconario: libros")
print(libros)
print()

print("Acceder a los valores de las claves")
titulos = libros['titulos']
print(titulos)
print(libros['autores'])
print("")

print("Acceder a los valores asociados al titulo 'Hyperfocus' ")
print(libros['titulos'][1])
autores = libros['autores'][1]
print(autores)
print(libros['tema'][1])
print()