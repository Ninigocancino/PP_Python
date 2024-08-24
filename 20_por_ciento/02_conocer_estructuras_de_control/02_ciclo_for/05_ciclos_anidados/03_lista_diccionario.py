"""
Nombre del ejercicio: Itera sobre lista de diccionario

Instrucciones: 
1.- Crea un diccionario con dos elementos que contienen listas
2.- Itera sobre cada elemento
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