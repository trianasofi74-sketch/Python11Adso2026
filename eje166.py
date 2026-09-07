estrato = int(input("ingrese el estrato: "))
edad = int(input("ingrese la edad: "))
matricula = float(input("ingrese el valor de la matricula: "))

if estrato == 1 and edad < 18:
    descuento = matricula * 0.20
elif estrato == 1 and edad >= 18:
    descuento = matricula * 0.15
elif estrato == 2 and edad < 18:
    descuento = matricula * 0.10
else:
    descuento = matricula * 0.05

precio = matricula - descuento

print("el descuento es:", descuento)
print("el precio a pagar es:", precio)