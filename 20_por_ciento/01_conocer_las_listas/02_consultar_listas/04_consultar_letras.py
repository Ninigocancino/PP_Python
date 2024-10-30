"""
Nombre del ejercicio: Letras de nombre

Instrucciones: 
1.- Reutiliza la lista del ejercicio 'Lista deletreo'.
2.- Imprime el contenido de la lista.
3.- Descurbe cuál es el número total de elementos que contiene la lista
4.- Descubre que letra se encunetra en las posiciones 3,5 y 2, luego imprime el resultado acompañado de un mensaje descriptivo en el que uses la interpolación 
"""

palabra = ["A", "L", "L", "A", "N", " ", "T", "U", "R", "I", "N", "G"]

print(palabra)

contar_l = len(palabra)

posicion_a = palabra[3]
posicion_b = palabra[5]
posicion_c = palabra[2]

print(f"En el nombre ALLAN TURING la letra en la posición 3 es la '{posicion_a}', la letra en la posición 5 es la letra '{posicion_b}' y la letra en la posición 2 es la letra '{posicion_c}'")
