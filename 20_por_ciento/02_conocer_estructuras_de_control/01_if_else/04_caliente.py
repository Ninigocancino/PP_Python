
print("Descubre si el libro esta en el archivo")

archivo = ["Hyperfocus", "El Quijote", "Originals", "Romeo y Julieta", "Sapiens"]

busqueda = input("¿Qué libro estás buscando?: ")

if busqueda in archivo:
    print(f"{busqueda} esta en la colección")
else:
    print("Lo sentimos {busqueda} no se encuentra en el archivo")