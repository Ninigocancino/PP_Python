"""
INFORMACIÓN DEL PROYECTO:

Nombre del Proyecto: Inventario Total

Descripción:
Crearemos un programa que permita controlar el inventario de un grupo comercial cuya principal línea de negocios son los supermercados y tiendas de conveniencia. Esta empresa distribuye los diferentes articulos de su stock desde su centro logístico a los almacenes insitu de cada sucursal de las distintas marcas que forman parte del grupo. El grupo comercial esta creciendo rápidamente y quiere digitalizar cada parte del negocio, pues aún no cuenta cuenta con una infraestructura digital que le permita ser competitivo con empresas de mayor tamaño. El gerente de logistica te ha contratado para que crear un programa que le ayude a controlar mejor el inventario y que pueda hacer más eficiente toda la operación del departamente y facilitar la entrega de información a otros departamentos relacionados. 

Instrucciones:
Se requiere que el proyecto se aborde por bloques de funcionalidades para poder detectar errores e incorporar mejoras de forma más ágil y esbelta.

Caso de uso:
Se quiere desarrollar el proyecto partiendo de la interacción con una de las tiendas más pequeñas y de menor volumen de ventas para establecer un entorno controlado, para evitar un consumo innecesario de recursos para este proyecto. Por lo que el primer paso es notificar al gerente de la tienda las ruebas que se estrán realizando.

Historia de usuario:
Cómo gerente de sucursal necesito tener información general del programa que me permita saber que acciones debo realizar para poder usarlo o cuál es la razón para hacerlo


Criterios de calidad:
Crear un programa sencillo que realice las siguientes acciones: 
1.- El programa debe imprimir un mensaje de bienvenida
2.- El programa debe debe imprimir una descripción del programa
3.- El programa debe debe imprimir al menos dos de las instrucciones del programa
4.- Los textos deben mostrarse de forma amigable para facilitar al usuario su lectura 
5.- El programa debe mostrar al usuario un ejemplo sencillo de la utilidad que tendrá el programa, mostrando la reducción del stock con una compra.
6.- El programa debe mostrar la información de la transacción de forma desglosada
7.- El programa debe mostrar un mensaje de despedida antes de cerrarse
"""

# Agrega formato a la entrada del programa

print("")

print("_"*60)

print("")
print("*"*20,"INVENTARIO TOTAL","*"*20)
print(" "*12,"Bienvenido, a tu sistema")

print("")

print("-"*13, "Antes de empezar:","-"*13)
print("")
print(" "*4,"¿Qué es Inventario Total?:")
print(" "*4,"En Grupo SuperTiendas queremos ayudarte a hacer tu trabajo mucho más fácil \n     y que puedas dedicar más tiempo a tu desarrollo como parte importante de nuestro negocio. \n     Con Inventario Total podrás gestionar la hasta ahora tediosa tarea de administrar el almacen \n     con un sistema inteligente, digital y nuy sencillo de usar")
print("")

print(" "*4,"Mira lo que podrás hacer con tu sistema...")

print(" ")

articulo = 'camisas de playa'
unidad = "piezas"
cantidad = 3000
venta_fecha01 = 10
venta_fecha02 = 0
venta_fecha03 = 3
venta_fecha04 = 5
venta_fecha05 = 6
venta_fecha06 = 2
venta_fecha07 = 8
venta_fecha08 = 4

ventas_totales = venta_fecha01 + venta_fecha02 + venta_fecha03 + venta_fecha04 + venta_fecha05 + venta_fecha06 + venta_fecha07 + venta_fecha08

existencia = cantidad - ventas_totales

print(" "*4,f"Supongamos que tienes {cantidad} {unidad} de {articulo} en el almacen pero has vendido...")
print(" "*4,f"Un lunes {venta_fecha01} {articulo}, un miércoles {venta_fecha02} {articulo}, un sábado {venta_fecha03} {articulo}")
print(" "*4,f"Un martes de otra semana {venta_fecha04} {articulo}, un jueves de esa semana {venta_fecha05} {articulo}, un sábado de esa semana {venta_fecha06} {articulo}")
print(" "*4,f"y luego jueves de una tercer semana {venta_fecha07} {articulo}, y un viernes de una cuarta semana {venta_fecha08} {articulo}")
print("")
print(" "*4,f"Saber cuantas {articulo} nos quedan el el almacen de forma rápida sería muy dificil, \n     tomando en cuenta que además hay que hacer lo mismo para mucho otros articulos")
print("")
print(" "*4,"En cambio con INVENTARIO TOTAL puedes saber en tiempo real que ...")
print("")

print(" "*4,f"Se han vendido {ventas_totales} {articulo}")
print(" "*4,f"y quedan en existencia {existencia} {articulo}")
print(" "*4,f"por lo que no es necesario comprar más {articulo}")

print("")

print(" "*4,"Iniciamos?")