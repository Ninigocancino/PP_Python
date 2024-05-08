
#Recursos
ciudades = ['Bogota','Cali','México','Paris']
lugar = {'Ciudad':'Ciudad de México', 'País' : 'México'}
palabra = ['Perro']
nombres = ['Julio','Marco', 'Sandra', 'Felipe','María']
paises = ['México','Sudafrica','Canada','Colombia','Cuba']

#RECORRER E IMPRIMIR VALORES

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

# Ejercicio 03: Usa el diccionario 'lugar' y recorre cada uno de sus elementos e imprime por separado las clave y los valores del iterable
print("")

for clave in lugar:
    print(clave)
for valor in lugar.values():
    print(valor)

# Ejercicio 04(Paises): Usa la lista 'Paises' y recorre cada elemento
print("")
print("*"*10)
print("EJERCICIO 04: PAISES")
for i in paises:
    print(i)

#RECORRIENDO SOBRE UN ELEMENTO

#Ejercicio 04: Crea una lista con un solo elemento, luego recorre el elemento para imprimir en consola cada letra

print("")

for i in palabra[0]:
    print(i)


#USAR RANGOS

#Ejercicio 05: En un rango de 0 a 20 imprime todo los numeros que sean pares
print("")
for i in range(0,21):
    if i % 2 == 0:
        print(i)


#USANDO IF

#Ejercicio 03: Usa la lista paises y recorrela en busca del elemento 'México', si el valor se encuentra en la lista imprime un mensaje descriptivo en consola
print("")
for i in paises:
    if i == 'México':
        print("Mexico está en la lista")

#CICLOS ANIDADOS

#USAR CONTINUE Y BREAK

#USANDO MÉTODOS

#Ejercicio 06: Toma la lista ciudades y conbierte cada elemento a mayúsculas

print("")

for i in ciudades:
    mayusculas = i.upper()
    print(mayusculas)

#USANDO FOR ELSE

#USANDO ZIP








