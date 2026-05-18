monto = float(input("Ingrese monto de compra: "))
cliente = input("Ingrese tipo de cliente (VIP/Normal): ")

if monto > 500 and cliente == "VIP":
    descuento = monto * 0.20
    print("Descuento del 20%")
elif monto > 500:
    descuento = monto * 0.10
    print("Descuento del 10%")
else:
    descuento = 0
    print("Sin descuento")

total = monto - descuento
print("Total a pagar:", total)