#ESTRUCTURAS DE CONTROL CONDICIONAL

#Ejercicio 01: Crea una instrucción que imprima si 'aceptado' si una persona tiene más de 18 años, de lo contrario deberá imprimir 'denegado'

print("EJERCICIO 'MAYOR DE EDAD' ")

edad = 16

if edad >= 18:
    print("Aceptado")
else:
    print("Denegado")

print("")

#Ejercicio 02: Crea una instrucción que solicite el nombre al usuario y valide si es el propietario de un objeto. El programa debe imprimir feedback

print("EJERCICIO '¿ESTO ES TUYO?' ")

solicitar_nombre = input("Ingresa tu nombre por favor:").upper()

duenio = "PERLA"

if solicitar_nombre == duenio:
    print("Este objeto es de tu propiedad")
else:
    print("Este objeto no te pertenece")