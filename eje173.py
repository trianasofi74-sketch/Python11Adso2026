print("Ingresa números (un número negativo termina el programa):")


new_var = 10

for i in range(new_var): 
    numero = float(input(f"Número {i + 1}: "))

    if numero < 0:
        print(f"¡Número negativo detectado! ({numero})")
        print("Programa terminado.")
        break  

    else:
        print(f"Número ingresado: {numero}")

print("Fin del programa.")