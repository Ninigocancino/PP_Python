"""
Nombre del ejercicio: Valor de Y

En funciones anidadas (funciones dentro de funciones), las variables de la función externa no son locales, pero tampoco globales. Estas variables se encuentran en el scope nonlocal, y se pueden modificar usando la palabra clave nonlocal.

Instrucciones: 
1.- Crea una función
2.- Crea una variable con valor numérico
3.- Crea una función dentro de la función creada anteriormente (función anidada)
4.- Dentro de la función interna referencia el valor de la variable creada en la función principal usando 'nonlocal' 
5.- Modifica el valor de la variable desués de ser refernciada
6.- Imprime un mensaje que contenga el valor de la variable ya referenciada
7.- Dentro de la función principal llama la funcion interna
8.- Dentro de la función principal imprime un mensaje que incluya el valor de la variable creada en la función principal
9.- Fuera de la función principal llama a la función función principal
"""

def funcion_externa():
    x = 5  # Variable local de 'funcion_externa'

    def funcion_interna():
        nonlocal x  # Usamos la variable de la función externa
        x = 10
        print(f"Valor de 'x' dentro de funcion_interna: {x}")

    funcion_interna()
    print(f"Valor de 'x' después de llamar a funcion_interna: {x}")

funcion_externa()