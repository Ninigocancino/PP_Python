import csv
import os 

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

    comprobador = input("¿Listo para apartar tu lugar? (Sí), (No): ")

    if comprobador == "si":

        data_path = "Datos_Usuario"
        archivo_csv_path = os.path.join(data_path, "data_user.csv" )

        if not os.path.exists(data_path):
            os.makedirs(data_path)

        with open(archivo_csv_path, "a", newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)

            if archivo_csv.tell() == 0:
                encabezados = ["U_nombre","Contrasenia",'P_nombre','S_nombre', "A_paterno", "M_nombre","N_telefonico"]
                escritor_csv.writerow(encabezados)

            while True:

                datos_usuarios = []

                print("!Perfecto!")
                print("")
                print("Solo necesitamos unos cuantos datos tuyos")
                print("Empecemos con tu proceso de registro")
                print("")
                print("")
                u_nombre = input("Ingresa un nombre de usuario: ")
                print("")
                contrasenia = input("Elige una contraseña segura [usa: letras mayusculas y minusculas,números,signos especiales]: ")
                print(" ")
                p_nombre = input("Ingresa tu primer nombre: ")
                print(" ")
                s_nombre = input("Ingresa tu segendo nombre *opcional: ")
                print("")
                a_paterno = input("Ingresa tU apellido paterno: ")
                print("")
                a_materno = input("Ingresa tu apellido materno: ")
                print("")
                n_telefonico = input("Ingresa tu número telefónico: ")
                print(" ")

                escritor_csv.writerow([u_nombre,contrasenia,p_nombre,s_nombre,a_paterno,a_materno,n_telefonico])

                archivo_csv.close()

                print("")
                print("Se agregarón nuevos datos")
                print("")

                datos_usuarios.append([u_nombre,p_nombre,s_nombre,a_paterno,a_materno,n_telefonico])

                print("Se ingresarón los siguientes datos: ")
                print(datos_usuarios)

                break
    
elif eleccion == "INSTRUCCIONES":
    print("Mostrar insturcciones")
else:
    exit()