#declarar variables
#primero definimos las 3 calificaciones
calificacion1=int(input("digita la primera calificacion"))
calificacion2=int(input("digita la segunda calificacion"))
calificacion3=int(input("digita la tercera calificacion"))
#despues definimos el promedio y dimos el comentario
promedio=(calificacion1+calificacion2+calificacion3) /3
if promedio>=70:
    print("el aprendiz aprueba algoritmia con el promedio de",promedio)
else:
      print("el aprendiz desaprobo algoritmia con el promedio de",promedio)