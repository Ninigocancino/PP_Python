"""
Nombre del ejercicio: Iterar elementos de una matriz numérica

Instrucciones: 
1.- Crea una matriz de elementos numericos desde una lista de lista 
2.- Usa un ciclo for para recorrer cada elemento
3.- Imprime cada fila de la matriz

"""

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=",")
    print("")

print("")