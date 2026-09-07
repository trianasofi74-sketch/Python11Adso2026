numero = int(input("Ingrese el número para la tabla de multiplicar: "))
inicio = int(input("Ingrese el valor inicial: "))
final = int(input("Ingrese hasta qué valor desea la tabla: "))
print("\nTabla de multiplicar del", numero)

for i in range(inicio, final + 1):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)