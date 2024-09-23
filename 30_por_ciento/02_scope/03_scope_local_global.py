"""
Nombre del ejercicio: Adivina del valor de X

En este ejercicio vas a trabajar con variables locales y globales. Intenta predecir qué imprimirá el código antes de ejecutarlo.

Instrucciones: 
1.- Crea una variable con un valor numérico
2.- Crea dos funciones
3.- En la primer función agrega una variable llamada igual que la variables creada fuera de la función, agrega un valor diferente y agrega la impresión de un mensaje que conteenga el valor de la variable
4.- En la segunda función usa global para referenciar la variable global 
5.- Modifica el valor de la variable después de referenciarla con global
6.- Imprime un mensaje que contenga el valor de la cariable
7.- Llama la funcion 1
8.- Imprime un mensaje que incluya el valor de la variable después de la ejecución de la función 1
9.- Llama la función 2
10.- Imprime un mensaje que incluya el valor de la variable después de la ejecución de la función 2
"""

x = 50  # Variable global

print("")
print(f"Valor de X antes de ejecutar las funciones es {x}")
print("")

def funcion1():
    x = 20  # Variable local
    print(f"Valor de 'x' dentro de funcion1: {x}")

def funcion2():
    global x
    x = 100  # Modifica la variable global
    print(f"Valor de 'x' dentro de funcion2: {x}")

print("")

funcion1()
print(f"Valor de 'x' después de llamar a funcion1: {x}")

funcion2()
print(f"Valor de 'x' después de llamar a funcion2: {x}")

print("")