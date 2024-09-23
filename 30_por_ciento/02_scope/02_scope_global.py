"""
Nombre del ejercicio: Contador de llamadas

En este ejercicio, trabajarás con variables globales, observando cómo se comportan dentro y fuera de las funciones, y cómo puedes modificarlas usando la palabra clave global.

Instrucciones: 
1.- Crea una variable iniciada en 0
2.- Usa 'global' para referenciar la variable en el scope global
3.- Crea una función en la que se incremente el valor de una variable determinada creada fuera de la función
4.- Llama a la función
5.- Imprime un mensaje que imprima e valor final de la variable
"""

contador_llamadas = 0  # Variable global

print("")
print(f"Contador antes de ejecutar función {contador_llamadas}")
print("")

def incrementar_contador():
    global contador_llamadas  # Hacemos referencia a la variable global
    contador_llamadas += 1
    print(f"Contador dentro de la función: {contador_llamadas}")

# Llamamos varias veces a la función
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Verificamos el valor final de la variable global
print("")
print(f"Contador fuera de la función: {contador_llamadas}")