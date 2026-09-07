conexion = int(input("ingrese la velocidad de conexion en Mbps: "))

if conexion > 20:
    print("la velocidad de descarga es de 10 Mbps")
elif conexion > 5:
    print("la velocidad de descarga es de 5 Mbps")
else:
    print("la velocidad de descarga es de 1 Mbps")