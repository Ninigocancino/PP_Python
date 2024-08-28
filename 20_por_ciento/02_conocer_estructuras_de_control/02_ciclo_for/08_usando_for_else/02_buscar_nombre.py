"""
Nombre del ejercicio: Buscar un nombre en una lista

Instrucciones: 
1.- Crea una lista de nombres
2.- Recorre los elementos de la lista
3.- Guarda un nombre en una variable
4:- Comprueba si el nombre esta en la lista
5.- Si el nombre esta en la lista imprime 'el nombre esta en la lista'
6.- Si el nombre no esta en la lista imprime 'el nombre no esta en la lista'

"""

nombres = ['Macario', 'Sarahi', 'Adrián', 'Lupe', 'Saul', 'Lucas']

buscar_nombre = "Saul"

for i in nombres:
    if i == "Saul":
        print(f"{buscar_nombre} esta en la lista nombre")
        break
else: 
    print(f"{buscar_nombre} no esta en la lista nombres")