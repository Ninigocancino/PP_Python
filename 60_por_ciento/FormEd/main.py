
print((" ") * 48, "FormEd")
print("")
print((" ") * 32, "Aparta tu lugar en nuestro próximo Curso:")
print((" ") * 26, "Curso Básico de Transformación Digital para Negocios")
print("")
print((" ") * 28, "¿Qué quieres hacer? (escribe la opción deseada)")
print((" ") * 27, "[INSCRIBIRME]", (" ") * 5, "[SALIR]", (" ") * 5, "[INSTRUCCIONES]")

print(" ")
eleccion = input("Ingresa tu eleccion: ").upper()
if eleccion == "INSCRIBIRME":
    print("Generar formulario de inscripción")
elif eleccion == "INSTRUCCIONES":
    print("Mostrar insturcciones")
else:
    exit()