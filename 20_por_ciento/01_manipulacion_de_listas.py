
#CREACIÓN DE LISTAS

#Ejercicio 01: Crea una lista de 5 elementos con nombres de personas e imprime el contenido.
print("Lista 1:")
nombres= ['Juan','Pablo','Lisa','Sebastian','Laura']
print(nombres)

#Ejercicio 02: Crea una lista con numeros del 0 al 4 e imprime el contenido.
print("")
print("Lista 2:")
numeros= [0,1,2,3,4]
print(numeros)

#Ejercicio 03: Crea una lista de 5 elementos con nombres de animales domesticos e imprime el contenido.
print("")
print("Lista 3:")
animales= ['Perro','Gato','Hamster','Perico','Caballo']
print(animales)

#Ejercicio 04: Accede a uno de los elementos de cada lista creada.
print("")
nombre_elegido =nombres[2]
print(f"El nombre {nombre_elegido} se encuentra en la lista")

print("")
numero_elegido = numeros[1]
print(f"El número {numero_elegido} esta en la lista")

print("")
animal_elegido = animales[3]
print(f"El animal {animal_elegido} esta en la lista")

#Ejercicio 05: Crea una sublista de cada una de las listas creadas.
print("")
nombres_dos = nombres[2:5]
print("Nuevo lista de nombres:")
print(nombres_dos)

print("")
numeros_dos = numeros[2:4]
print("Nueva lista de numeros:")
print(numeros_dos)

print("")
animales_dos = animales[0:2]
print("Nueva lista de animales:")
print(animales_dos)