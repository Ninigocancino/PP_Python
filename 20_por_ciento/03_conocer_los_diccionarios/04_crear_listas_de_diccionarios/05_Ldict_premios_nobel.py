#Trabajar con el diciconario Premios Nobel cuando tiene listas por valores de claves

premios_nobel = {
    'nombre' : ['Marie Curie', 'Marie Curie','Albert Einstein','Nelson Mandela','Tu Youyou'],
    'categoria' : ['Fisica','Quimica','Fisica','Paz','Medicina'],
    'anio' : [1903,1911,1921,1993,2015]
}

print("")
print("Diccionario 'Premios Nobel' con listas como valores")
print(premios_nobel)

print("")
print("Acceder a los valores de las claves 'categoria' y 'anio' ")
categoria = premios_nobel['categoria']
print(categoria)
print(premios_nobel['anio'])
print("")

print("")
print("Acceder a los valores que conforman el item 'Albert Einstein' ")
print(premios_nobel['nombre'][2])
print(premios_nobel['categoria'][2])
anio = premios_nobel['anio'][2]
print(anio)
print("")