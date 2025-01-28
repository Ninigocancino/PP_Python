
#Trabajar con el diccionario 'ganadores_nobel' como una lista de diccionarios

ganadores_nobel = [
    {'nombre':'Geoffri Hinton','categoria': 'Física','anio':'2024'},
    {'nombre':'Anne L Huillier','categoria': 'Física','anio':'2023'},
    {'nombre':'Demis Hassabis','categoria': 'Quimica','anio':'2024'},
    {'nombre':'Moungi Bawendi','categoria': 'Quimica','anio':'2023'},
]

print("")
print("Lista de dicionarios:")
print(ganadores_nobel)
print()

print("Acceder al dicionario numero 4 de la lista")
print(ganadores_nobel[3])
print()

print("Acceder a la clave anio del diccionario número 2 de la lista")
print(ganadores_nobel[1]['anio'])
print()