#!/usr/bin/env python3
"""
Ejercicio M2.1: Operadores
==========================

练习: Usar operadores aritméticos y de comparación

Libro: M2_Operadores.md
"""

# ==========================================
# Operadores Aritméticos
# ==========================================

a, b = 10, 3

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")   # suma
print(f"a - b = {a - b}")   # resta
print(f"a * b = {a * b}")   # multiplicación
print(f"a / b = {a / b}")   # división
print(f"a // b = {a // b}")  # división entera
print(f"a % b = {a % b}")   # módulo (resto)
print(f"a ** b = {a ** b}")  # exponente

# ==========================================
# Operadores de Comparación
# ==========================================

x, y = 5, 10

print(f"\nx = {x}, y = {y}")
print(f"x == y: {x == y}")   # igual
print(f"x != y: {x != y}")   # diferente
print(f"x < y: {x < y}")     # menor
print(f"x > y: {x > y}")     # mayor
print(f"x <= y: {x <= y}")   # menor o igual
print(f"x >= y: {x >= y}")   # mayor o igual

# ==========================================
# Operadores Lógicos
# ==========================================

sol = True
calor = True

print(f"\nsol = {sol}, calor = {calor}")
print(f"sol and calor: {sol and calor}")
print(f"sol or False: {sol or False}")
print(f"not sol: {not sol}")

# ==========================================
# OPERADORES EN CONDICIONES
# ==========================================

edad = 20

# and: ambas condiciones
if edad >= 18 and edad < 65:
    print(f"\nEdad {edad}: Adulto working")

# or: al menos una
rol = "admin"
if rol == "admin" or rol == "editor":
    print(f"Rol {rol}: Acceso completo")

# ==========================================
# DESAFÍO: Calculadora simple
# ==========================================

def calculadora(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        return a / b if b != 0 else "Error"
    else:
        return "Operación inválida"

print("\nCalculadora:")
print(f"10 + 5 = {calculadora(10, 5, '+')}")
print(f"10 - 5 = {calculadora(10, 5, '-')}")
print(f"10 * 5 = {calculadora(10, 5, '*')}")
print(f"10 / 5 = {calculadora(10, 5, '/')}")