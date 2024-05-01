# Ejercicio 01: Dada una lista, recorre cada elemento de la lista

ciudades = ['Bogota','Cali','México','Paris']

for i in ciudades:
    print(i)


# Ejercicio 02: Dado un diccionario recorre cada uno de sus elementos e imprime por separado las clave y los valores del iterable
print("")
lugar = {'Ciudad':'Ciudad de México', 'País' : 'México'}

for clave in lugar:
    print(clave)
for valor in lugar.values():
    print(valor)

#Ejercicio 03: Crea una lista con un solo elemento, luego recorre el elemento para imprimir en consola cada letra

print("")

palabra = ['Perro']

for i in palabra[0]:
    print(i)