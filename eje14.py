multp = int(input("Ingrese el numero de la tabla de multiplicar:"))
rang = int(input("Ingrese rango final:"))
i = int(input("Ingrese rango inicial:"))

if i >= rang:
    print("El rango final no puede ser mayor que el rango inicial")
else:
    while i <= rang:
        res = multp * i
        print(multp, "x", i, "=", res)
        i = i + 1