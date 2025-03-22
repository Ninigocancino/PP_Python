# -*- coding: utf-8 -*-  
"""
QUIZ ESTÁTICO - FASE 1 (10% dominio Python)
Propósito: Evaluar conocimientos básicos de primaria en historia, geografía y ciencias
Audiencia: Niños de 6-12 años
Característica clave: Retroalimentación inmediata con emojis
"""

# Sección 01: Declaración de variables iniciales
puntaje = 0

mensaje_bienvenida = (
    "\n¡Bienvenido al Quiz de la Escuela Patria México! 🌟\n"
    "Responde las siguientes 5 preguntas:\n"
)

# Sección 02: Interfaz 

print(mensaje_bienvenida)

#Pregunta 1 - Historia 
#-------------------------------------------------------------
respuesta_1 = input("\n1. ¿Qué celebra México el 16 de septiembre?: ")

if respuesta_1.lower() == "dia de la independencia":
    print("✅ ¡Correcto! +10 puntos")
    puntaje += 10
else:
    print("❌ Incorrecto. La respuesta es 'dia de la independencia'")

#Pregunta 2 - Geografía
#------------------------------------------------------------
respuesta_2 = input("\n2. ¿Cuál es la capital de México?: ")

if respuesta_2.lower() in ["ciudad de méxico", "cdmx", "méxico df"]:
    print("✅ ¡Excelente! +10 puntos")
    puntaje += 10
else:
    print("❌ Incorrecto. Es 'Ciudad de México'")