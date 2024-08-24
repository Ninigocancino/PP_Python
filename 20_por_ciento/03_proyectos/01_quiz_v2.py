"""
Nombre del proyecto: Quiz V_02

Instrucciones:

Ahora que hemos mostrado al usuario lo que puede hacer con nuestro programa añadiremos una nueva capa de complejidad a nuestro Quiz, por lo que agregaremos a nuestro programa nuestras primeras dos preguntas con opciones múltiples, deberemos utilizar estructura de control para indicar al programa que hacer cuándo la respuesta es correcta, cuando es incorrecta o cuando no es una opción valida 

Criterios de calidad:
1.- El programa debe permitir la interacción con el usuario 
2.- El programa debe incorparar al menos un manejo de errores
3.- El programa debe permitir que el usuario sume puntos por cada respuesta correcta. La solución del código puede ser elemental o poco sofisticada.
4.- El programa debe mostrar al usuario los puntos acumulados

"""


#Muestra en pantalla las instrucciones del programa 
print("")
print("_"*60)

print("")
print("*"*20,"QUIZ V_01","*"*20)
print(" "*16,"Bienvenido, juguemos")

print("")

print("-"*18, "Instrucciones","-"*18)
print("")
print(" "*4,"01 Ingresa iniciar")
print(" "*4,"02 Responde las reguntas para ganar puntos")
print("")

print("_"*60)
print("")



#Guarda una lista vacia que recibirá las respuestas ingresadas por el usuario
record = []

#Guardan las respuestas correctas a cada una de las preguntas
respuesta_q1 = "B"
respuesta_q2 = "C"

#Muestra en pantalla la información relacionada con la pregunta número 1 del quiz
print("¿Cuál es el país más grande del mundo?")
print("Opción A: China")
print("Opción B: Rusia")
print("Opción C: Beirut")
print("")

#Permite al usuario ingresar datos para interactuar con el programa
q1 = input("Ingresa tu respuesta: ").upper() 

#Con las estructuras if,elif,else evaluamos si el usuario ha ingresado una respuesta valida 
if q1 == respuesta_q1:
    print("Perfecto has acertado")
    print("Haz ganado 1 punto")
    pts_q1 = "C"
    record.append(pts_q1)
elif q1 == "B":
    print("Bierut, no es un país")
elif q1 == "A":
    print("Muy cerca, China es grande pero no es el más grande")
else:
    print("Elige una opción valida")

#Se imprime la información relacionada con la pregunta número 2 del quiz
print("¿Cuál es el país que limita al sur con los E.U.A.?")
print("Opción A: China")
print("Opción B: Rusia")
print("Opción C: México")
print("")

#Permite al usuario ingresar datos para interactuar con el programa
q2 = input("Ingresa tu respuesta: ").upper()


#Con las estructuras if,elif,else evaluaremos si el usuario a ingresado una respuesta valida y se agrega la letra de la opción a la lista record de ser correcta
if q2 == respuesta_q2:
    print("Perfecto has acertado")
    print("Haz ganado 1 punto")
    pts_q2 = "C"
    record.append(pts_q2)
elif q2 == "A":
    print("China, no se encuentra al sur de E.U.A.")
elif q2 == "B":
    print("Rusia está cerca de E.U.A, pero no al sur")
else:
    print("Elige una opción valida")

#Se cuentan los elementos contenidos en la lista
puntos = len(record)

#Se imprime la retroalimentación para el usuario
print(f"Tu record es de {puntos} pts")

"""
En esta solución se ha optado por abordar la lógica del programa de forma sencilla en la que cada vez que el usuario responde de forma correcta una de las preguntas del quiz el rograma 'toma' la opción correcta y la agrega a la lista vacia 'record', después el programa cuenta los elementos, en este enfoque cada respuesta correcta aporta 1 punto, al final el conteo de elementos en la lista es equivalente al numero de respuestas correctas donde cada una aporta un punto y final muestra un mensaje de retroalimentación para el usuario donde se incluye el puntaje obtenido.  
"""
