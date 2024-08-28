"""
Nombre del ejercicio: ¿Cuántas veces se repite una letra en una palabra?

Instrucciones: 
1.- Crea una variable que guarde una palabra determinada
2.- Recorre el elemento
3.- Imprime en verticalmente el caracter  y la cuenta de las vaces que aparece en la palabra

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