"""nombre = "Juan"
edad = 45
ciudad = "Loja"
print(30 * "=" + "Inicio" + 30 *"=" )
print(f"Hola, mi nombre es {nombre}, tengo actualmente {edad} años, vivo en la ciudad de {ciudad}")
#print("Hola, mi nombre es " + nombre + ", tengo actualmente " + str(edad) + " años y vivo en la ciudad de " + ciudad)
print(30 * "=" + "Fin" + 30 *"=" )
print(len(ciudad))"""

# Los strings son secuencias de caracteres
mensaje = "Python es genial"

# Acceder a caracteres individuales (indexación)
#primero = mensaje[0]
#print(primero)
#ultimo = mensaje[-1]
#print(ultimo)

#tercero = mensaje[2]
#print(tercero)

# Cortar una porción (slicing)
#palabra = mensaje[0:6]
#print(palabra)
#hasta = mensaje[:6]
#print(hasta)
#desde = mensaje[7:]
#print(desde)

"""invertido = mensaje[::-1]
print(invertido)"""

frase = "hola MUNDO, soy Python"

# Cambiar mayúsculas/minúsculas
#print(frase.upper())        # <1> — "HOLA MUNDO, SOY PYTHON"
#print(frase.lower())        # <2> — "hola mundo, soy python"
#print(frase.title())        # <3> — "Hola Mundo, Soy Python"
#print(frase.capitalize())   # <4> — "Hola mundo, soy python"
#print(frase.swapcase())     # <5> — "HOLA mundo, SOY pYTHON"

texto = "   Hola Mundo   \n\t"

# Eliminar espacios en blanco
#print(texto.strip())    # <1> — "Hola Mundo"
#print(texto.lstrip())   # <2> — "Hola Mundo   \n\t"
#print(texto.rstrip())   # <3> — "   Hola Mundo"

# Eliminar caracteres específicos
#url = "www.ejemplo.com"
#print(url.strip("w."))  # <4> — "ejemplo.com"

frase = "Python es fácil y Python es divertido"

# Buscar
#print(frase.find("Python"))     # <1> — 0 (primera aparición)
#print(frase.rfind("Python"))    # <2> — 20 (última aparición)
#print(frase.count("Python"))    # <3> — 2 (cuántas veces aparece)

# Reemplazar
#nueva_frase = frase.replace("Python", "JavaScript")
#print(nueva_frase)  # "JavaScript es fácil y JavaScript es divertido"

# Verificar contenido
#print(frase.startswith("Python"))  # <5> — True
#print(frase.endswith("divertido")) # <6> — True

# Dividir un string en partes
#datos = "Ana,25,Quito,Estudiante"
#partes = datos.split(",")
#print(partes)  # ['Ana', '25', 'Quito', 'Estudiante']

# Dividir por espacios
#frase = "Python es genial"
#palabras = frase.split()
#print(palabras)  # ['Python', 'es', 'genial']
#print(palabras[1])  # 'Python'

# Unir una lista de strings
#nombres = ["Ana", "Carlos", "María"]
#unidos = ", ".join(nombres)
#print(unidos)  # "Ana, Carlos, María"

# Unir con salto de línea
#lineas = ["Línea 1", "Línea 2", "Línea 3"]
#texto = "\n".join(lineas)
#print(texto)

nombre = "Ana"
edad = 25
saldo = 1234.5678
nota = 8.5

# Alineación y padding
#print(f"|{nombre:<10}|")     # <1> — "|Ana       |" (alineado izquierda, 10 chars)
#print(f"|{nombre:>10}|")     # <2> — "|       Ana|" (alineado derecha, 10 chars)
#print(f"|{nombre:^10}|")     # <3> — "|   Ana    |" (centrado, 10 chars)

# Formato de números
#print(f"Saldo: ${saldo:.2f}")     # <4> — "Saldo: $1234.57" (2 decimales)
#print(f"Nota: {nota:.1f}/10")     # <5> — "Nota: 8.5/10" (1 decimal)
#print(f"Porcentaje: {0.85:.1%}")  # <6> — "Porcentaje: 85.0%"

# Separador de miles
#poblacion = 8000000
#print(f"Población: {poblacion:,}")  # <7> — "Población: 8,000,000"

# Expresiones dentro de f-strings
#print(f"El doble de {edad} es {edad * 2}")
#print(f"¿Es mayor? {edad >= 18}")

# Verificar el contenido de un string
#print("123".isdigit())     # <1> — True: solo dígitos
#print("abc".isalpha())     # <2> — True: solo letras
#print("abc123".isalnum())  # <3> — True: letras y/o números
#print("   ".isspace())     # <4> — True: solo espacios
#print("Hola".istitle())    # <5> — True: formato título
#print("hola".islower())    # <6> — True: todo minúsculas
#print("HOLA".isupper())    # <7> — True: todo mayúsculas

#frase = "Hola Mundo"

# ❌ Error: los strings son INMUTABLES
# frase[0] = "h"  # TypeError: 'str' object does not support item assignment

# ✅ Correcto: crear un nuevo string
#nueva_frase = frase.replace("H", "h")
#print(nueva_frase)  # "hola Mundo"

#texto = "Hola Mundo"

# ❌ No verificar el resultado de find()
#posicion = texto.find("Python")
#print(posicion)  # -1 — no encontrado

# ✅ Verificar antes de usar
"""if "Python" in texto:
    print("Encontrado")
else:
    print("No encontrado")"""

texto = "Hola Mundo"

# ❌ Esto NO modifica texto
#texto.replace("Mundo", "Python")
#print(texto)  # "Hola Mundo" — ¡no cambió!

# ✅ Debes asignar el resultado
texto = texto.replace("Mundo", "Python")
print(texto)  # "Hola Python"