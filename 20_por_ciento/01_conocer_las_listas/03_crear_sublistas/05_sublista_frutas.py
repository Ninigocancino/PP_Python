

lista_frutas = ['Guanabana','Manzana','Pera','Cereza','Fresa','Uva','Melon','Sandía','Coco','Mango','Pitahaya','Tuna','Tomate','Aguacate','Guayaba','Piña','Papaya','Zapote', 'Kiwi', 'Zapote','Higos','Mamey','Rambutan','Nance','Naranja','Limón','Lima','Platano']


conteo = len(lista_frutas)

print("")
print(f"La lista frutas tiene {conteo} elementos")

print("")

sublista_1 = lista_frutas[0:22]
sublista_2 = lista_frutas[22 : 24]
sublista_3 = lista_frutas[24: ]

print("Sublista 1: ")
print(sublista_1)
print("Sublista 2: ")
print(sublista_2)
print("Sublista 3: ")
print(sublista_3)