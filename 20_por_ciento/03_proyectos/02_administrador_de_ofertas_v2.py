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

#Bloque 1: Instrucción principal y bienvenida

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

#Bloque 2: Definición de variables globales

productos = [
    "Camisa sport",
    "Zapatos",
    "Gafas",
    "Short berm",
    "Jeans"
]

desc_producto = {
    'Camisa sport' : 0,
    'Zapatos' : 0,
    'Gafas' : 7,
    'Short berm' : 0,
    'Jeans' : 7
}

cat_producto = {
    'CAMISA SPORT' : 200,
    'ZAPATOS' : 450,
    'GAFAS' : 180,
    'SHORT BERM' : 340,
    'JEANS' : 650
}

camisas_count = []
zapatos_count = []
gafas_count = []
shorts_count = []
jeans_count = []

sub_totales = []
sub_total_desc = []

producto_agregado = []


#Bloque 3: Interacción inicial con el usuario

print("¿Deseas continuar al catálogo?")
entrada = int(input("Ingresar a '1' para continuar y '2' para salir: "))
print("")


if entrada == 1:
    print("¡HOLA!")
    print("PASO 1: ECHALE UN VISTAZO A NUESTRO CATÁLOGO DE PRODUCTOS")
    print("")

    for clave in desc_producto:
        print(clave)

else:
    exit()


#Bloque 4: Consultar descuento

print("")
print("PASO 2: CONSULTA LOS DESCUENTOS EN NUESTROS PRODUCTOS")
print("¿Deseas consultar descuentos en productos?")
print("") 

consulta = int(input('ingresa 1 para consultar o cualquier otro número para continuar: '))

#opción 1:

"""
if consulta == 1:
    producto = input("¿Qué producto deseas consultar?: ").capitalize()

    for clave, valor in desc_producto.items():
        if clave == producto:
            print(f"{clave} tiene {valor}% de descuento")

else:
    print("")

"""
#opción 2: 

if consulta == 1:
    producto = input("¿Qué producto deseas consultar?: ").capitalize()

    if producto in desc_producto:
        print(f"{producto} tiene {desc_producto[producto]}% de descuento")

    else:
        print("")

#Bloque 5:

print("")
print("PASO 3: AGREGA PRODUCTOS AL CARRITO DE COMPRA")
print("Ingresa '1' para agregar a carrito de compra")
print("Ingresa '2' para salir")
print("")

entry = int(input("¿Que deseas hacer?: "))

if entry == 1:

    print("")
    print("Catálogo de productos")
    
    for c, v in cat_producto.items():
        print(f"- {c} ${v}")

    print("")

    disparador = input("¿Deseas agregar un producto? Ingresa (si) o (no): ") 

    while disparador == "si":

        producto_1 = input("Ingresa el árticulo: ").upper()

        if producto in cat_producto:

            cantidad = int(input(f"¿Cuántas unidades de {producto} deseas agregar?: "))

            if producto_1 == "CAMISA SPORT":
                camisas_count.append(cantidad)
            elif producto_1 == 'ZAPATOS': 
                zapatos_count.append(cantidad) 
            elif producto_1 == 'GAFAS': 
                gafas_count.append(cantidad) 
            elif producto_1 == 'SHORT BERM': 
                shorts_count.append(cantidad) 
            elif producto_1 == 'JEANS': 
                jeans_count.append(cantidad)

            precio = cat_producto[producto_1] 
            subtotal = precio * cantidad 
            sub_totales.append(subtotal)

            descuento = (subtotal * desc_producto[producto_1.capitalize()]) / 100
            sub_total_desc.append(descuento)

            print(f"Has agregado {cantidad} unidades de {producto_1}. Subtotal: ${subtotal}. Descuento: ${descuento}")

            if producto_1 not in producto_agregado: 
                producto_agregado.append(producto_1)

            disparador = input("¿Deseas agregar otro producto? Ingresa (si) o (no): ")

        else:
            print(f"El producto {producto_1} no está en el catálogo.")


#Bloque 6:

print("") 
print(producto_agregado) 
print("Tus compras fueron: ") 
for c, v in zip(producto_agregado, sub_totales): 
    print(f"{c}: Subtotal = ${v}")
    
total_compra = sum(sub_totales)  # Suma de todos los subtotales
compra_con_descuento = sum(sub_total_desc)  # Suma de todos los descuentos
tc = total_compra - compra_con_descuento  # Total con descuento aplicado

# Muestra los totales al usuario
print(f"\nTotal de la compra: ${total_compra}") 
print(f"Tu ahorro fue: ${compra_con_descuento}") 
print(f"Total con descuento aplicado: ${tc}")


        