#Recursos para resolver los ejercicios

lista_ciudades = ['Monterrey','Villehermosa','Oaxaca','La Paz','Méxio','Cancún','Palenque','Veracruz','Madrid','Barcelona','Bilbao','Zaragoza','Merida','León','Ibiza','Tenerife','Londres','Manchester','Liverpol','Bogota','Cali','Medellín','Cartagena','Roma','Milan','Florencia','Venecia','Napoles','Pizza','Turino']

lista_plantas = ['Cebolla','Zanahoria','Papa','Repollo','tomate','aguacate','fresa','uva','mango','platano','Pino','Cedro','Ceiba','caoba','Cecoya','Hule']

#EJERCICIOS

#Ejercicio 01: Imprime en consola el número de elementos contenido en cada lista
elementos_ciudades = len(lista_ciudades)
print("Elementos lista ciudades:")
print(elementos_ciudades)
print("")

elementos_plantas = len(lista_plantas)
print("Elementos lista plantas:")
print(elementos_plantas)
print("")

#Ejercicio 02: Crea una sublista con las ciudades mexicanas contenidas en 'lista_ciudades', después imprime la nueva lista en consola

ciudades_mexicanas = lista_ciudades[0:8]
print("LISTA DE CIUDADES MEXICANAS")
print(ciudades_mexicanas)
print("")

#Ejercicio 03: Crea una sublista con las ciudades italianas contenidas en 'lista_ciudades', después imprime la nueva lista en consola

ciudades_italianas = lista_ciudades[23:]
print("LISTA DE CIUDADES ITALIANAS")
print(ciudades_italianas)
print("")

#Ejercicio 04: Crea una sublista con las frutas contenidas en 'lista_plantas', después imprime la nueva lista en consola

plantas_frutas = lista_plantas[4:9]
print("LISTA DE FRUTAS")
print(plantas_frutas)
print("")

#Ejercicio 05: Crea una sublista con los arboles de 'lista_plantas', después imprime la nueva lista en consola

plantas_arboles = lista_plantas[9:16]
print("LISTA DE ARBOLES")
print(plantas_arboles)
