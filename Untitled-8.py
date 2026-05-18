salario = float(input("Ingrese salario: "))
años = int(input("Ingrese años de trabajo: "))

if años > 5 and salario < 2000:
    print("Recibe bono completo")
elif años > 5 or salario < 2000:
    print("Recibe bono menor")
else:
    print("No recibe bono")