"""
Nombre del ejercicio: ¿Cómo está el clima hoy?

Instrucciones: 
1.- Crea un programa que pida al usuario la temperatura y devuelva un recomendación con base en el dato ingresado


"""

print("EJERCICIO '¿Cómo está el clima hoy' ")

temp = float(input("Ingresa la temperatura actual(grados centigrados): "))

if temp < 0:
    print("Hace demasiado frio, no salgas a esta temperatura se congela el agua")
elif temp >= 0 and temp <= 10:
    print("Hace mucho frío, asegurate de abrigarte muy bien")
elif temp >10 and temp <= 20:
    print("Esta templado pudes salir, pero no olvides un abrigo ligero")
elif temp >20 and temp <= 24:
    print("El clima esta fresco puedes salir con ropa ligera")
elif temp >24 and temp <= 30:
    print("Es caluroso procura usar ropa comoda y tomar agua")
else:
    print("Es demasiado caluroso, no te expongas al sol y toma mucha agua")