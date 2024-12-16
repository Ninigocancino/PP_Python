"""
Nombre del ejercicio: Emparejar dos listas diferentes tamaños

Instrucciones: 
1.- Crea dos listas relacionadas conceptualmente
2.- Usa el método ZIP para iterarlas simultaneamente. Las listas no deben contener el mismo número de elementos 
3.- Imprime un mensaje que contenga las iteraciones simultaneas

"""

titulos = ['Originales','Hyperfocus','Esencialismo','Repensar la pobreza']
anios = [2014,2017,2019]

for titulo,anio in zip(titulos,anios):
    print(titulo,anio)

