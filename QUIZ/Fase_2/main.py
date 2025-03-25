# -*- coding: utf-8 -*-

"""
Fase 2 - Quiz dinámico 
Novedades:
-Preguntas almacenadas en una lista
-Uso de ciclo for para iterar
-Sistema escalable (añadir preguntas sin facilmente)
"""

# Sección 1: Lista de preguntas 
preguntas = [
    ["\n1. ¿Qué celebra México el 16 de septiembre?", "independencia"],
    ["\n2. ¿Cuál es la capital de México", "ciudad de méxico"],
    ["\n3. ¿Cuál es el animal nacional de México", "águila real"],
    ["\n4. ¿Cuál es el color representativo de México", "rosa mexicano"],
    ["\n5. ¿Cuál es la comida más conocida de Méxio", "tacos"]
]

# Sección 2: Lógica principal
puntaje = 0

print("Bienvenido al Quiz. Ahora es dinámico! 🚀\nResponde las siguientes preguntas: ")

for pregunta in preguntas:
    texto_pregunta = pregunta[0]
    respuesta_correcta = pregunta[1]

    respuesta = input(texto_pregunta + " ").lower().strip()

    if respuesta == respuesta_correcta:
        print("✅ ¡Correcto! + 10 puntos")
        puntaje +=10
    else: 
        print(f" Incorrecto. La respuesta es: {respuesta_correcta.title()}")

#Sección 3: Mostrar resultados

total_preguntas = len(preguntas)
print(f"\n⭐ Puntaje final: {puntaje}/{total_preguntas * 10}")