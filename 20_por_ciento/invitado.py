
invitados = ["Luis", "Maria", "Isabel", "Gabriel", "Isaac"]

tu_nombre = input("¿Cuál es tu nombre?: ")


if tu_nombre in invitados:

    anfitriones = ["Zara", "Sofia", "Mateo"]

    invitacion = input("¿QWuién te invitó?: ")

    if invitacion in anfitriones:

        print(f"Bienvenido! {invitacion} te espera adentro, disfruta la reunión ")

    else:
        print(f"Por favor espere un momento, debemos confirmar un dato con {invitacion}")

else:
    print("Lo siento no estás en la lista")