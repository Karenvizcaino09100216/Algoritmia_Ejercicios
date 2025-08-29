#NOMBRE:ALGORITMO AÑO BISIESTO
#ENTRADA: ingresar el año
#SALIDA: comprobar si el año es bisiesto o no
#PROCESO: este algoritmo lo que hace es que atraves de el año el usuario descrubra que años en si son bisiestos o no
añobisiesto=int(input("ingrese un año:"))
if añobisiesto % 4 == 0 and añobisiesto  % 100 != 0 or añobisiesto % 400 == 0:  
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")