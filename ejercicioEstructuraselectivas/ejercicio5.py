#declarar variables
# primeros sacamos edad,sexo y despues las pulsaciones
edad = int(input("Por favor, introduce tu edad: "))
sexo = input("Por favor, introduce tu sexo (femenino/masculino): ")
pulsaciones = (220 - edad) / 10
if sexo == "masculino":
    pulsaciones = (210 - edad) / 10
else:
     print ("Por favor, introduce un sexo válido: 'femenino' o 'masculino'.")

print("El número de pulsaciones que debes tener por cada 10 segundos de ejercicio aeróbico es:", pulsaciones)
