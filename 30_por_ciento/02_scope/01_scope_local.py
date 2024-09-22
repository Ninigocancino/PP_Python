"""
Nombre del ejercicio: Calcular área del circulo

Este ejercicio está enfocado en cómo se manejan las variables locales dentro de una función y cómo no son accesibles fuera de su contexto.

Instrucciones: 
1.- Crea una función que calcule el área de un circulo 
2.- Llama a la función
3.- Imprime un mensaje con el resultado dado por la función 
4.- Intenta acceder a la variable que contiene el valor pi desde fuera de la función ¿Qué sucede cuando intentas imprimir pi fuera de la función? 
"""

def calcular_area_circulo(radio):
    pi = 3.1416  # Variable local, solo visible dentro de la función
    area = pi * radio ** 2
    return area

# Llama a la función con un radio de 5
resultado = calcular_area_circulo(5)
print(f"El área del círculo es: {resultado}")

# Intenta acceder a la variable local 'pi' fuera de la función
#print(pi)  # ¿Qué ocurre aquí?