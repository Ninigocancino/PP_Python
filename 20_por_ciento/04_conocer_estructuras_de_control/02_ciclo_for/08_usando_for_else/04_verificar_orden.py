"""
Nombre del ejercicio: Verificar si la lista esta en orden de menor a mayor

Instrucciones: 
1.- Crea una lista de números
2.- Recorre los elementos de la lista
3:- Comprueba si el número anterior en cada iteración es menor que el siguiente
5.- Si los numeros cumplen la condición imprime 'Estan ordenados'
6.- Si los números no están ordenados imprime 'No están ordenados' 

"""

ln = [1,2,3,4,5]

for i in range(len(ln) -1):
    if ln[i] > ln[i+1]:
        print("La lista no está ordenada")
        break
else:
    print("La lista está ordenada")