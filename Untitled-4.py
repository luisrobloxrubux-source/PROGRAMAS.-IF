a = float(input("Ingrese lado 1: "))
b = float(input("Ingrese lado 2: "))
c = float(input("Ingrese lado 3: "))

if a + b > c and a + c > b and b + c > a:
    print("Sí forman un triángulo")

    if a == b and b == c:
        print("Triángulo equilátero")
    elif a == b or a == c or b == c:
        print("Triángulo isósceles")
    else:
        print("Triángulo escaleno")
else:
    print("No forman un triángulo")