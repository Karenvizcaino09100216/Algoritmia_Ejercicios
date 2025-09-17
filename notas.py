#NOMBRE:ALGORITMONOTA
#ENTRADA: ingresar una nota
#SALIDA:identificar si atraves de la nota del estudiante aprueba o no
#PROCESO: Este algoritmo hace que el usuario a la hora de digitar su nota sabra si aprobo o no y que no puede ser una nota mayor de 5 ya que no seria valida
#AUTOR: KAREN VIZCAINO
numero1 = float(input("ingrese la nota del estudiante"))
if numero1>= 0 and numero1 <= 5 or numero1 >=3:
    print("aprobaste")
else:
    print("reprobaste")
    print("nota no valida de 0 a 5")
