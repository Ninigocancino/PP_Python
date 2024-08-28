"""
Nombre del ejercicio: ¿Cuántas letras tiene una palabra?

Instrucciones: 
1.- Crea una variable que guarde una palabra determinada
2.- Recorre el elemento
3.- Imprime el elemento y la cuenta de caracteres o letras en el elemento

"""

palabra = "abracadabra"
contador = {}

for i in palabra:
    if i in contador:
        contador[i] += 1
    else:
        contador[i] = 1

for i, cuenta in contador.items():
    print(f"{i}: {cuenta}")