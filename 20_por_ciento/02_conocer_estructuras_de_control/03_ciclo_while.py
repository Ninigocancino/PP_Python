# IMPLEMENTACIÓN BÁSICA DEL CICLO WHILE

#Ejercicio 01: Itera una lista numérica  mientras el número sea menor al resultado de una operación dada
print("*"*20)
print("EJERCICIO 01: CONTADOR")
print("")

a = 3
b = 2
operacion = a*b

contador = 0

while operacion > contador:
    print(F"contador es: {contador}")
    contador += 1

print("")

#Ejercicio 02: crea una cuenta regresiva condicional 
print("*"*20)
print("EJERCICIO 02: CUENTA REGRESIVA")
print("")

operacion2 = 0

decrecer = 10

while operacion2 < decrecer:
    print(decrecer)
    decrecer  -= 1

print("")

#Ejercicio 03: Inicia una secuencia de lanzamiento personalizable
print("*"*20)
print("EJERCICIO 03: SECUENCIA DE LANZAMIENTO PERSONALIZADA")
print()

respuesta = int(input("¿Qué tan larga quieres que sea la cuenta regresiva para el lanzamiento: "))

while respuesta != 0:
    uno = 1
    print("")
    print("El lanzamiento iniciará en: ")
    while uno <= respuesta:
        print(respuesta)
        respuesta -= 1
    print("Lanzamiento")
    break

print("")

# USANDO WHILE TRUE

#Ejercicio 04: Crea una salida de un programa 
print("*"*20)
print("EJERCICIO 04: INSTRUCCIÓN PARA SALIR DE PROGRAMA")
print("")

while True:
    instruccion = input("Ingresa la palabra clave 'exit' para salir del programa: ")
    if instruccion.lower() == 'exit':
        break
    print(f"La instrucción {instruccion} no es valida")

print("La instrucción se ejecuto correctamente: programa cerrado")

#Ejercicio 05: Crea un programa que pregunte al usuario su edad y se detenga hasta que la edad sea igual a  25
print("*"*20)
print("EJERCICIO 05: ADIVINA LA EDAD")
print("")

while True: 
    edad_usuario = int(input("¿Cuál es tu edad?: "))
    edad = 25
    if edad_usuario == edad:
        break
    print("la edad no es correcta")

print("la edad es correcta")