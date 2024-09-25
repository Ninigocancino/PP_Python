"""
Nombre del ejercicio: Shadowing

Instrucciones: 
1.- Crea una variable global
2.- Crea una función que defina una variable con el mismo nombre que la variable global. 

"""

y = 200  # Variable global

def prueba_shadowing():
    y = 50  # Variable local que "sombra" la variable global
    print(f"Valor de 'y' dentro de la función: {y}")

prueba_shadowing()
print(f"Valor de 'y' fuera de la función: {y}")
