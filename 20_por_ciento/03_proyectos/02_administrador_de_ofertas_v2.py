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
2.- El programa debe mostrar si un producto ingresado por el usuario tiene descuento 
3.- El programa debe calcular el total de la compra
4.- El programa debe mostrar al usuario el ahorro en su compra
6.- El programa debe mostrar la información de la transacción de forma desglosada
7.- El programa debe mostrar un mensaje de despedida antes de cerrarse
"""

# Agrega formato a la entrada del programa

print("")

print("_"*60)

print("")
print("*"*20,"DESCUENTAPP","*"*20)
print(" "*8,"Bienvenido, conoce tu descuento")

print("")

print("-"*13, "Tenemos ofertas para ti:","-"*13)
print("")
print("Ingresa para descubrir nuestro catálogo de productos")
print("")

"""
print(" "*4,"Oferta:")
print(" "*4,"Descuento: '7 %'")
print(" "*4,"Productos: Toda la tienda")
"""

desc_producto = {
    'Camisa sport' : 0,
    'Zapatos' : 0,
    'Gafas' : 7,
    'Short berm' : 0,
    'Jeans' : 7
}

cat_producto = {
    'Camisa sport' : 200,
    'Zapatos' : 450,
    'Gafas' : 180,
    'Short berm' : 340,
    'Jeans' : 650
}

total_compra = 0

ahorro = 0

compras = []

cantidad = []

print("¿Deseas continuar al catálogo?")
entrada = int(input("Ingresar a '1' para continuar y '2' para salir: "))

if entrada == 1:
    print("¡HOLA!")
    print("Dale un vistazo a nuestros productos disponibles: ")

    for clave in desc_producto:
        print(clave)

else:
    exit()

print("")
print("¿Deseas consultar descuentos en productos?")

consulta = int(input('ingresa 1 para consultar o cualquier otro número para continuar: '))

if consulta == 1:
    producto = input("¿Qué producto deseas consultar?: ").capitalize()

    for clave, valor in desc_producto.items():
        if clave == producto:
            print(clave,valor)

else:
    print("")

print("Iniciemos tus compras ")
print("Ingresa '1' para agregar a carrito de compra")
print("Ingresa '2' para salir")

entry = int(input("¿Que deseas hacer?: "))

if entry == 1:

    print("Catálogo de productos")

    for c,v in cat_producto.items():
        print(c,v)

    print("")

    producto_1 = input("Ingresa el árticulo: ")

          

"""
# Se realiza la operación 

compra = 300

rebaja = 0.07

descuento = compra * rebaja

total = compra - descuento

print("")
print(" "*6,f"Su compra es de {compra}")
print(" "*6,f"Su descuento es {descuento}")
print(" "*6,f"Total a pagar: {total}")


#Proporciona formato después de la ejecución de la operación

print("")
print(" "*4,"Gracias por su compra vuelva pronto")



print("")

print("_"*60)

print("")

exit()

"""