
print("Veamos si tu calificación es aprovatoria")

entrada = float(input("Ingresa tu calificació: "))

if entrada == 10:
    print("Tu calificación es perfecto")
elif entrada >= 8 and entrada < 10:
    print("Puedes mejorar")
elif entrada < 8:
    print("Necesitas practicar más")