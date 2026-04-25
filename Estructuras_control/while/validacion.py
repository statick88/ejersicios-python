# Pedir un número válido al usuario
while True:
    entrada = input("Ingresa un número entre 1 y 10: ")
    
    if entrada.isdigit():
        numero = int(entrada)
        if 1 <= numero <= 10:
            print(f"¡Correcto! Elegiste el {numero}")
            break
        else:
            print("El número debe estar entre 1 y 10")
    else:
        print("Eso no es un número válido. Intenta de nuevo.")