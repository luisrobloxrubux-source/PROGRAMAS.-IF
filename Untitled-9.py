nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print("Promedio:", promedio)

if promedio >= 11:
    print("Aprobado")
elif promedio < 11 and promedio > 8:
    print("Recuperación")
else:
    print("Desaprobado")