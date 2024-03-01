#Supongamos que tienes una mochila y necesitas ingresar todo lo necesario para tus clases del día


mochila = []


while True:

    ingresar = input("Agrega algo a la mochila: ")

    if ingresar != "":
        mochila.append(ingresar)
        
        for i in mochila:
            print(i)
    else:
        print("Cerrar mochila")
        break