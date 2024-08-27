"""
Nombre del ejercicio: Saltar valores de una secuencia numérica

Instrucciones: 
1.- Salta dos valores de una secuencia del 1 al 20
2.- Imprime el resto de los números

"""

for i in range(1,21):
    if i == 10 or i == 15:
        continue
    print(i)