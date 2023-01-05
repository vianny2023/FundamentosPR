#entrada
nombreProducto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad que desea comprar: "))
precio = float(input("Ingrese el precio del producto: "))


#proceso
importe = cantidad * precio

descuento = (importe * 10)/100

totalPagar = importe - descuento

#salida


print("------------------------------")
print("\tTIENDA PEPITO")
print("------------------------------")
print(f"Importe......:{importe:2.1f}")
print("Descuento....:",descuento)
print("Total a pagar:",totalPagar)

print("¡Gracias por su compra! Vuelva pronto ;)")
