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
sub_total_desc_camisas = []
sub_total_desc_zapatos = []
sub_total_desc_gafas = []
sub_total_desc_shorts = []
sub_total_desc_jeans =[]

producto_agregado = []

compras = []
cantidad = []

ahorro = 0

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

print("")
print("PASO 2: CONSULTA LOS DESCUENTOS EN NUESTROS PRODUCTOS")
print("¿Deseas consultar descuentos en productos?")
print("")

consulta = int(input('ingresa 1 para consultar o cualquier otro número para continuar: '))

if consulta == 1:
    producto = input("¿Qué producto deseas consultar?: ").capitalize()

    for clave, valor in desc_producto.items():
        if clave == producto:
            print(f"{clave} tiene {valor}% de descuento")

else:
    print("")

print("")
print("PASO 3: AGREGA PRODUCTOS AL CARRITO DE COMPRA")
print("Ingresa '1' para agregar a carrito de compra")
print("Ingresa '2' para salir")
print("")

entry = int(input("¿Que deseas hacer?: "))

if entry == 1:

    print("")
    print("Catálogo de productos")

    for c,v in cat_producto.items():
        print(f"-{c} ${v}")

    print("")

    disparador = input("Deseas agregar un producto? Ingresa (si) o (no): ")

    while disparador == "si":
        producto_1 = input("Ingresa el árticulo: ").upper()

        if producto_1 == 'CAMISA SPORT':
            cantidad = int(input("¿Cuántas camisas deseas agregar?: "))
            camisas_count.append(cantidad)

            for i in camisas_count:
                print(f"{i} Camisas agregadas")

            for c,v in cat_producto.items():
                if c == producto_1:
                    precio = v

                    #multiplicador = sum(camisas_count)
                    if precio > 0:
                        
                        print(f"El precio por pieza es: ${precio}")
                        subtotal = precio * i
                        sub_totales.append(subtotal)

                        for clave,valor in desc_producto.items():
                            if clave == producto_1 and valor < 0:
                                descuento = subtotal * valor / 100
                                #print(c)
                                #print(v)
                                #print(descuento)


                                sub_total_desc_camisas.append(descuento)
                                print(f"precio con descuento: {descuento}")
                            else:
                                print(f"No hay descuento el precio es {subtotal}")
                                break
                    else:
                        print("Precio no disponible")
            if producto_1 not in producto_agregado: 
                producto_agregado.append(producto_1)
                print(producto_agregado)
            #break

        elif producto_1 == 'ZAPATOS':
            cantidad = int(input("¿Cuántos pares de zapatos deseas agregar?: "))
            zapatos_count.append(cantidad)
            
            for i in zapatos_count:
                print(f"{i} pares de zapatos agregados")

            for c,v in cat_producto.items():
                if c == producto_1:
                    precio = v

                    #multiplicador = sum(zapatos_count)
                    if precio > 0:
                        
                        print(f"El precio por pieza es: ${precio}")
                        subtotal = precio * i
                        sub_totales.append(subtotal)

                        for clave,valor in desc_producto.items():
                            if clave == producto_1 and valor < 0:
                                descuento = subtotal * valor / 100

                                sub_total_desc_camisas.append(descuento)
                                print(f"precio con descuento: {descuento}")
                            else:
                                print(f"No hay descuento el precio es {subtotal}")
                                break
                    else:
                        print("Precio no disponible")

            if producto_1 not in producto_agregado: 
                producto_agregado.append(producto_1)
                print(producto_agregado)
            #break
        
        elif producto_1 == 'GAFAS':
            cantidad = int(input("¿Cuántas gafas deseas agregar?: "))
            gafas_count.append(cantidad)
            
            for i in gafas_count:
                print(f"{i} gafas agregadas")

            for c,v in cat_producto.items():
                if c == producto_1:
                    precio = v

                    #multiplicador = sum(gafas_count)

                    if precio > 0:
                        
                        print(f"El precio por pieza es: ${precio}")
                        subtotal = precio * i
                        sub_totales.append(subtotal)

                        for clave,valor in desc_producto.items():
                            if clave == producto_1 and valor < 0:
                                descuento = subtotal * valor / 100
                                
                                sub_total_desc_camisas.append(descuento)
                                print(f"precio con descuento: {descuento}")
                            else:
                                print(f"No hay descuento el precio es {subtotal}")
                                break
                    else:
                        print("Precio no disponible")

            if producto_1 not in producto_agregado: 
                producto_agregado.append(producto_1)
                print(producto_agregado)


        elif producto_1 == 'SHORT BERM':
            cantidad = int(input("¿Cuántos shorts deseas agregar?: "))
            shorts_count.append(cantidad)
            
            for i in shorts_count:
                print(f"{i} shorts agregados")

            for c,v in cat_producto.items():
                if c == producto_1:
                    precio = v

                    #multiplicador = sum(shorts_count)

                    if precio > 0:
                        
                        print(f"El precio por pieza es: ${precio}")
                        subtotal = precio * i
                        sub_totales.append(subtotal)

                        for clave,valor in desc_producto.items():
                            if clave == producto_1 and valor < 0:
                                descuento = subtotal * valor / 100
                                
                                sub_total_desc_camisas.append(descuento)
                                print(f"precio con descuento: {descuento}")
                            else:
                                print(f"No hay descuento el precio es {subtotal}")
                                break
                    else:
                        print("Precio no disponible")

            if producto_1 not in producto_agregado: 
                producto_agregado.append(producto_1)
                print(producto_agregado)


        elif producto_1 == 'JEANS':
            cantidad = int(input("¿Cuántos jeans deseas agregar?: "))
            jeans_count.append(cantidad)
            
            for i in jeans_count:
                print(f"{i} jeans agregados")
            
            for c,v in cat_producto.items():
                if c == producto_1:
                    precio = v

                    #multiplicador = sum(jeans_count)

                    if precio > 0:
                        
                        print(f"El precio por pieza es: ${precio}")
                        subtotal = precio * i
                        sub_totales.append(subtotal)

                        for clave,valor in desc_producto.items():
                            if clave == producto_1 and valor < 0:
                                descuento = subtotal * valor / 100
                                
                                sub_total_desc_camisas.append(descuento)
                                print(f"precio con descuento: {descuento}")
                            else:
                                print(f"No hay descuento el precio es {subtotal}")
                                break
                    else:
                        print("Precio no disponible")

            if producto_1 not in producto_agregado: 
                producto_agregado.append(producto_1)
                print(producto_agregado)

        disparador = input("Deseas agregar un producto? Ingresa (si) o (no): ")


