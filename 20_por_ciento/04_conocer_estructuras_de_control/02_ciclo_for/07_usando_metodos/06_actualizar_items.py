"""
Nombre del ejercicio: Actualizar precio de productos

Instrucciones: 
1.- Crea un diccionario con productos y su precio
2.- Recorre los elementos del diccionario
3.- Usa el método items para hacer que el precio de los productos se actualice a razon deun incremento de 2 veces su valor actual
3.- Imprime los productos con sus recios actualizados

"""

productos = {
    'jamón' : 45,
    'leche' : 30,
    'zanahoria': 15
}

for producto,cantidad in productos.items():
    productos[producto] = cantidad * 2

for n, i in productos.items():
    print(f"{n},{i}")