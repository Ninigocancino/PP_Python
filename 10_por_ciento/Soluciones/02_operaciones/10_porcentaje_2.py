"""
Nombre del ejercicio: Calcular el porcentaje de una cifra, cuando una 

Instrucciones: Crea un programa que cuando se conoce la cantidad que corresponde a un porcentaje especifico calcule se necesita 
"""

#Se conoce el resultado y la equivalencia, se necesita descubrir la cantidad que representa el 100%
#por ejemplo: 20 pesos es el 20% de una cifra desconocida
cantidad =20
porcentaje = 10
cantidad_desc = (cantidad / porcentaje) * 100 

print(f"cuando {cantidad} es el {porcentaje}%, {cantidad_desc} es el 100% ")
