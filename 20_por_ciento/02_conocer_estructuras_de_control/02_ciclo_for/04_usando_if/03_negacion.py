"""
Nombre del ejercicio: Animal en lista

Instrucciones: 
1.- Crea una lista de animales y niega que 'Canguro' se encuentre en la lista
2.- Usa un ciclo for para recorrer cada elemento
3.- Imprime '____ está en la lista' para cada animal que no hayas negado y para canguro 'este animal no esta en la lista'

"""

animales = ['Lobo', 'Zorro', 'Hipopotamo', 'Comadreja','León', 'Jaguar']

print("")
print("Vamos si tenemos un Canguro")
print("")
animal_buscado = input("Ingresa la palabara Canguro: ")


for animal in animales:
    if not animal == animal_buscado:
        print("")
        print(f"encontre un {animal} en la lista")
        if not animal_buscado in animales:
            print(f"pero no encontre un {animal_buscado} en la lista")
            print("")
    else:
        print(f"No pude buscar este animal {animal_buscado}")
        print("Pero...")