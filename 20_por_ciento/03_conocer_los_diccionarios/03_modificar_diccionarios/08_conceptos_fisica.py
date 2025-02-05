

conceptos_fisica = {
    'Fuerza' : "La fuerza es cualquier interacción que causa que un objeto cambie su estado de movimiento, ya sea que se acelere, desacelere o cambie de dirección. Es una magnitud vectorial, lo que significa que tiene tanto magnitud como dirección.",
    'Energia' : "La energía es la capacidad de realizar trabajo. Se presenta en diversas formas, como la energía cinética (movimiento), potencial (posición), térmica (calor), eléctrica, etc. La ley de conservación de la energía establece que la energía no se crea ni se destruye, solo se transforma de una forma a otra. ",
    'Materia' : "La materia es todo aquello que ocupa un lugar en el espacio y tiene masa. Está compuesta por átomos, que a su vez están formados por protones, neutrones y electrones. La materia puede existir en diferentes estados: sólido, líquido, gaseoso y plasma. "
}

print("Agregar un nuevo par clave-valor")
conceptos_fisica['Masa']= ""
print(conceptos_fisica)

print("")
print("Modificar el valor de la clave 'Masa' ")
conceptos_fisica['Masa'] = 'La masa es una medida de la cantidad de materia que contiene un objeto. Es una propiedad intrínseca de la materia y se relaciona con la inercia, es decir, la resistencia de un objeto a cambiar su estado de movimiento.'
print(conceptos_fisica)
print()

conceptos_fisica['Trabajo'] = 'Concepto esencial en física'
print("Nuevo par clave valor")
print(conceptos_fisica['Trabajo'])
print()

print("Eliminar el par calve valor 'Trabajo")
del conceptos_fisica['Trabajo']
print(conceptos_fisica)
print()