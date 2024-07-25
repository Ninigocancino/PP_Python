
record = []
respuesta_q1 = "B"
respuesta_q2 = "C"

print("¿Cuál es el país más grande del mundo?")
print("Opción A: China")
print("Opción B: Rusia")
print("Opción C: Beirut")
print("")

q1 = input("Ingresa tu respuesta: ").upper()

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


print("¿Cuál es el país que limita al sur con los E.U.A.?")
print("Opción A: China")
print("Opción B: Rusia")
print("Opción C: México")
print("")

q2 = input("Ingresa tu respuesta: ").upper()

if q2 == respuesta_q2:
    print("Perfecto has acertado")
    print("Haz ganado 1 punto")
    pts_q1 = "C"
    record.append(pts_q1)
elif q1 == "A":
    print("China, no se encuentra al sur de E.U.A.")
elif q1 == "B":
    print("Rusia está cerca de E.U.A, pero no al sur")
else:
    print("Elige una opción valida")

puntos = len(record)

print(f"Tu record es de {puntos} pts")
