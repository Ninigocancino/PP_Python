
# Trabajar el dicionario 'Planetas' como lista de diccionarios

planeta = [
    {'nombre': 'Tierra', 'posición': '3'},
    {'nombre': 'Mercurio', 'posición': '1'},
    {'nombre': 'Urano', 'posición': '6'}
]

print("")
print("Lista de diciconarios 'Planeta': ")
print(planeta)
print("")

print("Acceder al primer diccionario de la lista")
print(planeta[0])
print("")

print("Acceder al valor de la clave nombre en el tercer diciconario de la lista")
print(planeta[2]['nombre'])
print("")

print("Agregar una nueva clave al diciconario 2 de la lista")
planeta[0]['tipo'] = 'Rocoso'
print(planeta[0])
print("")
print(planeta)
print()

print(planeta)
print()
print("Modifica el valor de la clave 'posición' en el diccionario 3 de la lista")
planeta[2]['posición'] = '7'
print(planeta)
print()
