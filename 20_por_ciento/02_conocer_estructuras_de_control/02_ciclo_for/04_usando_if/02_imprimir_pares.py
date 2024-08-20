"""
Nombre del ejercicio: Imprimir los números pares en un rango dado

Instrucciones: 
1.- Crea un rango del 0 al 20
2.- Usa un ciclo for para recorrer el rango mientras los números sean pares
3.- Imprime los valores 

"""

for i in range(0,20):
    if i % 2 == 0:
        print(f"{i} es un número par")
    