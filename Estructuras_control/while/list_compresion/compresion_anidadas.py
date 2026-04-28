# Tabla de multiplicar del 1 al 3
tabla = [f"{i}x{j}={i*j}" for i in range(1, 4) for j in range(1, 4)]

for operacion in tabla:
    print(operacion)