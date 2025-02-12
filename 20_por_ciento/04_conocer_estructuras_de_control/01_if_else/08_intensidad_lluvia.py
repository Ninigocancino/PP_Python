
#Determina si la lluvia ha sido intensa, leve o moderada

cantidad_precipitacion = float(input("Ingresa la cantidad de lluvia que a caido (expresala en mm) en tu área: "))

tiempo_lluvia = float(input("Ahora ingresa el tiempo, expresado en horas, que duro la precipitación: "))

intensidad =  cantidad_precipitacion / tiempo_lluvia

if intensidad >= 30:
    print(f"La intensidad de la lluvia fue {intensidad}mm/hora")
    print("Por lo que la lluvia fue intensa")
elif intensidad >= 15 and intensidad <30:
    print(f"La intensidad de la lluvia fue {intensidad}mm/hora")
    print("Por lo que la lluvia fue moderada")
elif intensidad > 0 and intensidad < 15:
    print(f"La intensidad de la lluvia fue {intensidad}mm/hora")
    print("Por lo que la lluvia fue leve")
else:
    print(f"La intensidad de la lluvia fue {intensidad}mm/hora")
    print("Por lo que podemos decir que no llovio")