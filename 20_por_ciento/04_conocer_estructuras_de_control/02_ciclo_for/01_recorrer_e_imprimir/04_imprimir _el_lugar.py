"""
Nombre del ejercicio: Imprime el lugar

Instrucciones: 
1.- Crea un diccionario de donde la claves sean  'País' y 'ciudad' respectivamente.
2.- Usa un ciclo for para recorrer cada elemento del diccionario.
3.- Imprime los valores del diccionario para indicar el par ciudad país

"""

lugar = {'Ciudad':'Ciudad de México', 'País' : 'México'}

print("*"*20)
print("EJERCICIO 04: IMPRIME EL LUGAR")


for valor in lugar.values():
    print(valor)
