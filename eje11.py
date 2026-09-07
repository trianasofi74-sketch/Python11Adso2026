not1 = float(input("Ingrese nota 1: "))
not2 = float(input("Ingrese nota 2: "))

if (not1 >= 2.5 and not2 >= 2.5):
    if (not1 <= 5 and not2 <= 5):
        prom = (not1 + not2) / 2
        if (prom >= 3.0):
            print("El aprendiz aprueba con:", prom)
        else:
            print("El aprendiz no aprueba, su nota es:", prom)
    else:
        print("Solo se admiten notas menores a 5.0")
else:
    print("Solo se admiten notas mayores a 2.5")
        