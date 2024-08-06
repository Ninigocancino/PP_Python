"""
NOMBRE DEL PROYECTO:  Calculadora de gastos de viaje 

DESCRICPÓN DEL PROYECTO: 
Supongamos que debes realizar un viaje en automovil de una ciudad 'A' a una ciudad 'B', la ciudad 'A' se encuentra a 80 km de distancia en línea recta, sin embargo ninguno de los dos caminos que conectan ambas ciudades siguen una línea recta perfecta.

En cambio, el camino 1 cuenta con muchas curvas y en total se deben recorrer 130 km para llegar a la ciudad 'B',
por su parte el camino 2 es más directo y solo deben recorrerse 100 km para llegar a la ciudad 'B' pero para tomar
este camino debe pagarse un peaje de $250 para vehiculos pequeños, $350 para vehiculos medianos y $700 para vehiculos pesados.

Como cuentas con presupuesto limitado para este viaje necesitas cuidar al máximo el dinero y economizar.

Haz decidido viajar en un vehículo pequeño que tiene un consumo de 10 litros por kilometro en caminos con pocas curvas
y 18 litros por kilometro en caminos pronunicados o con muchas curvas.

El precio de la gasolina a la fecha de tu salida es de $25 por litro.

INSTRUCCIONES:
Crea un programa sencillo que realice las siguientes acciones:
  1.- Calcula el gasto total de cada opción para elegir el más económico
  2.- Muestra el desarrollo del problema al usuario usando print

"""


print("Datos analisis 1: ")

distancia_1 = 130
c_c_1 = 18
precio_gas = 25

print("")
print(f"Distancia: {distancia_1}")
print(f"Consumo del vehiculo (k/L): {c_c_1}")
print(f"Costo del combustible por litro: {precio_gas}")
print("")


print("Primero debemos calcular el consumo total de combustible:")

consumo_t_1 = c_c_1 * distancia_1

print(f"Para ello multiplicaremos el consumo estimado del vehiculo que es ({c_c_1}) LK por los kilometros del camino 1 que equivalen a: {distancia_1} km")
print(f"Entonces obtenemos como resultado que el consumo total para esta opción es de: {consumo_t_1} litros por kilometro")
print("")

print("Ahora debemos calcular el costo total del viaje")
print(f"Para lo cual debemos simplemente multiplicar el consumo total de combustible durante el viaje por el precio del combustible (en litros) que es de ${precio_gas}")
print("")
gasto_t = consumo_t_1 * precio_gas

print("Datos analisis 2: ")

distancia_2 = 100
c_c_2 = 10
peaje_2 = 250

print("")
print(f"Distancia: {distancia_2}")
print(f"Consumo del vehiculo (k/L): {c_c_2}")
print(f"Costo de peaje: ${peaje_2}")
print(f"Costo del combustible por litro: {precio_gas}")
print("")

print("Calculamos el consumo total de combustible:")

consumo_t_2 = c_c_2 * distancia_2

print(f"Para ello multiplicaremos el consumo estimado del vehiculo que es ({c_c_2}) LK, por los kilometros del camino 2 que equivalen a: {distancia_2} km")
print(f"Entonces obtenemos como resultado que el consumo total para esta opción es de: {consumo_t_2} litros por kilometro")
print("")

print("Ahora debemos calcular costo total del viaje")

gasto_t_2 = consumo_t_2 * precio_gas
gasto_t_2 = gasto_t_2 + peaje_2

print(f"Para lo cual debemos simplemente multiplicar el consumo total de combustible durante el viaje por el precio del combustible (en litros) que es de ${precio_gas} y sumar el costo del peaje del camino")
print("")

print("")
print("De esta forma obtenemos como resultados que ...")
print("")
print(f"El viaje por el camino 1 tendrá un costo total de = ${gasto_t}")
print(f"Y el viaje por el camino 2 tendrá un costo total de  = ${gasto_t_2}")