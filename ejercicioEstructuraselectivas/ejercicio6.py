#declarar variables
#primero sacamos el costo y el promedio 
costo = 2000000
promedio = float(input("Digite su promedio de su periodo anterior: "))
# despues sacamos el mayor y dividimos el costo por 0.3
if promedio >= 9:
    costo = costo-(costo*0.3)
    print (f"Se le hará un desucento del 30% al valor de su pension y queda en: {costo}")
#despues sacamos el menor y dividimos por 0.1
elif promedio < 9:
    costo = ( costo*0.1)+costo
    print(f"Su pension queda igual y se le agrega el 10% de IVA yqueda en: {costo}")