n_camisas_count = []
camisas_count = sum(camisas_count)
n_camisas_count.append(camisas_count)

n_zapatos_count = []
zapatos_count = sum(zapatos_count)
n_zapatos_count.append(zapatos_count)

n_gafas_count = [] 
gafas_count = sum(gafas_count)
n_gafas_count.append(gafas_count)

n_shorts_count = []
shorts_count = sum(shorts_count)
n_shorts_count.append(shorts_count)

n_jeans_count = []
jeans_count = sum(jeans_count)
n_jeans_count.append(jeans_count)

reg_compra = n_camisas_count + n_zapatos_count + n_gafas_count + n_shorts_count + n_jeans_count
#dict_reg_compra = dict(zip(productos,reg_compra))

print("")
print(producto_agregado)
print("Tus compras fuerón: ")
for c,v in zip(producto_agregado,reg_compra):
    print(f"{c}.....{v}, el subtotal = ")

    

print("")    
total_compra = sum(sub_totales)
compra_con_descuento = sum(sub_total_desc_camisas)
tc = total_compra - compra_con_descuento
print(f"Total compra : ${total_compra}")
print(f"Tu ahorro fue: ${compra_con_descuento}")
print(f"Tu compra con descuento fue : ${tc}")



"""
     'Camisa sport' : 200,
    'Zapatos' : 450,
    'Gafas' : 180,
    'Short berm' : 340,
    'Jeans' : 650
"""
        


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