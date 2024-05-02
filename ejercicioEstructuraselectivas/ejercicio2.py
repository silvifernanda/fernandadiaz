#declarar variables
#definimos la cantidad de zapatillas, el precio y el total
cantidad_zapatillas=int(input("ingrese la cantidad de zapatillas"))
precio_zapatilla=float(input("ingrese el precio de la zapatilla"))

total_sin_descuento=cantidad_zapatillas*precio_zapatilla

if cantidad_zapatillas >=3:
    descuento=total_sin_descuento*0.20
else:
    descuento=total_sin_descuento*0.10
    total_a_pagar=total_sin_descuento-descuento
print("total a pagar es:",total_a_pagar)