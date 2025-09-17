#NOMBRE:VOTACIÓN
#ENTRADA:ingresar su edad y su nacionalidad
#SALIDA:si su edad y nacionalidad es valida para votar
#PROCESO:este algoritmo permite que solo el usuario sea colombiano y mayor de edad para que vote de lo contrario no podra votar
#AUTOR: KAREN VIZCAINO
edad = int(input("digite una edad"))
nacionalidad = str(input("digite nacionalidad"))
if edad < 18 or nacionalidad != " colombiano":
    print("usted no puede votar") 
else:
    print("si puede votar")