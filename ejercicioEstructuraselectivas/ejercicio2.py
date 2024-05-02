#declarar variables
#definimos la cantidad de zapatillas,el precio
cantidad_zapatillas=int(input("ingrese la cantidad de zapatillas"))
precio_zapatilla=float(input("ingrese el precio de la zapatilla"))
#despues dimos el total de las zapatillas
total_sin_descuento=cantidad_zapatillas*precio_zapatilla
#y despues dimos el descuento y el comentario
if cantidad_zapatillas >=3:
    descuento=total_sin_descuento*0.20
else:
    descuento=total_sin_descuento*0.10
    total_a_pagar=total_sin_descuento-descuento
print("total a pagar es:",total_a_pagar)