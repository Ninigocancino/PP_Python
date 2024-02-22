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
    
    #Creación de la cuenta del usuario

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

                if u_nombre != "" and p_nombre != "" and s_nombre != "" and a_paterno != "" and a_materno != "" and n_telefonico != "":
                    print("Se ha realizado el registro exitoso de los siguientes datos: ")
                    print(f"Nombre de usuario: {u_nombre}")
                    print(f"Primer nombre: {p_nombre}")
                    print(f"Segundo nombre: {s_nombre}")
                    print(f"Apellido paterno: {a_paterno}")
                    print(f"Aperllido materno: {a_materno}")
                    print(f"Telefono: {n_telefonico}")

                break

            print("")
            print("Ahora apartemos tu lugar en el curso")
            print("")

            print("Fechas disponibles: ")
            print(" Grupo: 1, 10 de marzo de 2024")
            print(" Grupo: 2, 20 de marzo de 2024")
            print(" Grupo: 3, 05 de abril de 2024")
            print("")

            fecha_elegida = int(input("Ingresa el número del grupo al que deseas inscribite: "))

            print("")
            print("Ahora elige el horario deseado")
            print("")

            print(" A, 08:00 am -> 10:00 am")
            print(" B, 12:00 pm -> 02:00 pm")
            print(" C, 06:00 pm -> 08:00 pm")
            print("")

            horario_elegido = input("Ingresa el número del horario en el que deseas inscribirte: ")

            print("")

            data_path_2 = "Datos_cursos"          

            if not os.path.exists(data_path_2):
                os.makedirs(data_path_2)

            if fecha_elegida == 1 and horario_elegido == "A":
                name_file = "G1A_Curso_01_inscripicones.csv"
                    
                archivo_csv_path_2 = os.path.join(data_path_2, name_file)

                with open(archivo_csv_path_2, 'a', newline='') as archivo_csv_2:
                        escritor_csv_2 = csv.writer(archivo_csv_2)
                        
                        if archivo_csv_2.tell() == 0:
                            encabezados_curso_01 = ["usuario", "Nombre", "Forma_pago"]
                            escritor_csv_2.writerow(encabezados_curso_01)
                            
                        while True:
                            ins_user = input("Ingresa tu usuario por favor: ")
                            ins_nombre = input("Ingresa tu nombre: ")
                            print("¿Cémo deseas pagar tu inscripción?")
                            print("En línea con tarjeta de credito [pulsa 1]")
                            print("En efectivo [pulsa 2]")

                            f_pago = input("Ingresa tu forma de pago: ")
                            escritor_csv_2.writerow([ins_user,ins_nombre, f_pago])

                            archivo_csv_2.close()

                            print("Felicidades has apartado tu lugar")
                            print("")

                            print("Debes completar tu registro antes del 08 de marzo")
                            print("")

                            print("Datos del curso \n Fecha: 10 de marzo \n Ubicación: Online")

                            break

            elif fecha_elegida == 1 and horario_elegido == "B":
                name_file = "G1B_Curso_01_inscripicones.csv"
                            
                archivo_csv_path_2 = os.path.join(data_path_2, name_file)

                with open(archivo_csv_path_2, 'a', newline='') as archivo_csv_2:
                        escritor_csv_2 = csv.writer(archivo_csv_2)

                        if archivo_csv_2.tell() == 0:
                            encabezados_curso_01 = ["usuario", "Nombre", "Forma_pago"]
                            escritor_csv_2.writerow(encabezados_curso_01)
                            
                        while True:
                            ins_user = input("Ingresa tu usuario por favor: ")
                            ins_nombre = input("Ingresa tu nombre: ")
                            print("¿Cémo deseas pagar tu inscripción?")
                            print("En línea con tarjeta de credito [pulsa 1]")
                            print("En efectivo [pulsa 2]")

                            f_pago = input("Ingresa tu forma de pago: ")
                            escritor_csv_2.writerow([ins_user,ins_nombre, f_pago])

                            archivo_csv_2.close()

                            print("Felicidades has apartado tu lugar")
                            print("")

                            print("Debes completar tu registro antes del 08 de marzo")
                            print("")

                            print("Datos del curso \n Fecha: 10 de marzo \n Ubicación: Online")


                            break




elif eleccion == "INSTRUCCIONES":
    print("Mostrar insturcciones")
else:
    exit()