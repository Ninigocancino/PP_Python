# -*- coding: utf-8 -*-

"""
Fase 5 - Quiz completo
Funcionalidades:
-Preguntas cargadas desde CSV
-Resultados guardados en .txt
-Interfaz con colores
-Temporizador
"""

import csv
import time 
from datetime import datetime 
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Sección 1: Carga de preguntas desde CSV

def cargar_preguntas(archivo_csv="preguntas.csv"):
    """Carga preguntas desde un archivo CSV. Retorna lista de diccionarios."""
    preguntas = []
    try:
        with open(archivo_csv, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Convierte las opciones válidas en lista (ej: "a,b,c" → ["a", "b", "c"])
                opciones = [opcion.strip().lower() for opcion in fila["respuesta"].split(",")]
                preguntas.append({
                    "texto": fila["pregunta"],
                    "respuesta": {"opciones": opciones, "tema": fila["tema"]},
                    "pistas": fila["pistas"].split("|")  # Separa pistas con "|" en el CSV
                })
        return preguntas
    except FileNotFoundError:
        print(Fore.RED + f"⚠️ Error: Archivo '{archivo_csv}' no encontrado.")
        return []
    except Exception as e:
        print(Fore.RED + f"⚠️ Error inesperado: {str(e)}")
        return []
    
# sección 2: Guardar resultados en archivo

def guardar_resultados(puntaje, estadisticas, tiempo_total):
    """Guarda resultados en un archivo .txt con marca de tiempo."""
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("resultados.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"\n=== Resultado del {fecha} ===\n")
        archivo.write(f"Puntaje: {puntaje} puntos\n")
        archivo.write(f"Tiempo: {tiempo_total:.2f} segundos\n")
        archivo.write("Desempeño por tema:\n")
        for tema, datos in estadisticas.items():
            archivo.write(f"- {tema}: {datos['aciertos']}/{datos['total']}\n")

# Sección 3: Ejecución del quiz

def ejecutar_quiz(preguntas):
    estadisticas = {}
    puntaje = 0
    inicio = time.time()  # Inicia el temporizador

    print(Fore.CYAN + "\n¡COMIENZA EL QUIZ! 🚀")
    for pregunta in preguntas:
        tema = pregunta["respuesta"]["tema"]
        if tema not in estadisticas:
            estadisticas[tema] = {"aciertos": 0, "total": 0}
        estadisticas[tema]["total"] += 1

        respuesta = input(Fore.YELLOW + pregunta["texto"] + " ").lower().strip()
        
        if respuesta in pregunta["respuesta"]["opciones"]:
            print(Fore.GREEN + "✅ Correcto (+10 puntos)")
            puntaje += 10
            estadisticas[tema]["aciertos"] += 1
        else:
            print(Fore.RED + f"❌ Incorrecto. Pista: {pregunta['pistas'][0]}")

    tiempo_total = time.time() - inicio  # Calcula tiempo transcurrido
    return puntaje, estadisticas, tiempo_total