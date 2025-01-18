#Manipular el diccionario planeta cuando tiene listas como valores

planetas = {
    'nombre' : ['Jupiter','Saturno','Urano','Neptuno','Tierra','Venus','Marte','Mercurio'],
    'tamaño' : ['142,984','108,728 ','51,118','49,532','12,756','12,104','6,794','4,880'],
    'p_elemento' : ['Hidrogeno','Hidrogeno','Hidrogeno','Hidrogeno','Oxigeno','Dioxido de carbono','Hierro','Hierro']
}

print("")
print("Diciconario Planetas con listas como valores: ")
print(planetas)

print("")
print("Acceder a los valores de las claves")
nombre = planetas['nombre']
print(planetas['tamaño'])
print(planetas['p_elemento'])
print()

print("Acceder a los valores especificos que forme el item 'Saturno'")
saturno = planetas['nombre'][1]
print(saturno)
print(planetas['tamaño'][1])
elemento = planetas['p_elemento'][1]
print(elemento)
print()