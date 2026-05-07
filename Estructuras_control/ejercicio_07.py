#!/usr/bin/env python3
"""
Ejercicio M8.1: Manejo de Errores
==================================

练习: Practicar manejo de errores

Libro: M8_Errores.md
"""

# ==========================================
# Ejercicio 1: División segura
# ==========================================

def division_segura(a, b):
    """División que maneja errores."""
    try:
        return a / b
    except ZeroDivisionError:
        return None  # O returns "Error: división por cero"

print("=== Ejercicio 1: División Segura ===")
print(f"10 / 2 = {division_segura(10, 2)}")
print(f"10 / 0 = {division_segura(10, 0)}")

# ==========================================
# Ejercicio 2: Conversión de tipos
# ==========================================

def convertir_a_numero(valor):
    """Convierte string a número"""
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            return None

print("\n=== Ejercicio 2: Conversión ===")
print(f"'42' → {convertir_a_numero('42')}")
print(f"'3.14' → {convertir_a_numero('3.14')}")
print(f"'hola' → {convertir_a_numero('hola')}")

# ==========================================
# Ejercicio 3: Validar edad
# ==========================================

class EdadInvalidaError(Exception):
    """Error para edad inválida."""
    pass

def validar_edad(edad):
    """Valida que edad sea positiva."""
    if edad < 0:
        raise EdadInvalidaError("Edad negativa")
    if edad > 150:
        raise EdadInvalidaError("Edad imposible")
    return True

print("\n=== Ejercicio 3: Validar Edad ===")
for edad in [25, -5, 200]:
    try:
        validar_edad(edad)
        print(f"Edad {edad}: OK")
    except EdadInvalidaError as e:
        print(f"Edad {edad}: Error - {e}")

# ==========================================
# DESAFÍO: Calculadora robusta
# ==========================================

def calculadora(a, b, operacion):
    """Calculadora con manejo de errores."""
    try:
        if operacion == "+":
            return a + b
        elif operacion == "-":
            return a - b
        elif operacion == "*":
            return a * b
        elif operacion == "/":
            return a / b
        else:
            raise ValueError(f"Operación desconocida: {operacion}")
    except ZeroDivisionError:
        return "Error: División por cero"
    except TypeError:
        return "Error: Tipos incompatibles"

print("\n=== Desafío: Calculadora ===")
print(f"10 + 5 = {calculadora(10, 5, '+')}")
print(f"10 / 0 = {calculadora(10, 0, '/')}")
print(f"10 % 5 = {calculadora(10, 5, '%')}")