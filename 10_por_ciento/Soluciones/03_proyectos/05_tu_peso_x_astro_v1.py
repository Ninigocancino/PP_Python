"""
INFORMACIÓN DEL PROYECTO:

Nombre del Proyecto: Tu peso en un astro

Descripción:
Progamaremos un juego que permita calcular el peso de una persona en la luna 


Instrucciones:
Se requiere que el proyecto se aborde por bloques de funcionalidades para poder detectar errores e incorporar mejoras de forma más ágil y esbelta.

Caso de uso:
Se requiere desarrollar un juego para una clase escolar donde los alumnos tengan un primer acercamiento al tema de la gravedad y como afecta esta el peso de los objetos en diferentes cuerpos celestes. En este caso se pretende que el programa ayude a los alumnos conocer la diferencia entre su peso en la tierra y su peso hipotetico en la luna. 

Historia de usuario:
Cómo profesor de la clase requiero un programa que permita a mis alumnos ingresar el peso de un objeto en la tierra para conocer el precio estimado del mismo objeto si estuviera en la luna, además de que proporcione información de como se realizó el calculo. 


Criterios de calidad:
Crear un programa sencillo que realice las siguientes acciones: 
1.- El programa debe imprimir un mensaje de bienvenida
2.- El programa debe debe imprimir una descripción del programa
3.- El programa debe debe imprimir al menos dos de las instrucciones del programa
4.- Los textos deben mostrarse de forma amigable para facilitar al usuario su lectura 
5.- El programa debe mostrar al usuario un ejemplo sencillo de la utilidad que tendrá el programa, mostrando la conversión del peso del objeto en la tierra al peso estimado del mismo objeto pero en la luna.
6.- El programa debe mostrar la explicación de la operación
7.- El programa debe mostrar un mensaje de despedida antes de cerrarse
"""

print("")
print("Bienvenido a Laika")
print("Calcula el peso que un objeto de la tierra tendría en la luna")
print("")

print("Instrucciones:")
print("01) Ingresa una cifra que represente peso en kg")
print("02) Da enter para realizar el calculo")

peso_tierra = float(input("Ingresa un peso que represente kg: "))

# formula: peso en la tierra * gravedad en la luna / gravedad en la 

g_luna = 0.34
g_tierra = 1

resultado = peso_tierra * g_luna / g_tierra

print("")
print(f"Tu objeto pesa: {peso_tierra} kg en la tierra, pero en la luna pesa:{resultado} kg")
print("")

print("¿Quieres saber como llegamos al resultado? mira:")

print("")
print("Para realizar conocer el peso del objeto en la luna:")
print("1) Debemos conocer el valor la gravedad en la tierra y en la luna")
print(f"La gravedad en la tierra es igual a {g_tierra}")
print(f"La gravedad en la luna es igual a {g_luna}")
print("")
print(f"2) Debemos conocer el peso del objeto en la tierra, en este caso {peso_tierra} kg")
print("")
print("3) Multiplicar el peso del objeto en la tierra por la gravedad de la tierra")
print("")
print("4) dividimos el resultado de la multiplicación entre la gravedad de la luna")
print("")
print("Formula:")
print(" R = p*t/l")
print("Donde: ")
print("R es el reulstado de la conversión")
print("p es el peso del objeto expresado en kilogramos")
print("t es la gravedad de la tierra")
print("l es la gravedad de la luna")
print("")
print("Sustitución: ")
print(f"R = {peso_tierra} * {g_tierra} / {g_luna}")
print("")

print("Espero hayas aprendido algo nuevo sobre el universo hoy")
print("Nos vemos pronto")