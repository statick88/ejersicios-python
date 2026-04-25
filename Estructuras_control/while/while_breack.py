# Menú interactivo que se repite hasta que el usuario quiere salir
while True:
    print("\n=== MENÚ ===")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("Tu saldo es: $1,000")
    elif opcion == "2":
        monto = input("¿Cuánto deseas depositar? ")
        print(f"Depósito de ${monto} recibido")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")