# Ejercicio 01: Dada una lista, recorre cada elemento de la lista

ciudades = ['Bogota','Cali','México','Paris']

for i in ciudades:
    print(i)


# Ejercicio 02: Dadoun diccionario recorre cada uno de sus elementos e imprime por separado las clave y los valores del iterable
print("")
lugar = {'Ciudad':'Ciudad de México', 'País' : 'México'}

for clave in lugar:
    print(clave)
for valor in lugar.values():
    print(valor)