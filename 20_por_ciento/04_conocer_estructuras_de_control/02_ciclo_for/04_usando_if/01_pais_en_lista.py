"""
Nombre del ejercicio: Encuentra el país

Instrucciones: 
1.- Crea una lista de paises 
2.- Usa un ciclo for para recorrer los elementos y buscar el valor 'México' en la lista
3.- Si el valor existe imprime una confirmación de existencia
4.- Si no es el valor imprime un mensaje que indique cuál es el valor por el que esta pasando el ciclo

"""

paises = ['México','Sudafrica','Canada','Colombia','Cuba']

for i in paises:
    if i == "México":
        print(f"Aquí esta {i}")
    else:
        print(f"Este país es {i}")


