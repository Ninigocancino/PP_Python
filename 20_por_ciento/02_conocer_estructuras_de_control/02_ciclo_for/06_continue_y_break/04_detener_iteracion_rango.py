"""
Nombre del ejercicio: Detener la iteración de un rango

Instrucciones: 
1.- Crea un rango del 0 al 20
2.- Has que el programa se detenga cuando el valor del iterable sea igual a la multiplicación de 2 por 8 
3.- Imprime los elementos antes del break

"""

for i in range(0,20):
    if i == 2*8:
        break
    print(i)
print(f"El break sucede en {i}")