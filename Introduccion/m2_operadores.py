#!/usr/bin/env python3
"""
Módulo 2: Operadores y Expresiones
=============================

 Este módulo cubré cómo operar datos en Python:
 - Operadores aritméticos (+, -, *, /)
 - Operadores de comparación (==, !=, <, >)
 - Operadores lógicos (and, or, not)
 - Operador ternario

 Ebook: Ver M2_Operadores.md para teoría completa
"""

# ==========================================
# 1. OPERADORES ARITMÉTICOS
# ==========================================

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Suma: a + b = {a + b}")           # 13
print(f"Resta: a - b = {a - b}")           # 7
print(f"Multiplicación: a * b = {a * b}")   # 30
print(f"División: a / b = {a / b}")       # 3.333...
print(f"División entera: a // b = {a // b}")  # 3
print(f"Módulo: a % b = {a % b}")           # 1 (resto)
print(f"Exponente: a ** b = {a ** b}")      # 1000

# ==========================================
# 2. OPERADORES DE COMPARACIÓN
# ==========================================

x = 5
y = 10

print("\n--- Comparación ---")
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")   # False (igual)
print(f"x != y: {x != y}")   # True (diferente)
print(f"x < y: {x < y}")     # True (menor)
print(f"x <= y: {x <= y}")   # True (menor o igual)
print(f"x > y: {x > y}")     # False (mayor)
print(f"x >= y: {x >= y}")   # False (mayor o igual)

# ==========================================
# 3. OPERADORES LÓGICOS
# ==========================================

sol = True
lluvia = False
calor = True

print("\n--- Lógicos ---")
print(f"sol={sol}, lluvia={lluvia}, calor={calor}")

# and: ambos deben ser True
print(f"sol Y lluvia: {sol and lluvia}")           # False
print(f"sol Y calor: {sol and calor}")             # True

# or: al menos uno debe ser True
print(f"sol O lluvia: {sol or lluvia}")           # True

# not: invierte el valor
print(f"NO lluvia: {not lluvia}")               # True

# ==========================================
# 4. OPERADOR TERNARIO (CONDIÇÃO)
# ==========================================

edad = 18

# Forma larga:
if edad >= 18:
    resultado = "Mayor de edad"
else:
    resultado = "Menor de edad"

# Forma ternaria (una línea):
resultado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"\nEdad: {edad} → {resultado}")

# ==========================================
# 5. PRIORIDAD DE OPERADORES
# ==========================================

# Python sigue el orden matemático estándar:
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. == != < > <= >=
# 6. not
# 7. and
# 8. or

resultado = 2 + 3 * 4          # 14 (no 20)
resultado_parens = (2 + 3) * 4    # 20

print(f"\n2 + 3 * 4 = {resultado}")
print(f"(2 + 3) * 4 = {resultado_parens}")

# ==========================================
# 6. OPERADORES DE ASIGNACIÓN
# ==========================================

x = 10
x += 5      # x = x + 5  → 15
print(f"\nx += 5: {x}")

x = 10
x -= 5      # x = x - 5  → 5
print(f"x -= 5: {x}")

x = 10
x *= 2      # x = x * 2  → 20
print(f"x *= 2: {x}")

# ==========================================
# RESUMEN DEL MÓDULO 2
# ==========================================
"""
Operadores aprendidos:
✓ aritméticos: + - * / // % **
✓ comparación: == != < > <= >=
✓ lógicos: and or not
✓ ternario: valor1 if cond else valor2
✓ asignación: += -= *= /=

Precedencia (orden de cálculo):
1. ()
2. **
3. * / // %
4. + -
5. == !=
6. not
7. and
8. or

Siguiente unidad: M3 - Control de Flujo
Ebook: M3_Control_Flujo.md
"""

# Fin del Módulo 2