
# Trabajar el dicionario 'Planetas' usando anidamiento de diccioanrios

planetas = {
    'rocosos' :{
        'pr01':{
            "nombre" : 'Tierra',
            'posición' : '3',
            'principal_elemento' : 'Oxigeno' },
        'pr02':{
            'nombre' : 'Mercurio',
            'posicion' : '1',
            'principal_elemento' : 'Hierro'},
        },
    'gaseosos':{
        'pg01' :{
            'nombre' : 'Jupiter',
            'posicion': '5',
            'principal_elemento' : 'Hidrogeno'},
        'pg02': {
            'nombre' : 'Saturno',
            'posicion' : '6',
            'principal_elemento' : 'Hidrogeno'}
        }
    }

print()
print("Diccionario anidado con información de planetas")
print(planetas)
print()

print("Primer nivel de la clave Rocosos")
rocosos = planetas['rocosos']
print(rocosos)
print("")

print("Acceder al segundo nivel de la clave 'gaseoso' ")
gaseoso = planetas['gaseosos']['pg01']
print(gaseoso)
print()
