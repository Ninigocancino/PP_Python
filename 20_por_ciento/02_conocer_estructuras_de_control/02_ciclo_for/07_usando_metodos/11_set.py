"""
Nombre del ejercicio: Elimina elementos duplicados

Instrucciones: 
1.- Crea una lista de números
2.- Recorre los elementos de la lista
3.- Usa el método set para eliminar de la lista los elementos repetidos
7:- Imprime los elementos números de forma vertical

"""

numeros = [1,2,2,3,4,5,6,7,2,5,5,9,3]

for i in set(numeros):
    print(i)
