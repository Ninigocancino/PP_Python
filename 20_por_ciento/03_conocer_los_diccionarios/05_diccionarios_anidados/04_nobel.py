
nobel = {
    'Fisica': {
        '2024':{
            'Nombre': 'Geoffri Hinton, John Holpfield',
            'Titulo' : 'Informaticos'},
        '2023': {
            'Nombre':'Anne L Huillier, Pierre Agostini,  Ferenc Krausz',
            'Titulo':'Fisicos'}
        },
    'Quimica' : {
        '2024':{
            'Nombre': 'Demis Hassabis, David Baker, John Jumper',
            'Titulo': 'Quimicos'},
        '2023': {
            'Nombre': 'Moungi Bawendi, Louis Brus, Alexei Ekimov',
            'Titulo': 'Quimicos'}
        }
    }


print("")
print("Diccionario completo")
print(nobel)
print()


print("Primer nivel de la clave Fisica")
fisica = nobel['Fisica']
print(fisica)
print("Segundo nivel de la clave Fisica")
fisica= nobel['Fisica']['2024']
print(fisica)
print("Tercer nivel de la clave Fisica")
fisica= nobel['Fisica']['2024']['Nombre']
print(fisica)

print("")