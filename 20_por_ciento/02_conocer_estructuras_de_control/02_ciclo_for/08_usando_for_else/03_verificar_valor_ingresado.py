"""
Nombre del ejercicio: Verificar si un valor ingresado coincide con los valores de una lista

Instrucciones: 
1.- Crea una lista de animales
2.- Pida al usuario que ingrese un animal 
3.- Recorre los elementos de la lista
4:- Comprueba si el animal buscado por el usuario esta en la lista
5.- Si el nombre esta en la lista imprime 'el nombre esta en la lista'
6.- Si el nombre no esta en la lista imprime 'el nombre no esta en la lista'

"""

animales = ["León", "Tigre", "Lobo", "Oso", "Boa"]

valor_ingresado = input("Por favor ingresa el nombre de un animal: ").capitalize()

for i in animales:
    if i == valor_ingresado:
        print(f"{valor_ingresado} esta en nuestra base de datos de animales")
        break
else: 
    print(f"{valor_ingresado} no esta en nuestra base de datos de animales")