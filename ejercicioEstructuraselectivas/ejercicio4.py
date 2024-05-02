#declarar variables
#primero definimos el color,la compra 
color = str(input("digite un color :"))
compra =float(input("digite el valor de la compra :"))
#depues sacamos el descuento de la compra
if color =="rojo":
    descuento =compra*0.15
    valorPagar=compra-descuento
    print("El valor de la compra fue:",compra,"usted saco la balota: ",color,"con un descuento de:",descuento,"el valor a pagar es:",valorPagar)
    #y ya por ultimo dimos el total a pagar de la compra
elif color == "verde":
    descuento= compra*0.20
    valorPagar=compra-descuento
    print("El valor de la compra fue:",compra,"usted saco la balota: ",color,"con un descuento de:",descuento,"el valor a pagar es:",valorPagar)
else:
    print("no tienes descuento")