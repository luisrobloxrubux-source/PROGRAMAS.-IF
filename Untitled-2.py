usuario = input("Ingrese usuario: ")
contraseña = int(input("Ingrese contraseña: "))

if usuario == "admin" and contraseña == 1234:
    print("Acceso correcto")
else:
    print("Acceso denegado")