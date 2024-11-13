"""
Nombre del ejercicio: Libros

Instrucciones: 
1.- Reutiliza la lista del ejercicio 'Lista Libros' y amplia su contenido.
2.- Imprime el contenido de la lista.
3.- Descurbe cuál es el número total de elementos que contiene la lista
4.- Descubre que letra se encuentra en las posiciones 1,4 y 3, luego imprime el resultado acompañado de un mensaje descriptivo en el que uses la interpolación 
"""

libros = ["Hyperfocus","Originals", "Repensar la pobreza","Sapeins", "Esencialismo", "Fuera de serie", "El cisne negro", "Small data", "Así se domina el mundo"]

conteo = len(libros)
print(f"La lista contiene {conteo} libros")

posicion1 = libros[1]
posicion4 = libros[4]
posicion3 = libros[3]

print(f"{posicion1} se encuentra en la posición 1, {posicion4} se encuantra en la posición 4 y {posicion3} se encuentra en la posición 3")