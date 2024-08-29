"""
Nombre del ejercicio: Secuencia de lanzamiento personalizada

Instrucciones: 
1.- Pide al usuario que ingrese una cantidad deseada
2.- Usa el ciclo while para decrecer la cantidad ingresada por el usuario hasta que se cumpla una condición especifica
2.- Imprime el conteo 

"""

tamanio_cuenta = int(input("¿Qué tan larga quieres que sea la cuenta regresiva para el lanzamiento: "))

while tamanio_cuenta != 0:
    uno = 1
    print("")
    print("El lanzamiento iniciará en: ")
    while uno <= tamanio_cuenta:
        print(tamanio_cuenta)
        tamanio_cuenta -= 1
    print("Lanzamiento")
    break
