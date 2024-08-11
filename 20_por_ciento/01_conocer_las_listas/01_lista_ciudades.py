"""
Nombre del ejercicio: Crear sub lista de ciudades de paises 

Instrucciones: 
1.- Crea una lista, usa el comando 'Alt + z' para que el editor te muestre el contenido con salto de línea y escribe tres línea con nombres de ciudades 'agrupandolas' por el país al que pertenecen.
2.- Imprime el número de elementos de la lista.
3.- Identifica el indice de la última ciudad de cada país.
3.- Crea una sublista de ciudades mexicana.
4.- Crea una sublista de ciudades italianas.
5.- Crea una sublista de ciudades francesas
"""

lista_ciudades = ['Monterrey','Villehermosa','Oaxaca','La Paz','Méxio','Cancún','Palenque','Veracruz','Madrid','Barcelona','Bilbao','Zaragoza','Merida','León','Ibiza','Tenerife','Londres','Manchester','Liverpol','Bogota','Cali','Medellín','Cartagena','Roma','Milan','Florencia','Venecia','Napoles','Pizza','Turino', 'Paris','Lyon','Marsella','Monaco','Dunkerque', 'Burdeos']

elementos = len(lista_ciudades)
print(f"Lista ciudades contiene: {elementos} elementos")

ciudades_mexico = lista_ciudades[0:7]
print(ciudades_mexico)

ciudades_italia = lista_ciudades[24:30]
print(ciudades_italia)

ciudades_francia = lista_ciudades[30:]
print(ciudades_francia)