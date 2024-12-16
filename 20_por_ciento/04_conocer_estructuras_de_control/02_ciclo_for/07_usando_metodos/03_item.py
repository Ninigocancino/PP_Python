"""
Nombre del ejercicio: Traer clave y valor

Instrucciones: 
1.- Crea un diccionario 
2.- Recorre cada elemento del diccionario
3.- Imprime la clave y el valor de cada elemnto

"""

lugar = {
    'Venecia' : 'ciudad',
    'Saturno' : 'planeta',
    'Atlnatida' : 'mito'
}

for k,v in lugar.items():
    print(f"Clave: {k}, Valor: {v}")