"""
Nombre del ejercicio: Combinaciones en conteo anidado

Instrucciones: 
1.- Crea un conteo que controle la ejecución de otro conteo mientras la cuenta en ambos conteos sea menor de tres 
2.- Imprime las combinaciones posibles

"""

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f" i = {i}, j = {j}")
        j +=1
    
    i +=1