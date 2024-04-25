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

#Ejercicio 03: Crea un programa que pida al usuario la temperatura y devuelva un recomendación con base en el dato ingresado

print("EJERCICIO 'TEMPERATURA' ")

temp = float(input("Ingresa la temperatura actual(grados centigrados): "))

if temp < 0:
    print("Hace demasiado frio, no salgas a esta temperatura se congela el agua")
elif temp >= 0 and temp <= 10:
    print("Hace mucho frío, asegurate de abrigarte muy bien")
elif temp >10 and temp <= 20:
    print("Esta templado pudes salir, pero no olvides un abrigo ligero")
elif temp >20 and temp <= 24:
    print("El clima esta fresco puedes salir con ropa ligera")
elif temp >24 and temp <= 30:
    print("Es caluroso procura usar ropa comoda y tomar agua")
else:
    print("Es demasiado caluroso, no te expongas al sol y toma mucha agua")