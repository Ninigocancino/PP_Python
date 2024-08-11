"""
Nombre del ejercicio: ¿Esto es tuyo?

Instrucciones: 
1.- Crea un script que pregunte el nombre del usuario para validar si un objeto le pertenece o no
2.- Si el objeto le pertenece se debe imprimir el mensaje 'aquí lo tiene, disculpe el inconveniente'
3.- De no pertenecer debe imprimir el mensaje 'Lo sentimos su nombre no coincide con el del propietario' 

"""

print("EJERCICIO '¿ESTO ES TUYO?' ")

solicitar_nombre = input("Ingresa tu nombre por favor:").upper()

duenio = "PERLA"

if solicitar_nombre == duenio:
    print("Aquí lo tiene, disculpe el inconveniente")
else:
    print("Lo sentimos, no podemos entregar el objeto: \nsu nombre no coincide con el del propietario")
