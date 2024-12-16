"""
Nombre del ejercicio: Traer las claves de un diccionario

Instrucciones: 
1.- Crea un diccionario cualquiera
2.- Recorre los elementos del diccionario
3.- Usa el método keys para traer las claves del diccionario
3.- Imprime las clave

"""

vegetacion = {
    'Bugambilia' : 'Flor',
    'Pino' : 'Arbol',
    'Mango' : 'Arbol frutal',
    'Zanahoria' : 'Verdura'
}

for i in vegetacion.keys():
    print(i)