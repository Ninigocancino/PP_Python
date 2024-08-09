"""
Nombre del ejercicio: Consultar lista de frutas

Instrucciones: 
1.- Crea una lista, usa el comando 'Alt + Z' para que el editor te muestre el contenido con salto de línea y escribe dos líneas con nombres de frutas sin importar el tipo.
2.- Imprime el contenido de la lista.
3.- Descurbe cuál es el número total de elementos que contiene la lista
4.- Descubre que fruta se encunetra en la posiciones 10, luego imprime el resultado acompañado de un mensaje descriptivo en el que uses la interpolación 
"""

lista_frutas = ['Guanabana','Manzana','Pera','Cereza','Fresa','Uva','Melon','Sandía','Coco','Mango','Pitahaya','Tuna','Tomate','Aguacate','Guayaba','Piña','Papaya','Zapote', 'Kiwi', 'Zapote','Higos','Mamey','Rambutan','Nance','Naranja','Limón','Lima','Platano']



print(f"El contenido de la lista frutas es: {lista_frutas}")
print("")



conteo_frutas = len(lista_frutas)
print(f"El número de elementos en lista frutas es: {conteo_frutas}")

print("")

fruta_desconocida = lista_frutas[10]
print(f"La fruta desconocida es {fruta_desconocida}")
print("")