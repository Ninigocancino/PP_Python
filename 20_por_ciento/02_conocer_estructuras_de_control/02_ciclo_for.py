
#Recursos
ciudades = ['Bogota','Cali','México','Paris']
lugar = {'Ciudad':'Ciudad de México', 'País' : 'México'}
palabra = ['Perro']
nombres = ['Julio','Marco', 'Sandra', 'Felipe','María']

#BÁSICO

# Ejercicio 01: Usa la lista ciudades y recorre cada elemento de la lista
print("")
print("NIVEL BÁSICO DE CICLO FOR")
print("Ejercicio 01: Ciudades")


for i in ciudades:
    print(i)

#Ejericio 02: Usa la lista nombres y recorre cada elemento
print("")
print("Ejercicio 02: Nombres")


for nombre in nombres:
    print(nombre)

# Ejercicio 02: Dado un diccionario recorre cada uno de sus elementos e imprime por separado las clave y los valores del iterable
print("")

for clave in lugar:
    print(clave)
for valor in lugar.values():
    print(valor)

#Ejercicio 03: Crea una lista con un solo elemento, luego recorre el elemento para imprimir en consola cada letra

print("")

for i in palabra[0]:
    print(i)

#Ejercicio 04: En un rango de 0 a 20 imprime todo los numeros que sean pares
print("")
for i in range(0,21):
    if i % 2 == 0:
        print(i)


#Ejercicio 05: Toma la lista ciudades y conbierte cada elemento a mayúsculas

print("")

for i in ciudades:
    mayusculas = i.upper()
    print(mayusculas)