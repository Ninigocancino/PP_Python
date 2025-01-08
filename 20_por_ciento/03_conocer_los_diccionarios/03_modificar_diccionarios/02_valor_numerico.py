
numero_valor = {
    'veinte': 20,
    'treinta':30,
    'cuarenta': 40,
    'cincuenta': 50,
}

print("")
print("Diccionario original: ")
print(numero_valor)
print("")

print("Modificar el valor de la clave 'cincuenta': ")
numero_valor['cincuenta'] = "cincuenta es lo mismo que:  50"
print(numero_valor)
print("")

print("Modificar el diccionario agregando un nuevo par clave valor:")
numero_valor['sesenta']= 'sesenta es lo mismo que 60'
print(numero_valor)
print("")

print("Modificar el diccionario eliminando una clave valor:")
del numero_valor['sesenta']
print(numero_valor)
print("")

numero_valor['sesenta']= 60
numero_valor['setenta']=70
numero_valor['ochenta']=80

print("Modificar el diccionario eliminando un par calve valor usando pop:")
ochenta= numero_valor.pop('ochenta')
print(numero_valor)
print("")