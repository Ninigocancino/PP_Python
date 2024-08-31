"""
Nombre del ejercicio: Validación de datos de registro

Instrucciones: 
1.- Crea datos de control
2.- Pregunta al usuario su nombre, edad y altura
3.- Usa While True para comparar si los datos ingresados concuerdadn con los de control
4.- Si los datos coinciden imprime 'Hola ___ ¿qué quieres hacer?
5.- Si los datos no coinciden imprime 'No eres ___'

"""

while True:
    edad_usuario = 45
    nombre_usuario = "Lucas"
    altura_usuario = 1.70

    edad_g = int(input("Ingresa tu edad: "))
    nombre_u = input("Ingresa tu nombre: ")
    altura_u = float(input("Ingresa tu estatura:"))

    if edad_usuario == edad_g and nombre_usuario == nombre_u and altura_usuario == altura_u:
        break
    print("No eres Lucas, intenta de nuevo")

print("Hola Lucas ¿Qué quieres hacer?")