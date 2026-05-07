#!/usr/bin/env python3
"""
Módulo 1: Variables y Tipos de Datos
=================================

Este módulo cubré los tipos fundamentales en Python:
- String (texto)
- Integer (número entero)
- Float (número decimal)
- Boolean (True/False)

Libro: M1_Variables_Tipos.md
"""

# ==========================================
# 1. STRINGS (TEXTO)
# ==========================================

nombre = "María"
apellido = 'García'

# Concatenar (unir) strings
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # María García

# Métodos útiles
print(nombre.upper())      # MAYÚSCULAS
print(nombre.lower())      # minúsculas
print(nombre.capitalize())  # Primera mayúscula

# Longitud
print(len(nombre))         # 5 caracteres

# ==========================================
# 2. INTEGERS (NÚMEROS ENTEROS)
# ==========================================

edad = 25
año_actual = 2026
año_nacimiento = año_actual - edad
print(año_nacimiento)  # 2001

# Operaciones básicas
a = 10
b = 3
print(a + b)   # 13  (suma)
print(a - b)   # 7   (resta)
print(a * b)   # 30  (multiplicación)
print(a / b)   # 3.333... (división)
print(a // b)  # 3   (división entera)
print(a % b)   # 1   (módulo/resto)
print(a ** b)  # 1000 (exponente)

# ==========================================
# 3. FLOATS (NÚMEROS DECIMALES)
# ==========================================

precio = 19.99
pi = 3.14159
iva = 0.15

# Calcular precio con IVA
precio_final = precio + (precio * iva)
print(precio_final)  # 22.9885

# Redondear
print(round(precio_final, 2))  # 22.99

# ==========================================
# 4. BOOLEANS (VERDADERO/FALSO)
# ==========================================

es_mayor = True
tiene_credito = False

# Operadores de comparación
x = 5
y = 10

print(x == y)   # False (igual a)
print(x != y)   # True (diferente de)
print(x < y)    # True (menor que)
print(x <= y)   # True (menor o igual)
print(x > y)    # False (mayor que)
print(x >= y)   # False (mayor o igual)

# ==========================================
# 5. CASTING (CONVERSIÓN DE TIPOS)
# ==========================================

# String → Integer
edad_texto = "25"
edad_numero = int(edad_texto)
print(type(edad_numero))  # <class 'int'>

# Integer → String
numero = 42
texto = str(numero)
print(type(texto))  # <class 'str'>

# String → Float
precio_texto = "19.99"
precio_float = float(precio_texto)
print(type(precio_float))  # <class 'float'>

# ==========================================
# 6. F STRING (FORMATEO MODERNO)
# ==========================================

nombre = "Carlos"
edad = 30

# f-string = formateo moderno y limpio
print(f"Me llamo {nombre} y tengo {edad} años")
print(f"El año que viene tendré {edad + 1} años")

# Con decimales
precio = 19.99
print(f"El precio es: ${precio:.2f}")  # $19.99

# ==========================================
# RESUMEN DEL MÓDULO 1
# ==========================================
"""
Tipos de datos aprendidos:
✓ str     - Texto ("hola")
✓ int     - Entero (42)
✓ float   - Decimal (3.14)
✓ bool    - True/False

Conversiones (casting):
✓ int()   → convierte a entero
✓ float() → convierte a decimal  
✓ str()   → convierte a texto
✓ bool()  → convierte a booleano

Siguiente unidad: M2 - Operadores
"""

# Fin del Módulo 1