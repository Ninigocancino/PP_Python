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

#Elementos para acumular valores relacionados con las compras y productos

productos_comprados = []
total = 0.0
ahorro_total = 0.0

while True: 
    seleccion = input("Ingresa el número del producto que deseas comprar (o escribe 'salir' para terminar): ")

    #Condición para finalizar la compra
    if seleccion.lower() == "salir":
        break

    #Convertir selección a un indice de la lista
    try:
        indice = int(seleccion) -1
        if 0 <= indice < len(productos):
            #Agregar el producto seleccionado a la lista de productos comprados
            productos_comprados.append(productos[indice])

            #Calcular el precio con descuento si aplica
            precio = precios[indice]
            descuento = descuentos[indice]
            if descuento > 0:
                ahorro = precio * descuento
                precio_final = precio - ahorro
                print(f"{productos[indice]} tiene un descuento del 7%. Precio final: ${precio_final:.2f}")
            else:
                ahorro = 0
                precio_final = precio
                print(f"{productos[indice]} no tiene descuento. Precio: ${precio_final:.2f}")

            #Actualizar total de compra y ahorro acumulado
            total += precio_final
            ahorro_total += ahorro

        else:
            print("Por favor, selecciona un número válido.")
    except ValueError:
        print("Entrada no valida. Por favor ingresa un número o 'salir'. ")

print("/nResumen de tu compra: ")
print("Productos comprados: ", ", ".join(productos_comprados))
print(f"Total comprado: ${total:.2f}")
print(f"Total ahorrado: ${ahorro_total:.2f}")

#Mensaje de despedida
print("Gracias por usar Descuentapp. ¡Hasta pronto!")
