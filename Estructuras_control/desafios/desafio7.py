"""
Desafío 7: Cajero automático
Situación
Vas a simular un cajero automático completo. Este es el desafío integrador del módulo: 
combina if/else, 
bucles, 
validación y lógica de negocio en un solo programa.

Tu misión
Crea un programa que simule un cajero con las siguientes funciones:

Ejemplo de ejecución
=== CAJERO AUTOMÁTICO ===
Bienvenido, usuario

Saldo actual: $1,000.00

1. Consultar saldo
2. Depositar
3. Retirar
4. Historial
5. Salir

Elige una opción: 3

¿Cuánto deseas retirar? 200
✅ Retiro exitoso: $200.00
Saldo actual: $800.00

1. Consultar saldo
2. Depositar
3. Retirar
4. Historial
5. Salir

Elige una opción: 4

=== HISTORIAL DE TRANSACCIONES ===
#1  | Retiro   | -$200.00 | Saldo: $800.00
#0  | Inicial  |          | Saldo: $1,000.00

1. Consultar saldo
2. Depositar
3. Retirar
4. Historial
5. Salir

Elige una opción: 5

¡Gracias por usar nuestro cajero!
---
Pista
Usa un while True para el menú principal
Usa if/elif/else para cada opción del menú
Almacena las transacciones en una lista de diccionarios o tuplas
Para el historial, itera la lista con for y formatea cada línea
Valida que los montos sean positivos y que el retiro no exceda el saldo
Usa break para salir del menú principal
"""

# Consultar saldo — muestra el saldo actual
#Requisitos técnicos
#Cada transacción debe registrarse con tipo, monto y resultado

saldo = 1000.00
transacciones = [("Inicial", 0.00, saldo)]

while True:
#El menú se repite hasta que el usuario decida salir
    print("=== CAJERO AUTOMÁTICO ===")
    print("Bienvenido, usuario\n")
    print(f"Saldo actual: ${saldo:.2f}\n")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Historial")
    print("5. Salir\n")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        #Saldo inicial: $1,000
        print(f"Saldo actual: ${saldo:.2f}")
    elif opcion == "2":
    #Depositar — agrega dinero a la cuenta
        monto = float(input("¿Cuánto deseas depositar? "))
        if monto > 0:
            print(f"✅ Depósito exitoso: ${monto:.2f}")
            saldo += monto
            transacciones.append(("Depósito", monto, saldo))
        else:
            print("Monto inválido. Debe ser positivo.")
    elif opcion == "3":
        #Retirar — saca dinero (no puede superar el saldo)
        monto = float(input("¿Cuánto deseas retirar? "))
        if monto > 0 and monto <= saldo:
            print(f"✅ Retiro exitoso: ${monto:.2f}")
            saldo -= monto
            transacciones.append(("Retiro", monto, saldo))
        else:
            print("Monto inválido o saldo insuficiente.")
    elif opcion == "4":
        #Historial — muestra las últimas transacciones
        #No se puede retirar más del saldo disponible
        #El historial debe mostrar al menos las últimas 10 transacciones
        print("=== HISTORIAL DE TRANSACCIONES ===")
        for i, (tipo, monto, nuevo_saldo) in enumerate(transacciones[-10:]):
            if tipo == "Retiro":
                print(f"#{i}  | {tipo}   | -${monto:.2f} | Saldo: ${nuevo_saldo:.2f}")
            else:
                print(f"#{i}  | {tipo}  | +${monto:.2f} | Saldo: ${nuevo_saldo:.2f}")
    elif opcion == "5":
        #Salir — termina el programa
        print("¡Gracias por usar nuestro cajero!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.") 



