"""
Nombre del ejercicio: Emparejar dos listas

Instrucciones: 
1.- Crea dos listas relacionadas conceptualmente
2.- Usa el método ZIP para iterarlas simultaneamente. Las listas deben contener el mismo número de elementos (al menos tres por cada listas)
3.- Imprime un mensaje que contenga las iteraciones simultaneas

"""

lista_nombres = ["Laura","Fernanda", "Mara"]
edades = [20,35,19]

for nombre,edad in zip(lista_nombres,edades):
    print(f"{nombre} tiene: {edad}")