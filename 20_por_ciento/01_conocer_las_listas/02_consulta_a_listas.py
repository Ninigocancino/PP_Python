#Listas a trabajar en el fichero:

lista_ciudades = ['México','Lisboa','San Fracisco','Monterrey','Bogota','Madrid','Barcelona','París','Berlin','Pekin','Manila','Alejandría', 'Caracas','Toronto','Buenos Aires', 'Montevideo','Cancún','Ciudad del Cabo','Londres','Río de Janeiro','Tokio','Monaco','Playa del Carmen']

lista_frutas = ['Guanabana','Manzana','Pera','Cereza','Fresa','Uva','Melon','Sandía','Coco','Mango','Pitahaya','Tuna','Tomate','Aguacate','Guayaba','Piña','Papaya','Zapote']

lista_nombres = ['German','Juan','Francisco','Iker','Laura','Maria','Mary','Lucio','Cuahutemoc','Xochitl','Marina','Kate','Lucrecia', 'Malinalli','Saul', 'Levi', 'Domingo', 'Dominic', 'John', 'Joe', 'Luca']

#EJERCICIOS

#Ejercicio 01: Muestra en consola el contenido de las listas

print(f"El contenido de la lista ciudades es: {lista_ciudades}")
print("")
print(f"El contenido de la lista frutas es: {lista_frutas}")
print("")
print(f"El contenido de la lista nombres es: {lista_nombres}")
print("")
#Ejercicio 01: De la lista 'frutas' descubre cual es la fruta que esta en la posición 10 e impremelo con un mensaje descriptivo usando interpolación 

ciudad_desconocida = lista_ciudades[10]
print(f"La ciudad desconocida es {ciudad_desconocida}")
print("")

#Ejercicio 02: De la lista 'nombres' descubre que nombres se encunetran en las posiciones 3,8 y 15, luego imprime el resultado acompañado de un mensaje descriptivo en el que uses la interpolación 

nombres_desconocido_1 = lista_nombres[3]
nombres_desconocido_2 = lista_nombres[8]
nombres_desconocido_3 = lista_nombres[15]
print(f"El nombre en la posición 3 es: {nombres_desconocido_1}, el nombre en la posición 8 es: {nombres_desconocido_2} y el nombre en la posición 15 es: {nombres_desconocido_3}")
print("")

#Ejercicio 03: De la lista 'ciudades' descurbe cuál es el número total de elementos que contiene

conteo_ciudades = len(lista_ciudades)
print(f"El número de elementos en lista ciudades es: {conteo_ciudades}")