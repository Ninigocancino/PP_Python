# -*- coding: utf-8 -*-

"""
Fase 4: Quiz Modularizado
Requisitos: 
-Código organizado en funciones
-Manejo de errores en inputs
-Sistema de reintentos
"""

# Sección 1: Creación de funciones principales

def cargar_preguntas():
    return [

        #Retorna preguntas desde una lista
        
        {
            "texto" : "\n1. ¿Qué celebra México el 16 de septiembre?",
            "respuestas" : {"opciones": ["independencia"], "tema": "Historia"},
            "pistas" : ["¡Es un evento patrio!", "Comenzó en 1810"]
        },
    ]