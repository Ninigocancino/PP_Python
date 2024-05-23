
#Recursos
ciudades = ['Bogota','Cali','México','Paris','Atenas']
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

print("")

#Ejercicio 08(nombres): Usa la lista 'nombres' y recorre el elemento de la posición 2

print("*"*20)
print("EJERCICIO 08: RECORRE UN ELEMENTO DE LA LISTA NOMBRES")

for i in nombres[2]:
    print(i)

print("")

#Ejercicio 09: Usa la lista 'ciudades' y recorre l elemnto de la posición 4

print("*"*20)
print("EJERCICIO 09: RECORRER UN ELEMENTO DE LA LISTA 'CIUDADES' ")

for i in ciudades[4]:
    print(i)

print("")

#USAR RANGOS

#Ejercicio 10: Crea un rango de  0 a 5 y recorrelo
print("*"*20)
print("EJERCICIO 10: RECORRE UN RANGO DE 0 A 5")
for i in range(0,5):
    print(i)

print("")

#Ejercicio 11: Crea un rango de 0 a 5 e imprimelo
print("*"*20)
print("EJERCICIO 12: CREAR UN RANGO E IMPRIMIRLO")

for i in range(0,5):
    print(i)

print("")

#Ejercicio 12: Crea un rango del 0 al 100 con incrementos de 10 en 10, luego recorre el rango e imprimelo
print("*"*20)
print("EJERCICIO 12: RECORRER RANGO CON INCREMENTOS")

for i in range(0,100,10):
    print(i)

print("")

#Ejercicio 13: Crea un rango del 5 al 200 con incrementos de 5, luego eleva al cuadrado cada elemento
print("*"*20)
print("EJERCICIO 13: RANGOCON INCREMENTO Y OPERACIÓN MATEMATICA")

for i in range(5,200,5):
    i = i**2
    print(i)

print("")


#USANDO IF

#Ejercicio 14: Usa la lista paises y recorrela en busca del elemento 'México', si el valor se encuentra en la lista imprime un mensaje descriptivo en consola
print("*"*20)
print("EJERCICIO 14: vALIDACIÓN DE VALOR EXISTENTE EN LA LISTA PAISES")

for i in paises:
    if i == 'México':
        print("Mexico está en la lista")

print("")

#Ejercicio 15: En un rango de 0 a 20 imprime todo los numeros que sean pares
print("*"*20)
print("EJERCICIO 15: RECORRE LOS NÚMERO PARES DE UN RANGO DE 0 A 20")

for i in range(0,21):
    if i % 2 == 0:
        print(i)

print("")

#Ejercicio 16: Usa la lista animales y niega que 'Canguro' se encuentre en la lista. Luego imprime '____ está en la lista' para cada animal que no hayas negado y para canguro 'este animal no esta en la lista'
print("*"*20)
print("EJERCICIO 16: NIEGA QUE UN ANIMAL ESTE EN LA LISTA")

for i in animales:
    if not i == 'Canguro':
        print(f"{i} está en la lista")
    else:
        print("este animal no está en la lista")

print("")
print(animales)

print("")

#CICLOS ANIDADOS
#     Apartir de este punto usaremos elementos iterables propios para cada ejercicio
#Ejercicio 17: Crea una matriz de elementos numericos desde una lista de lista e imprime cada fila de la matriz

print("*"*20)
print("EJERCICIO 17: ITERA SOBRE LAS FILAS DE UNA MATRIZ")

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

for i in matriz:
    for e in i:
        print(e, end=",")
    print("")

print("")
#USAR CONTINUE Y BREAK

#USANDO MÉTODOS

#Ejercicio 06: Toma la lista ciudades y conbierte cada elemento a mayúsculas

print("")

for i in ciudades:
    mayusculas = i.upper()
    print(mayusculas)

#USANDO FOR ELSE

#USANDO ZIP








