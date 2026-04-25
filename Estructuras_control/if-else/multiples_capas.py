
# Sistema de autenticación con múltiples capas
usuario = "admin"
password = "secreto123"
token = "valido"

if usuario == "admin":
    if password == "secreto123":
        if token == "valido":
            print("Acceso concedido al panel")
        else:
            print("Token inválido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")