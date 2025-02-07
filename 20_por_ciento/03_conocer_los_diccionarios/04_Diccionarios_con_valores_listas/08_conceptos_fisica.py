
conceptos_fisica = {
    'concepto' : ["Fuerza",'Energía','Materia'],
    'definicion' : ['Interacción que causa que un objeto cambie su estado de movimiento','capacidad de realizar trabajo','todo aquello que ocupa un lugar en el espacio y tiene masa']
}

print()
print("Diccionario conceptos de física con listas como valores ")
print(conceptos_fisica)
print()

print("Acceder a los valores de las claves")
print(conceptos_fisica['concepto'])
print(conceptos_fisica['definicion'])
print()

print("Acceder a valores especificos de la clave 'concpeto' ")
print("Valor en el indice 1 de la lista")
print(conceptos_fisica['concepto'][1])
concepto = conceptos_fisica['concepto'][2]
print("Valos en el indice 2 de la lista")
print(concepto)