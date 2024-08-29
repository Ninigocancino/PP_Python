"""
Nombre del ejercicio: Adivina la edad 

Instrucciones: 
1.- Usa while true para crear un programa que le pida al usuario adivinar la edad de Lucas 
2.- Compara la edad de Lucas con el número ingresado por el usuario
3.- Si las cifras no coinciden imprime 'La edad no es correcta'
4.- Si las cifras coinciden imprime 'Acertaste, la edad es correcta'

"""

print("Adivina que edad tiene Lucas")

while True: 
    edad_usuario = int(input("¿Qué edad crees que tiene Lucas?: "))
    edad = 25
    if edad_usuario < edad:
        print("Uy! Lucas es un poco mayor")
    elif edad_usuario > edad:
        print("Lucas es un poco más jóven")
    elif edad_usuario == edad:
        break
    #print("la edad no es correcta")

print("Acertaste: la edad es correcta")