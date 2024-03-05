"""
Planteamiento del problema:

Suponagmos que trabajas en un negocio donde eres el responsable del almacen. Tu trabajo consiste en recibir los diferentes articulos que llegan al negocio y colocarlos en el anaquel correspondiente.

Para ello debes verificar el particulo en la barra de recepción y después ingresar al sistema e ingresar el tipo de articulo que estas recibiendo, una vez que lo consultas con el sistema, este te devuelve el numero de anaquel en el cuál debes colocar el articulo, así como el numero de fila y columna.

Después debes llevar el articulo al anaquel y confirmar en el sistema que el articulo a sido colocado correctamente. 
"""

"""
Instrucciones:

1) Crea 6 categorias de anaqueles ("enlatados","granos","Cajas","Limpieza","Electronicos","Vidrio")
2) Divide el espacio vertical del anaquel  en 5 niveles que correpondan con el tamaño del articulo ("Muy grande","Grande","Mediano","Puequeños" y "Muy pequeños")
3) Permite al sistema recibir entradas del usuario
4) Devuelve al usuario un mensaje que le ayude a realizar la siguiente acción
"""

"""
Elementos de prueba:

1) Paquete de atún (50 latas)
2) Bajilla de cristal (200 piezas)
3) Saco e arroz 60 kilos
"""

a_1 = [
    {"fila 1":{"columna 1": "O", "columna 2": "V", "columna 3": "V"}},
    {"fila 2":{"columna 1": "V", "columna 2": "O", "columna 3": "V"}},
    {"fila 3":{"columna 1": "V", "columna 2": "V", "columna 3": "V"}}
]

a_2 = [
    {"fila 1":{"columna 1": "V", "columna 2": "V", "columna 3": "V"}},
    {"fila 2":{"columna 1": "V", "columna 2": "O", "columna 3": "V"}},
    {"fila 3":{"columna 1": "V", "columna 2": "V", "columna 3": "V"}}
]

a_3 = [
    {"fila 1":{"columna 1": "O", "columna 2": "V", "columna 3": "V"}},
    {"fila 2":{"columna 1": "O", "columna 2": "O", "columna 3": "O"}},
    {"fila 3":{"columna 1": "V", "columna 2": "O", "columna 3": "V"}}
]

a_4 = [
    {"fila 1":{"columna 1": "O", "columna 2": "V", "columna 3": "V"}},
    {"fila 2":{"columna 1": "V", "columna 2": "O", "columna 3": "V"}},
    {"fila 3":{"columna 1": "V", "columna 2": "V", "columna 3": "V"}}
]

a_5 = [
    {"fila 1":{"columna 1": "O", "columna 2": "V", "columna 3": "V"}},
    {"fila 2":{"columna 1": "V", "columna 2": "O", "columna 3": "V"}},
    {"fila 3":{"columna 1": "V", "columna 2": "V", "columna 3": "V"}}
]

a_6 = [
    {"fila 1":{"columna 1": "O", "columna 2": "V", "columna 3": "V"}},
    {"fila 2":{"columna 1": "V", "columna 2": "O", "columna 3": "V"}},
    {"fila 3":{"columna 1": "V", "columna 2": "V", "columna 3": "V"}}
]

print("Esta sucursal puede almacenar solo este tipo de articulos: \n Enlatados (1) \n Granos (2) \n Limpieza (3) \n Electronicos (4) \n Vidrio (5) \n Cajas (6)")
print("")
articulo = int(input("¿Qué tipo de articulo necesitas guardar (ingresa el número asignado a la opción correspondiente): "))
print("")
print("Tamaños para guardar articulos: \n Muy Grande (1) \n Grande (2) \n Mediano (3) \n pequeño (4) \n Muy pequeño (5)")
size = int(input("Ingrese el tamaño del articulo: "))



