

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
    print("!Perfecto!")
    print("")
    print("Solo necesitamos unos cuantos datos tuyos")
    print("Empecemos con tu proceso de registro")
    print("")
    print("")
    input("Ingresa un nombre de usuario: ")
    print("")
    input("Elige una contraseña segura [usa: letras mayusculas y minusculas,números,signos especiales]: ")
    print(" ")
    input("Ingresa tu primer nombre: ")
    print(" ")
    print("Ingresa tu segendo nombre *opcional: ")
    print("")
    input("Ingresa tU apellido paterno: ")
    print("")
    input("Ingresa tu apellido materno: ")
    print("")
    input("Ingresa tu número telefónico: ")
    print(" ")
    
elif eleccion == "INSTRUCCIONES":
    print("Mostrar insturcciones")
else:
    exit()