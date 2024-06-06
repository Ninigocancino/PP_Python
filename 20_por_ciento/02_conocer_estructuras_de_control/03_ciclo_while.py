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
