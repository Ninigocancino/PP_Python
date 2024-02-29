"""
Supongamos que debes realizar un viaje en automovil de una ciudad 'A' a una ciudad 'B', laciudad 'A' se encuentra a 80 km de distancia 
en línea recta, sin embargo ninguno de los dos caminos que conectan ambas ciudades siguen una línea recta perfecta.
En cambio el camino 1 cuenta con muchas curvas y en total se deben recorrer 130 km para llegar a la ciudad 'B',
por su parte el camino 2 es más directo y solo deben recorrerse 100 km para llegar a la ciudad 'B' pero para tomar
este camino debe pagarse un peaje de $250 para vehiculos pequeños, $350 para vehiculos medianos y $700 para vehiculos pesados.

Como cuentas con presupuesto limitado para este viaje necesitas cuidar al máximo el dinero y economizar.

Haz deicidido viajar en un vehiculo pequeño que tiene un consumo de 10 litros por kilometro en caminos con pocas curvas
y 18 litros por kilometro en caminos pronunicados o con muchas curvas.

El precio de la gasolina a la fecha de tu salida es de $25 por litro.

"""

#Calcula el gasto total de cada opción para elegir el más económico
#Muestra eld esarrollo del problema al usuario usando print


print("Datos analisis 1: ")

distancia_1 = 130
c_c_1 = 18
precio_gas = 25

#Calcular el consumo total

consumo_t_1 = c_c_1 * distancia_1
print(consumo_t_1)

#Calcular costo total:

gasto_t = consumo_t_1 * precio_gas

print("Datos analisis 2: ")

distancia_2 = 100
c_c_2 = 10
peaje_2 = 250

#Calcular el cnsumo total de combustible:

consumo_t_2 = c_c_2 * distancia_2
print(consumo_t_2)

#Calcular costo total:

gasto_t_2 = consumo_t_2 * precio_gas
gasto_t_2 = gasto_t_2 + peaje_2

print("")
print("Resultados")
print("")
print(f"Camino 1 = {gasto_t}")
print(f"Camino 2 = {gasto_t_2}")