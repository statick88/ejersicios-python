# for con else
"""for i in range(5):
    if i == 10:  # Nunca se cumple
        print("Encontré el 10")
        break
else:
    print("El bucle terminó sin encontrar el 10")"""

# while con else
intentos = 3
while intentos > 0:
    password = input("Contraseña: ")
    if password == "secreto":
        print("¡Acceso concedido!")
        break
    intentos = intentos - 1
    print(f"Te quedan {intentos} intentos")
else:
    print("🔒 Cuenta bloqueada. Demasiados intentos fallidos.")