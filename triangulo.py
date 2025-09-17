#NOMBRE:ALGORITMOTRIANGULOS
#ENTRADA: ingresar 3 lados
#SALIDA:identificar si los lados que digito pertenece a triangulo isosceles equilatero o escaleno
#PROCESO:este algoritmo hace que cuando el usuario digite 3 lados identifique que tipo de triangulo que es  escaleno,equilatero o isosceles
#AUTOR: KAREN VIZCAINO

lado1=float(input("ingrese el primer lado del triangulo:"))
lado2=float(input("ingrese el segundo lado del triangulo:"))
lado3=float(input("ingrese el tercer lado del triangulo:"))
if lado1 == lado2 == lado3 or lado1==lado3==lado2:
    print("el triangulo es equilatero")
elif lado1 == lado2 and lado2 != lado3 or lado1==lado3 and lado3!=lado2 or lado3==lado2 and lado1!=lado3:
    print("el triangulo es isosceles")
else:
    print("el triangulo es escaleno")

