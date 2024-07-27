# Hacer un algortimo para encontrar el valor de 'x' en el comentario siguiente:
# x=2-a+3/bc + ad -15y

#Se imprimen en consola las instrucciones 
print("Averiguemos el valor de 'x' en la siguiente ecuación:")
print(" x= 2- a+3/bc + ad -15y")
print("") #simplemente separa las lineas en consola

#las sigunetes variables guardan un valor ingresado por el usuario que se asignarán a las variables de la ecuación 
a = float(input("siendo 'a' = ")) #se pide al usuario que asigne el valor de la variable 'a' y lo combertimos a un dato de tipo decimal
b = float(input("siendo 'b' = "))
c = float(input("siendo 'c' = "))
d = float(input("siendo 'd' = "))
y = float(input("siendo 'y' = "))

x = 2 - (a+3)/(b*c + a*d) - 15*y #Se asigna la operación a la variable 'x' para guardar el resultado

print("") #simplemente separa las lineas en consola

print(f"el resultado de 'x' es igual a {x}") #Se imprime el resultado en consola acompañado de un mensaje relacionado