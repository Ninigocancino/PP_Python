
record = []
respuesta_q1 = "B"

print("¿Cuál es el país más grande del mundo?")
print("Opción A: China")
print("Opción B: Rusia")
print("Opción C: Beirut")
print("")

q1 = input("Ingresa tu respuesta: ").upper()

if q1 == respuesta_q1:
    print("Perfecto has acertado")
    print("Haz ganado 5 puntos")
    pts_q1 = 5
    record.append(pts_q1)
elif q1 == "C":
    print("Bierut, no es un país")
    pts_q1 = 0
    record.append(pts_q1)
elif q1 == "A":
    print("Muy cerca, China es grande pero no es el más grande")
    pts_q1 = 0
    record.append(pts_q1)
else:
    print("Elige una opción valida")
    pts_q1 = 0
    record.append(pts_q1)

print(f"Tu record es de {record} pts")
