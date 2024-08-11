"""
Nombre del ejercicio: Crear sub lista de plantas

Instrucciones: 
1.- Crea una lista, usa el comando 'Alt + z' para que el editor te muestre el contenido con salto de línea y escribe tres línea con nombres de plantas 'agrupandolos' de acuerdo a su tipo.
2.- Imprime el número de elementos de la lista.
3.- Identifica el indice de la última última planta de cada tipo.
3.- Crea una sublista de plantas que son arboles.
4.- Crea una sublista de plantas que son vegetales.
"""

plantas = ["Roble", "Pino", "Eucalipto", "Nogal", "Manzano", "Pera", "Cerezo", "Naranjo", "Limonero", "Olivo", "Castaño", "Haya", "Arce", "Abedul", "Cedro","Manzana", "Pera", "Cereza", "Naranja", "Limón", "Banana", "Uva", "Fresa", "Frambuesa", "Mora", "Melón", "Sandía", "Piña", "Mango", "Kiwi","Lechuga", "Tomate", "Pepino", "Zanahoria", "Cebolla", "Pimiento", "Brócoli", "Coliflor", "Espinaca", "Ajo", "Patata", "Calabacín","Rosa", "Lavanda", "Jazmín", "Azalea", "Camelia", "Rododendro", "Hibiscus", "Boj"]


print("")
elementos_lista = len(plantas)
print(f"La lista tiene {elementos_lista} elementos")
print("")


arboles = plantas[0:14]
print(arboles)
print("")


vegetales = plantas[32:41]
print(vegetales)
print("")