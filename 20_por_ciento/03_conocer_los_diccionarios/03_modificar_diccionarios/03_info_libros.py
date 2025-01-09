
libros_info = {
    'Titulo': 'Sapiens, De animales a dioses',
    'Autor': 'Yuval Noah Harari',
    'Año': '2016',
    'N_paginas': 450,
    'Edición': '1era edición',
    'Genero':'Pensamiento, filosofía',
    'Precio': '$650 mxn'
}

print("")
print("Diccionario original")
print(libros_info)
print("")

print("")
print("Modificar el valor de la clave 'N_paginas' ")
libros_info['N_paginas'] = 600
print(libros_info)

print("")
print("Agregar un nuevo par clave valor al diccionario")
libros_info['Calificacion'] = '5/5'
print(libros_info)
