"""
Nombre del ejercicio: Traer los valores de un diccionario

Instrucciones: 
1.- Crea un diccionario cualquiera
2.- Recorre los elementos del diccionario
3.- Usa el método values para traer los valores del diccionario
3.- Imprime los valores

"""


vegetacion = {
    'Bugambilia' : 'Flor',
    'Pino' : 'Arbol',
    'Mango' : 'Arbol frutal',
    'Zanahoria' : 'Verdura'
}

for i in vegetacion.values():
    print(i)