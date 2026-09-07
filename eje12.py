import math
entrada = input("Ingresa el radio del circulo: ")
if entrada.replace('.','',1).isdigit():
    radio = float(entrada)
    if radio >= 0:
        area = math.pi * radio ** 2
        print(f"El area del circulo es: {area: .2f}")
    else:
        print("Error: El radio no puede ser negativo")
else:
    print("Error: Debes ingresar un numero valido.")    