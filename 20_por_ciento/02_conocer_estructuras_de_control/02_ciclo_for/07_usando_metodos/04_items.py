"""
Nombre del ejercicio: Ficha de producto

Instrucciones: 
1.- Crea un diccionario que guarde información de un producto
2.- Recorre cada elemento del diccionario
3.- Imprime la clave y el valor de cada elemnto

"""

producto = {
    "Nombre" : "Laptop",
    "Precio" : "12550",
    "Disponibilidad" : True,
    "Caracteristicas" : ["i7", "16GB RAM", "512GB SSD"]
}

for c, v in producto.items():
    print(f"{c}:{v}")