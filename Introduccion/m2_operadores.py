#!/usr/bin/env python3
"""
Módulo 2: Operadores
====================

Operadores en Python:
- Aritméticos (+, -, *, /, //, %, **)
- Comparación (==, !=, <, >, <=, >=)
- Lógicos (and, or, not)
- Asignación (=, +=, -=, etc.)

Libro: M2_Operadores.md
"""

# ==========================================
# 1. OPERADORES ARITMÉTICOS
# ==========================================

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")   # 13  suma
print(f"a - b = {a - b}")   # 7   resta
print(f"a * b = {a * b}")   # 30  multiplicación
print(f"a / b = {a / b}")   # 3.333... división
print(f"a // b = {a // b}") # 3   división entera
print(f"a % b = {a % b}")  # 1   módulo (resto)
print(f"a ** b = {a ** b}") # 1000 exponente

# ==========================================
# 2. OPERADORES DE COMPARACIÓN
# ==========================================

x = 5
y = 10

print(f"\nx = {x}, y = {y}")
print(f"x == y = {x == y}")   # False (igual a)
print(f"x != y = {x != y}")  # True (diferente de)
print(f"x < y = {x < y}")    # True (menor que)
print(f"x > y = {x > y}")    # False (mayor que)
print(f"x <= y = {x <= y}")  # True (menor o igual)
print(f"x >= y = {x >= y}")  # False (mayor o igual)

# ==========================================
# 3. OPERADORES LÓGICOS
# ==========================================

# and: ambas condiciones deben ser True
edad = 25
tiene_licencia = True

puede_conducir = edad >= 18 and tiene_licencia
print(f"\n年龄 {edad}, licencia {tiene_licencia}")
print(f"Puede conducir: {puede_conducir}")  # True

# or: al menos una condición debe ser True
es_estudiante = True
es_descuento = False
tiene_cupon = True

recibe_descuento = es_estudiante or es_descuento or tiene_cupon
print(f"\nEstudiante: {es_estudiante}, Descuento: {es_descuento}, Cupón: {tiene_cupon}")
print(f"Recibe descuento: {recibe_descuento}")  # True

# not: invierte el valor
es_mayor = False
print(f"\nEs mayor: {es_mayor}")
print(f"Not es mayor: {not es_mayor}")  # True

# ==========================================
# 4. OPERADORES DE ASIGNACIÓN
# ==========================================

# =
x = 5
print(f"\nx = 5 → x = {x}")

# +=
x += 3   # x = x + 3
print(f"x += 3 → x = {x}")  # 8

# -=
x -= 2   # x = x - 2
print(f"x -= 2 → x = {x}")  # 6

# *=
x *= 2   # x = x * 2
print(f"x *= 2 → x = {x}")  # 12

# /=
x /= 3   # x = x / 3
print(f"x /= 3 → x = {x}")  # 4.0

# //=
x //= 2  # x = x // 2
print(f"x //= 2 → x = {x}")  # 2.0

# %=
x = 10
x %= 3   # x = x % 3
print(f"x %= 3 → x = {x}")  # 1

# **=
x = 2
x **= 4   # x = x ** 4
print(f"x **= 4 → x = {x}")  # 16

# ==========================================
# 5. PRECEDENCIA DE OPERADORES
# ==========================================

# Order de operaciones en Python:
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. == != < > <= >=
# 6. not
# 7. and
# 8. or

resultado = 2 + 3 * 4    # 14 (no 20)
print(f"\n2 + 3 * 4 = {resultado}")  # 14

resultado = (2 + 3) * 4  # 20
print(f"(2 + 3) * 4 = {resultado}")  # 20

# ==========================================
# RESUMEN DEL MÓDULO 2
# ==========================================
"""
Operadores aprendidos:
✓ Aritméticos:  +  -  *  /  //  %  **
✓ Comparación: ==  !=  <  >  <=  >=
✓ Lógicos:    and  or  not
✓ Asignación: =  +=  -=  *=  /=  //=  %=  **=

Precedencia (recuerda PEMDAS):
1. ()
2. **
3. * / // %
4. + -
"""

# Fin del Módulo 2