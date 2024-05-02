#declarar variables
#primero definimos llanta 
llanta = int(input("Llantas compradas: "))
 # fuimos nombrando el mayor y el menor 
if llanta < 5:
    llanta = llanta * 300
    print(f"El valor total a pagar es de: {llanta}")
# y ya despues comenzamos a divir los resultados
elif llanta >= 5 and llanta <= 10:
    llanta = llanta * 250
    print(f"El valor total a pagar es de: {llanta}")
elif llanta > 10:
    llanta = llanta * 200    
    print(f"el valor total a pagar es de: {llanta}")