"""
Nombre del ejercicio: Ordena los nombres de una lista

Instrucciones: 
1.- Crea una lista con nombres
2.- Recorre los elementos de la lista
3.- Usa el método sorted para ordenar los elementos de la A a la Z
3.- Imprime los nombres

"""

nombres = ['Zara','Lucas', 'Felipe', 'Armando','Tristan','Leticia','Silas','Mauricio','Juvenal']

print("Contenido de la lista:")
print(nombres)
print("")
print("ASCENDENTE POR DEFAULT")
for i in sorted(nombres):
    print(i)

print("")
print("DESCENDENTE")
for i in sorted(nombres, reverse=True):
    print(i)