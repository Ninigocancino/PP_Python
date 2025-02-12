
conceptos_fisica = [
    {'Concepto': 'fuerza', 'Definición' : "La fuerza es una magnitud física que describe la interacción entre dos objetos, capaz de modificar el estado de movimiento o la forma de un cuerpo.", 'Tipo': 'Elemental'},
    {'Concepto': 'energia', 'Definicion' : 'La energía es la capacidad que tiene la materia para realizar un trabajo, producir cambios o generar movimiento','Tipo': 'Elemental'},
    {'Concepto': 'materia', 'Definicion' : 'todo lo que podemos tocar, ver, sentir o medir', 'Tipo': 'Elemental'},
    {'Concepto':'constante de PLANCK', 'Definicion' : 'es un número fundamental en la física que representa el cuanto elemental de acción. Es decir, es la unidad más pequeña de energía que un sistema puede intercambiar.', 'Tipo': 'Avanzado'}
]

print()
print("Lista de diccionarios 'conceptos_fisica' ")
print(conceptos_fisica)
print()

print("Acceder al primer diciconario de la lista")
primer_diccionario = conceptos_fisica[0]
print(primer_diccionario)
print("")

print("Acceder al valor de la clave 'Tipo' del ultimo diccionario")
clave_tipo = conceptos_fisica[3]['Tipo']
print(clave_tipo)
print(conceptos_fisica[3]['Tipo'])
print()

print("Agregar una nueva clave al diccionario 2")
conceptos_fisica[2]['Nota'] = 'Bien'
nueva_clave = conceptos_fisica[2]
print(nueva_clave)
print()

print("Modificar el valor de la clave 'Nota' en el diccionario 2")
conceptos_fisica[2]['Nota'] = 'Necesita más información'
clave_modificada = conceptos_fisica[2]
print(clave_modificada)
print()