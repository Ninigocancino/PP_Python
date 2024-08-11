"""
Nombre del ejercicio: Solo mayores de edad

Instrucciones: 
1.- Crea una instrucción que imprima 'bienvenido puede pasar' si una persona tiene más de 18 años, de lo contrario deberá imprimir 'lo siento solo mayores de 18 años pueden ingresar'
2.- Permite al usuario ingresar datos

"""

print("Hola")
edad_usuario = int(input("¿Cuál es tu edad?: "))

if edad_usuario >= 18:
    print("Bienvenido, puede pasar")
else: 
    print("Lo siento, solo mayores de 18 años pueden ingresar")