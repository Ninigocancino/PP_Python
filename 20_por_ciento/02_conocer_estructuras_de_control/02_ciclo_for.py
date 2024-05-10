
#Recursos
ciudades = ['Bogota','Cali','México','Paris']
lugar = {'Ciudad':'Ciudad de México', 'País' : 'México'}
palabra = ['Perro']
nombres = ['Julio','Marco', 'Sandra', 'Felipe','María']
paises = ['México','Sudafrica','Canada','Colombia','Cuba']
animales = ['Zorro','Canguro','León','Caballo']


#RECORRER E IMPRIMIR VALORES

print("NIVEL BÁSICO DE CICLO FOR")
print("PRACTICA 01: RECORRER E IMPRIMIR VALORES")
print("")

# Ejercicio 01(ciudades): Usa la lista ciudades y recorre cada elemento de la lista
print("*"*20)
print("EJERICICIO 01: CIUDADES")

for i in ciudades:
    print(i)

print("")

#Ejericio 02(nombres): Usa la lista nombres y recorre cada elemento
print("*"*20)
print("EJERCICIO 02: NOMBRES")

for nombre in nombres:
    print(nombre)

print("")

# Ejercicio 03: Usa el diccionario 'lugar' y recorre cada uno de sus elementos e imprime por separado las clave y los valores del iterable
print("*"*20)
print("EJERCICIO 03: LUGARES")

for clave in lugar:
    print(clave)
for valor in lugar.values():
    print(valor)

# Ejercicio 04(Paises): Usa la lista 'Paises' y recorre cada elemento
print("")
print("*"*20)
print("EJERCICIO 04: PAISES")
for i in paises:
    print(i)

# Ejercicio 05(animales): Usa la lista animales y recorre cada elemento
print("")
print("*"*20)
print("EJERCICIO 05:ANIMALES")

for i in animales:
    print(i)

print("")


#RECORRIENDO SOBRE UN ELEMENTO

#Ejercicio 06: Crea una lista con un solo elemento, luego recorre el elemento para imprimir en consola cada letra

print("*"*20)
print("EJERCICIO 06: PALABRA")

for i in palabra[0]:
    print(i)

print("")  

# Ejercicio 07(variable): Recorre el valor de una variable
print("*"*20)
print("EJERCICIO 07: RECORRER ELEMENTO DE VARIABLE")

palabra_01 = "letra"

for i in palabra_01:
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








