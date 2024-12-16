"""
Nombre del ejercicio: Tablas de multiplicar del 1 al 10

Instrucciones: 
1.- Usa el ciclo for para crear lastablas de multiplicar del 1 al 10
2.- Imprime cada una de las tablas

"""

for i in range(1,11):
    for n in range(1,11):
        multiplicar = n * i
        print(f"{n} X {i} = {multiplicar}")
    print("")
