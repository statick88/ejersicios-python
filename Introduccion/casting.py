"""texto_edad = "25"
print(type(texto_edad))
edad = int(texto_edad)
print(type(edad))"""


"""precio = 19.99
print(type(precio))
precio_texto = str(precio)
print(type(precio_texto))"""

"""valor = 1
print(type(valor))
es_verdadero = bool(valor)
print(type(es_verdadero))"""

"""# ✅ Patrón seguro: validar antes de convertir
edad_input = "25"

# Método 1: verificar con .isdigit()
if edad_input.isdigit():
    edad = int(edad_input)
    print(f"Edad: {edad}")
else:
    print("Error: ingresa un número entero válido")

# Método 2: intentar y capturar el error (try/except)
try:
    precio = float("19.99")
    print(f"Precio: {precio}")
except ValueError:
    print("Error: el valor no es un número válido")"""


"""# Redondeo básico
pi = 3.14159265
print(round(pi, 2))  # <1> — 3.14
print(round(pi, 4))  # <2> — 3.1416

# Redondeo a entero
nota = 8.7
print(round(nota))   # <3> — 9 (redondea al entero más cercano)

# Redondeo de dinero
subtotal = 19.99
impuesto = subtotal * 0.15  # 2.9985
total = subtotal + impuesto  # 22.9885
total_redondeado = round(total, 2)  # <4> — 22.99
print(f"Total: ${total_redondeado}")"""

"""# Decimal a binario (base 2)
numero = 42
binario = bin(numero)
print(binario)  # 0b101010

# Decimal a hexadecimal (base 16)
hexadecimal = hex(numero)
print(hexadecimal)  # 0x2a

# Decimal a octal (base 8)
octal = oct(numero)
print(octal)  # 0o52

# De vuelta a decimal
print(int("101010", 2))   # <4> — 42 (binario a decimal)
print(int("2a", 16))      # <5> — 42 (hexadecimal a decimal)"""

"""# Carácter a código numérico (Unicode)
codigo = ord("A")
print(codigo)  # 65

codigo_z = ord("a")
print(codigo_z)  # 97

# Código numérico a carácter
caracter = chr(65)
print(caracter)  # A

caracter_z = chr(97)
print(caracter_z)  # a

# Ejemplo práctico: verificar si un carácter es mayúscula
letra = "M"
es_mayuscula = 65 <= ord(letra) <= 90
print(es_mayuscula)  # True"""

"""# Valores FALSY (se evalúan como False)
print(bool(0))        # <1> — False: cero numérico
print(bool(0.0))      # False: cero decimal
print(bool(""))       # <2> — False: string vacío
print(bool(None))     # <3> — False: ausencia de valor

# Valores TRUTHY (se evalúan como True)
print(bool(1))        # <4> — True: cualquier número distinto de 0
print(bool(-5))       # True: incluso negativos
print(bool("hola"))   # <5> — True: cualquier string no vacío
print(bool([1, 2]))   # True: listas no vacías"""

"""# ❌ Forma verbosa
nombre = input("Nombre: ")
if nombre == "":
    nombre = "Invitado"
print(nombre)"""

"""# ✅ Forma Pythonica
nombre = input("Nombre: ")
nombre = nombre or "Invitado"
print(nombre)"""

"""# ❌ int() NO redondea, TRUNCA (corta los decimales)
nota = 8.9
nota_entera = int(nota)
print(nota_entera)  # 8 — ¡no 9!

# ✅ Usa round() si quieres redondear
nota_redondeada = round(nota)
print(nota_redondeada)  # 9"""

"""# ❌ Error: int() no acepta strings con punto decimal
# int("3.14")  # ValueError

# ✅ Correcto: primero a float, luego a int
numero = int(float("3.14"))
print(numero)  # 3"""

# str() — para humanos (legible)
texto = str(3.14159)
print(texto)  # "3.14159"

# repr() — para debugging (preciso)
representacion = repr(3.14159)
print(representacion)  # "3.14159"