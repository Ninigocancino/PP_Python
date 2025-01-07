dato_personal = {
    "nombre": "Alberto",
    "apellido": "Gonzalez",
    "edad": 30,
    "ciudad_residencia": "Venecia"}

print(dato_personal)

print("")

dato_personal["edad"] = 36

print("Modificando el valor de la clave 'edad': ")
print(dato_personal)
print("")

print("Agregando un nuevo par clave valor: ")
dato_personal["nivel_educativo"] = "Universidad"
print(dato_personal)
print("")

print("Eliminando un par clave valor: ")
del dato_personal["apellido"]
print(dato_personal)
print("")

dato_personal["apellido_paterno"] = 'Perez'
dato_personal["apellido_materno"] = "Gonzalez"
dato_personal["apodo"] = "Dagon"

print("Nuevos pares:")
print(dato_personal)
print("")

print("Eliminando un par clave valor con pop: ")
apodo = dato_personal.pop("apodo")
print(apodo)
print(dato_personal)
print("")
