"""
Nombre del ejercicio: Crear sub lista de animales

Instrucciones: 
1.- Crea una lista, usa el comando 'Alt + z' para que el editor te muestre el contenido con salto de línea y escribe tres línea con nombres de animales 'agrupandolos' de acuerdo a su tipo.
2.- Imprime el número de elementos de la lista.
3.- Identifica el indice del último animal de cada tipo.
3.- Crea una sublista de animales carnivoros.
4.- Crea una sublista de animales vegetarianos.
"""

animales = ["Perro", "Gato", "Tiburón", "Cocodrilo", "León", "Tigre", "Elefante", "Caballo", "Obeja", "Llama", "Cabra"]

print("")

elementos = len(animales)
print(f"La lista contiene {elementos} elementos")

print("")

carnivoros = animales[0:6]
print(f"Animales carnivoras: {carnivoros}")

vegetarianos = animales[6:]
print(f"Animales vegetarianos: {vegetarianos}")
