"""
Nombre del ejercicio: Buscar número en una lista

Instrucciones: 
1.- Crea una lista de números
2.- Recorre los elementos de la lista
3.- Si el número se encunetra en la lista imprime 'esta en la lista'
4:- Si no esta en la lista impirme 'No esta en la lista

"""

l_numeros = [20,25,60,15, 10]
buscar = 12

for i in l_numeros:
    if i == buscar:
        print(f"El numero {buscar} se encuentra en la lista")
        break
else:
    print(f"El numero {buscar} no se encuentra en la lista")