print("calculadora de areas")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

continuar = "s"

while continuar == "s":

    print("\nSeleccione una figura:")
    print("1. Cuadrado")
    print("2. Círculo")
    print("3. Rectángulo")
    print("4. Triángulo")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado * lado
        print("El área del cuadrado es:", area)

    elif opcion == 2:
        radio = float(input("Ingrese el radio del círculo: "))
        area = 3.1416 * radio ** 2
        print("El área del círculo es:", area)

    elif opcion == 3:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print("El área del rectángulo es:", area)

    elif opcion == 4:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = (base * altura) / 2
        print("El área del triángulo es:", area)

    else:
        print("Opción no válida.")

    continuar = input("\n¿Desea calcular otra área? (s/n): ").lower()

print("\nPrograma finalizado.")
print("Usuario:", nombre, apellido)
