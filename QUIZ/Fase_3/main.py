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
    },
    {
        "texto": "\n3. ¿En qué año llegó el hombre a la luna?",
        "respuesta" : {"opciones": ["1969"], "tema": "Historia"},
        "pistas" : ["Fue en la decada de los 60s", "Apolo 11"]
     }
]

# Sección 2: Lógica principal

puntaje = 0
estadisticas = {}

for pregunta in preguntas:
    tema = pregunta["respuesta"]["tema"]

    if tema not in estadisticas:
        estadisticas[tema] = {"aciertos": 0, "total": 0}
    estadisticas[tema]["total"] += 1

print("¡Bienvenido al Quiz con Estadísticas! 📊\nResponde las siguientes preguntas:")

for pregunta in preguntas:
    texto = pregunta["texto"]
    opciones = pregunta["respuesta"]["opciones"]
    tema = pregunta["respuesta"]["tema"]

    respuesta = input(f"{texto} ").lower().strip()

    if respuesta in opciones:
        print(f"✅ Correcto (+10 puntos) | Tema: {tema}")
        puntaje += 10
        estadisticas[tema]["aciertos"] += 1
    else:
        print(f"❌ Incorrecto. Pista: {pregunta['pistas'][0]}")

# Seccción 3: Manejo de dicionarios para generar un reporte final

print(f"\n ⭐ Puntaje final: {puntaje}/{len(preguntas) * 10}")

print("\n🏅 Desempeño por tema: ")
for tema, datos in estadisticas.items():
    aciertos = datos["aciertos"]
    total_tema = datos["total"]
    porcentaje = (aciertos / total_tema) *100 if total_tema > 0 else 0
    print(f"- {tema}: {aciertos}/{total_tema} ({porcentaje:.1f}%)")


