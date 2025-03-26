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