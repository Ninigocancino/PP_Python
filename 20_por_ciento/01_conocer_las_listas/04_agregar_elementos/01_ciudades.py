
"""
Instrucciones: crea una lista con 7 ciudades mexicanas y luego agrega 3 nuevos elementos. Intenta agregar directamente nuevos elementos a la lista y luego intenta concatenando listas o viceversa. Imprime cauda una de las listas
"""

ciudades_mexicanas = ['Monterrey','Villehermosa','Oaxaca','La Paz','Méxio','Cancún','Palenque']

nuevas_ciudades = ['Puerto vallarta', 'Merida','Toluca']

ciudades_union = ciudades_mexicanas + nuevas_ciudades

ciudad_agregada = 'San Luis Potosí'
ciudades_mexicanas = ciudades_mexicanas + [ciudad_agregada] + ['Queretaro']

print()
print("lista original:")
print(ciudades_mexicanas)
print("")
print("Lista con agregación de elementos concatenando listas: ")
print(ciudades_union)
print()
print("Sumando  elementos a la lista")
print(ciudades_mexicanas)
print()