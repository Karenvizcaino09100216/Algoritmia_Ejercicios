#NOMBRE:ALGORITMO ACCESO
#ENTRADA: ingresar el rol para saber si tiene acceso permitido o no
#SALIDA:ingresar el rol para saber si es admin o usuario 
#PROCESO:el usuario al digitar su rol,el algoritmo le dira si tiene acceso si es admin de lo contrario no tendra acceso
#AUTOR: KAREN VIZCAINO
rol=str(input("INGRESE SU ROL ADMIN/USUARIO:   "))
if rol== "admin":
    print("ACCESO PERMITIDO")
else:
    print("ACCESO DENEGADO INTRUSOOO")
    