# -*- coding: utf-8 -*-

"""
Fase 3 - Quiz con estadísticas
Requerimeintos:
- Preguntas almacenadas en diccionarios con categorías
- Sistema de estadísticas por tema
- Validación flexible de respuestas
"""

# Sección 1: Estructura de diccionarios anidados

preguntas = [
    {
        "texto" : "\n1. ¿Qué celebra México el 16 de septiembre?",
        "respuesta" : {"opciones": ["independencia"], "tema": "Historia"},
        "pistas" : ["¡Es un evento patrio!", "Comenzo en 1810"]
    },
    {
        "texto" : "\n2. ¿Cuál es la capital de México?",
        "respuesta" : {"opciones": ["ciudad de méxico", "cdmx"], "tema": "Geografía"},
        "pistas" : ["Tiene un zócalo famoso", "Es la ciudad más grande del país"]
    }
]

# Sección 2: Lógica principal

puntaje = 0
estadisticas = {"Historia": 0, "Geografía": 0}

for pregunta in preguntas:
    texto = pregunta["texto"]
    opciones_validas = pregunta["respuesta"]["opciones"]
    tema = pregunta["respuesta"]["tema"]

    respuesta = input(f"{texto} ").lower().strip()
    if respuesta in opciones_validas:
        print(f"✅ Correcto (+10 puntos) | Tema: {tema}")
        puntaje += 10
        estadisticas[tema] += 1
    else: 
        print(f"❌ Incorrecto. Pista: {pregunta["pistas"][0]}")
        print(f"Respuesta válida: {', '.join(opciones_validas).title()}")


