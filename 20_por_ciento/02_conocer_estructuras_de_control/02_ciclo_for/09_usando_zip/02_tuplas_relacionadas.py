"""
Nombre del ejercicio: Emparejar dos tuplas

Instrucciones: 
1.- Crea dos tuplas relacionadas conceptualmente
2.- Usa el método ZIP para iterarlas simultaneamente. Las tuplas deben contener el mismo número de elementos (al menos tres por cada tupla)
3.- Imprime un mensaje que contenga las iteraciones simultaneas

"""

tipos = ("mascota","silvestre","salvaje","ganado")
animales = ("perro",'conejo','león','vaca')

for animal,tipo in zip(tipos,animales):
    print(f"{animal}:{tipo}")