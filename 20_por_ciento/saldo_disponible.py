#_________________________________PROYECTO: CONTADOR DE SALDO DISPONIBLE________________________________

#-------INSTRUCCIONES:
        #Utiliza los conceptos que has aprendido en los directorios anteriores para resolver el problema siguiente.

        #PROBLEMA: Supón que quieres tener un mayor control de tus gastos para cuidar tu dinero, por lo que decides crear un programa que te ayude a cuidar tu dinero el programa te permite establecer un tope de gastos al enviarte un mensaje de advertencia cuando tus gastos han superado un monto establecido previamente por ti


print(" ")
print((("-")*10),("CONTROLA TUS GASTOS"),(("-")*10))
print("Bienvenido a tu controlador de gastos, por favor sigue las instrucciones")
print("")

print(((" ")*10),"¿Listo para iniciar?")
triger = int(input("ingresa (1) para continuar y (2) para salir: "))

if triger == 1:
    print("Ok")

    saldo_inicial = float(input("¿Cuánto dinero quieres depositar a tu cuenta?: "))
    tope_gastos = float(input("¿Cuando quieres que te detengamos?: "))

    if tope_gastos < saldo_inicial:
        print("Ok podemos continuar")

        while saldo_inicial >= tope_gastos:
            compra = float(input("¿Cuánto gastaste hoy?: "))
            saldo_inicial = saldo_inicial - compra
            print(saldo_inicial)



    else:
        print("El saldo debe ser mayor al tope")


elif triger == 2:
    exit()