
libros = {
    'Hyperfocus' : {'Autor': 'Chris Bailey', 'Anio': 2018, 'Formato': 'Físico'},
    'Originals' : {'Autor': 'Adam Grant', 'Anio': 2014, 'Formato': 'Físico'},
    'Sapiens' : {'Autor': 'Yuval Noah Harari', 'Anio': 2012, 'Formato':'Físico'}
}

print()
print("Diccionario completo")
print(libros)
print()

print('Primer nivel de la Clave Originals')
originals = libros['Originals']
print(originals)
print("Según do nivel de la clave Originals")
originals = libros['Originals']['Autor']
print(originals)
print()
