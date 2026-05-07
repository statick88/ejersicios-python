#!/usr/bin/env python3
"""
Ejercicio M2.1: Operadores
=========================

练习: Practicar operadores en Python

Libro: M2_Operadores.md
"""

# ==========================================
# Ejercicio 1: Operadores aritméticos
# ==========================================

a = 15
b = 4

print("=== Operadores Aritméticos ===")
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")   # 19
print(f"a - b = {a - b}")   # 11
print(f"a * b = {a * b}")   # 60
print(f"a / b = {a / b}")   # 3.75
print(f"a // b = {a // b}") # 3
print(f"a % b = {a % b}")  # 3
print(f"a ** b = {a ** b}") # 50625

# ==========================================
# Ejercicio 2: Operadores de comparación
# ==========================================

x = 7
y = 7
z = 10

print("\n=== Operadores de Comparación ===")
print(f"x = {x}, y = {y}, z = {z}")
print(f"x == y: {x == y}")   # True
print(f"x != z: {x != z}")   # True
print(f"x < z: {x < z}")    # True
print(f"x <= y: {x <= y}")  # True

# ==========================================
# Ejercicio 3: Operadores lógicos
# ==========================================

edad = 16
es_estudiante = True
tiene_dinero = False

print("\n=== Operadores Lógicos ===")
print(f"Edad: {edad}, Estudiante: {es_estudiante}, Dinero: {tiene_dinero}")

# and - ambas condiciones
puede_entrar = edad >= 18 and tiene_dinero
print(f"edad >= 18 and tiene_dinero = {puede_entrar}")  # False

# or - al menos una
tiene_descuento = es_estudiante or tiene_dinero
print(f"es_estudiante or tiene_dinero = {tiene_descuento}")  # True

# not - inverso
no_es_estudiante = not es_estudiante
print(f"not es_estudiante = {no_es_estudiante}")  # False

# ==========================================
# Ejercicio 4: Calculadora simple
# ==========================================

def calculadora(a, b, operador):
    """Calculadora básica con operadores."""
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        return a / b if b != 0 else "Error: división por cero"
    else:
        return "Operador no válido"

print("\n=== Calculadora ===")
print(f"10 + 5 = {calculadora(10, 5, '+')}")   # 15
print(f"10 - 5 = {calculadora(10, 5, '-')}")   # 5
print(f"10 * 5 = {calculadora(10, 5, '*')}")   # 50
print(f"10 / 5 = {calculadora(10, 5, '/')}")   # 2.0

# ==========================================
# DESAFÍO: Calculadora de IMC
# ==========================================

# BMI = weight / (height in meters)²

peso = 70     # kg
altura = 1.75  # metros

imc = peso / (altura ** 2)
print(f"\n=== Calculadora de IMC ===")
print(f"Peso: {peso}kg, Altura: {altura}m")
print(f"IMC = {imc:.2f}")  # ~22.86

# Clasificación
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc < 25:
    print("Clasificación: Normal")
elif imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")