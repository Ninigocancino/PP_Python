"""
DESCRIPCIÓN DEL PROYECTO:

Nombre del Proyecto: Control de ofertas

Instrucciones:
Crearemos un programa que permita a una tienda administrar sus ofertas y conocer la información relacionada a cada una de allas y al mismo tiempo sea capaz de mostrar a los clientes el desglose de información referente a su compra.

Se requiere que el proyecto se aborde por bloques de funcionalidades para poder detectar errores e incorporar mejoras de forma más ágil y esbelta.

Caso de uso:
En una surucrsal de la empresa se hace un descuento del 7% sobre el total de las compras, calcula la cantidad a pagar por una compra determinada

Historia de usuario:
Como comprador me gustaría poder saber de cuanto es el ahorro que tender en esta compra

Criterios de calidad:
1.- El programa debe imprimir un mensaje de bienvenida
2.- El programa debe debe imprimir una descripción del programa
3.- El programa debe debe imprimir al menos dos de las instrucciones del juego
4.- Los textos deben mostrarse de forma amigable para facilitar al usuario su lectura 
5.- El programa debe calcular el descuento de un monto con base en el descueto establecido de 7% sobre cualquier producto de la     sucursal.
6.- El programa debe mostrar la información de la transacción de forma desglosada
7.- El programa debe mostrar un mensaje de despedida antes de cerrarse
"""

print("Hoy tenemos 7 por ciento de descuento en toda la tienda")

compra = float(input("Ingrese el monto de la campra: "))

rebaja = 0.07

descuento = compra * rebaja

total = compra - descuento

print(f"Su compra es de {compra}")
print(f"Su descuento es {descuento}")
print(f"Total a pagar: {total}")

print("")
print("Gracias por su compra vuelva pronto")

exit()