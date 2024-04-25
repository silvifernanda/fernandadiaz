sueldo=3000000
tcomisiones=0
comisiones=700
ventas=0
total=0

nombre=str(input("nombre del vendedor"))
ventas=int(input("Digite cantidad de ventas"))

tcomisiones= ventas*comisiones
total_= tcomisiones+sueldo

print(f"el vendedor {nombre},tiene un sueldo de {sueldo},durante el mes obtuvo una comision de {tcomisiones}")