"""
Nombre del ejercicio: Instrucción para salir de un programa

Instrucciones: 
1.- Usa while true para crear un programa que detenga su ejecución al recibir la instrucción 'exit'
2.- Si la instrrucción no es la correcta imprime el mensaje 'La instrucción no es correcta'
3.- Si la instrucción es correcta imprime el mensaje ' El programa se ejecutó correctamente' 

"""


while True:
    instruccion = input("Ingresa la palabra clave 'exit' para salir del programa: ")
    if instruccion.lower() == 'exit':
        break
    print(f"La instrucción {instruccion} no es valida")

print("La instrucción se ejecuto correctamente: programa cerrado")