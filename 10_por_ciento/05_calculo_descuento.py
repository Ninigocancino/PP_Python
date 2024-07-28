#En una tienda se hace un descuento del 7% sobre el total de las compras, calcula la cantidad a pagar por una compra determinada

print("Hoy tenemos 7 por ciento de descuento en toda la tienda")

compra = float(input("Ingrese el monto de la campra: "))

rebaja = 0.07

descuento = compra * rebaja

total = compra - descuento

print(f"Su compra es de {compra}")
print(f"Su descuento es {descuento}")
print(f"Total a pagar: {total}")

print("")
print("Gracias por su compra vuelva pronto")

exit()