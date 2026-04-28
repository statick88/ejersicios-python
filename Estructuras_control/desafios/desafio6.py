"""
Desafío 6: Generador de contraseñas
Situación
Una empresa necesita un generador de contraseñas seguras para sus empleados. Las contraseñas deben cumplir con 
requisitos de seguridad específicos y el usuario debe poder personalizar la longitud.

Tu misión
Crea un programa que:

¿Cuántos caracteres? (mínimo 8): 12

Incluir mayúsculas? (s/n): s
Incluir minúsculas? (s/n): s
Incluir números? (s/n): s
Incluir símbolos? (s/n): s

🔐 Tu contraseña segura:
K7m$pL9@xQ2n

¿Generar otra? (s/n): n

¡Hasta luego!
Pista
string.ascii_uppercase → todas las mayúsculas
string.ascii_lowercase → todas las minúsculas
string.digits → todos los números
string.punctuation → todos los símbolos
Usa random.choice() para elegir caracteres aleatorios
Construye una “bolsa” de caracteres según las opciones del usuario
Valida que al menos un tipo de carácter esté seleccionado
Usa un while para ofrecer generar más contraseñas
"""
# Importa los conjuntos de caracteres: import string
import string, random

print("=== GENERADOR DE CONTRASEÑAS ===")

# Pregunte al usuario cuántos caracteres quiere (mínimo 8)
while True:
    longitud = input("¿Cuántos caracteres? (mínimo 8): ")
    if longitud.isdigit() and int(longitud) >= 8:
        longitud = int(longitud)
        break
    print("Por favor, ingresa un número válido (mínimo 8).")
#Mayúsculas (A-Z)
mayusculas = string.ascii_uppercase if input("Incluir mayúsculas? (s/n): ").lower() == "s" else ""

#Pregunte qué tipos de caracteres incluir:

#Minúsculas (a-z)
minusculas = string.ascii_lowercase if input("Incluir minúsculas? (s/n): ").lower() == "s" else ""

#Números (0-9)
numeros = string.digits if input("Incluir números? (s/n): ").lower() == "s" else ""

#Símbolos (!@#$%&*)
simbolos = string.punctuation if input("Incluir símbolos? (s/n): ").lower() == "s" else ""

#Genere una contraseña aleatoria con los criterios seleccionados
caracteres = mayusculas + minusculas + numeros + simbolos
if not caracteres:
    print("Debes seleccionar al menos un tipo de carácter.")
else:
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
#Muestre la contraseña generada
print(f"🔐 Tu contraseña segura:\n{contrasena}")
#Ofrezca generar otra si el usuario lo desea
while input("¿Generar otra? (s/n): ").lower() == "s":
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    print(f"🔐 Tu contraseña segura:\n{contrasena}")
print("¡Hasta luego!")