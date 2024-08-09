"""
Nombre del ejercicio: Consultar lista de ciudades

Instrucciones: 
1.- Crea una lista, usa el comando 'Alt + z' para que el editor te muestre el contenido con salto de línea y escribe tres línea con nombres de ciudades sin importar el país o continente al que pertenezcan.
2.- Imprime el contenido de la lista.
3.- Descurbe cuál es el número total de elementos que contiene la lista
4.- Descubre que ciudades se encunetran en las posiciones 3, 8 y 13, luego imprime el resultado acompañado de un mensaje descriptivo en el que uses la interpolación 
"""

lista_ciudades = ['México','Lisboa','San Fracisco','Monterrey','Bogota','Madrid','Barcelona','París','Berlin','Pekin','Manila','Alejandría', 'Caracas','Toronto','Buenos Aires', 'Montevideo','Cancún','Ciudad del Cabo','Londres','Río de Janeiro','Tokio','Monaco','Playa del Carmen', "San Petersburgo","Tijuana",'Houston','Nogales','Guaimas', 'Zapopan', 'Belfast','San Salvador','San José']

print(f"El contenido de la lista ciudades es: {lista_ciudades}")
print("")


conteo_ciudades = len(lista_ciudades)
print(f"El número de elementos en lista ciudades es: {conteo_ciudades}")
print("")


ciudad_desconocida_1 = lista_ciudades[3]
ciudad_desconocida_2 = lista_ciudades[8]
ciudad_desconocida_3 = lista_ciudades[13]

print(f"La ciudad en la posición 3 es: {ciudad_desconocida_1}, la ciudad en la posición 8 es: {ciudad_desconocida_2} y la ciudad en la posición 15 es: {ciudad_desconocida_3}")
print("")