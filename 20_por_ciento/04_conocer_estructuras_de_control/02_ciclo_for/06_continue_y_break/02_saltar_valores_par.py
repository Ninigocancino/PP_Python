"""
Nombre del ejercicio: Saltar los valores par de una secuencia numérica

Instrucciones: 
1.- Crea una secuencia del 1 al 20
2.- Has que el programa identifique los números que sean par y los salte
3.- Imprime el resto de los números

"""

for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i)