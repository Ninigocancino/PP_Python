
#Manejar el diccionario números usando listas como valores de las claves

numeros = {
    'pares' : [2,4,6,8,10,12],
    'primos' : [2,3,5,7,11,13],
    'impares' : [1,3,5,7,9,11],
    'romanos_pares' : ['II','IV','VI','VIII','X','XII']
}

print("")
print("Diccionario números manejando listas como valres de las claves")
print(numeros)
print()

print("Acceder a los valores de las claves del diccionario")
pares = numeros['pares']
print(pares)
print(numeros['primos'])
impares = numeros['impares']
print(impares)
print(numeros['romanos_pares'])
print("")

print("Acceder a valores especificos en el diccionario 'numeros' ")
primos = numeros['primos'][4]
print(primos)
print(numeros['romanos_pares'][3])
print("")