"""
Nombre del ejercicio: Consultar lista de nombres

Instrucciones: 
1.- Crea una lista, usa el comando 'Alt + Z' para que el editor te muestre el contenido con salto de línea y escribe dos líneas con nombres de personas.
2.- Imprime el contenido de la lista.
3.- Descurbe cuál es el número total de elementos que contiene la lista
4.- Descubre que nombre se encunetra en la posiciones 10, luego imprime el resultado acompañado de un mensaje descriptivo en el que uses la interpolación 
"""

lista_nombres = ["Ana", "Pedro", "María", "Juan", "Laura", "Diego", "Sofía", "Daniel", "Lucía", "Javier", "Marta", "David", "Sara", "Álvaro", "Paula", "Carlos", "Esther", "Miguel", "Claudia", "Alejandro", "Isabel", "Andrés", "Victoria", "Marcos", "Beatriz", "Óscar", "Inés", "Rodrigo", "Valeria", "Pablo"]



print(f"El contenido de la lista nombres es: {lista_nombres}")
print("")



conteo_nombres = len(lista_nombres)
print(f"El número de elementos en lista nombres es: {conteo_nombres}")



nombres_desconocido_1 = lista_nombres[5]
nombres_desconocido_2 = lista_nombres[2]
nombres_desconocido_3 = lista_nombres[23]
print(f"El nombre en la posición 3 es: {nombres_desconocido_1}, el nombre en la posición 8 es: {nombres_desconocido_2} y el nombre en la posición 15 es: {nombres_desconocido_3}")
print("")

