"""
Nombre del ejercicio: Verdura y Frutas

Instrucciones: 
1.- Crea un diccionario con dos listas, una lista de frutas y una lista de verduras
2.- Itera sobre los elementos para mostrar en pantalla las dos listas que agrupan frutas y verduras
2.- Imprime el resultado

"""

canasta = {
    "frutas" : ['manzana','uva','pera'],
    "verduras" : ['zanahorias', 'rabano','calabaza'] 
}

for e in canasta:
    print(f"{e.capitalize()}:")
    for i in canasta[e]:
        print(f"{i.capitalize()}")
    print("")