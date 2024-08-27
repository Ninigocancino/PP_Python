"""
Nombre del ejercicio: Detener la iteración de una lista

Instrucciones: 
1.- Crea una lista con almenos 5 elementos
2.- Has que el programa se detenga cuando encuentre un valores especifico en la lista
3.- Imprime los elementos antes del break

"""

items = ['camiseta','sandalias','gorras','alimentos','decoración']

for i in items:
    if i == 'sandalias':
        break
    print(i)
print(f"El break esta en  {i}")