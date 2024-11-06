"""
DESCRIPCIÓN DEL PROYECTO:

Nombre del Proyecto: Descuentapp

Instrucciones:
Crearemos un programa que permita a una tienda administrar sus ofertas y conocer la información relacionada a cada una de ellas y al mismo tiempo sea capaz de mostrar a los clientes el desglose de información referente a su compra.

Se requiere que el proyecto se aborde por bloques de funcionalidades para poder detectar errores e incorporar mejoras de forma más ágil y esbelta.

Caso de uso:
En una sucursal de la tienda algunos productos cuentan con un 7% de descuentos mientras otros no cuentan con descuento 

Historia de usuario:
Como comprador me gustaría poder saber que productos cuentan con descuento y cuales no cuentan con descuento, además de conocer cuanto es el mónto que ahorrare con respecto del precio normal

Criterios de calidad:
Además de los requisitos de la versión anterior...
1.- El programa debe permitir la interacción del usuario con el programa
2. -El programa debe incluir un invetario de 5 productos
2.- El programa debe mostrar si un producto ingresado por el usuario tiene descuento 
3.- El programa debe calcular el total de la compra
4.- El programa debe mostrar al usuario el ahorro en su compra
6.- El programa debe mostrar la información de la transacción de forma desglosada
7.- El programa debe mostrar un mensaje de despedida antes de cerrarse
"""


productos = ["Jabón", "Shampoo", "Pasta dental", "Crema corporal", "Desodorantes"]
precios = [20.0,50.0,25.0,40.0,30.0]
descuentos = [0.07,0.07,0.0,0.0,0.07]

#Bloque 1: Instrucción principal y bienvenida

print("")

print("_"*60)

print("")
print("*"*20,"DESCUENTAPP","*"*20)
print(" "*8,"Bienvenido, conoce tu descuento")

print("")

print("-"*13, "Tenemos ofertas para ti:","-"*13)
print("")
print("Nuestro inentario incluye los siguientes productos:")
print("")

#Mostrar inventario

for indice, producto in enumerate(productos):
    print(f"{indice + 1}.{producto} - ${precios[indice]}")



#Bloque 2: Definición de variables globales
