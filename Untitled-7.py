contraseña = int(input("Ingrese una contraseña numérica: "))

if contraseña > 1000 and contraseña < 9999:
    print("Contraseña válida")
else:
    print("Contraseña inválida")