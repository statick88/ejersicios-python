#!/usr/bin/env python3
"""
Módulo 8: Manejo de Errores
============================

Este módulo cubre cómo manejar errores y excepciones
en Python de manera elegante.

Libro: M8_Errores.md
"""

# ==========================================
# 1. TRY/EXCEPT (BÁSICO
# ==========================================

print("=== Try/Except Básico ===")

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")

# Capturar cualquier error
try:
    x = int("no es número")
except Exception as e:
    print(f"Error capturado: {e}")

# ==========================================
# 2. MÚLTIPLES EXCEPT
# ==========================================

print("\n=== Múltiples Except ===")

try:
    lista = [1, 2, 3]
    valor = lista[10]  # IndexError
except IndexError:
    print("Error: Índice fuera de rango")
except ZeroDivisionError:
    print("Error: División por cero")
except Exception as e:
    print(f"Otro error: {e}")

# ==========================================
# 3. ELSE (SIN ERROR)
# ==========================================

print("\n=== Try/Except/Else ===")

try:
    numero = int("42")
except ValueError:
    print("Error de conversión")
else:
    print(f"Conversión exitosa: {numero}")
    print("El bloque else se ejecuta si NO hay error")

# ==========================================
# 4. FINALLY (SIEMPRE)
# ==========================================

print("\n=== Try/Except/Finally ===")

try:
    archivo = open("temp.txt", "w")
    archivo.write("Datos")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Finally: Siempre se ejecuta")
    # archivo.close()  # Cerrar recurso

# ==========================================
# 5. LANZAR EXCEPCIONES (RAISE)
# ==========================================

print("\n=== Raise (Lanzar Error) ===")

def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(f"Error capturado: {e}")

# ==========================================
# 6. EXCEPCIONES PERSONALIZADAS
# ==========================================

print("\n=== Excepciones Personalizadas ===")

class MiErrorError(Exception):
    """Mi excepción personalizada."""
    pass

def validarEdad(edad):
    if edad < 0:
        raise MiErrorError("La edad no puede ser negativa")
    return "Válido"

try:
    resultado = validarEdad(-5)
except MiErrorError as e:
    print(f"Mi error: {e}")

# ==========================================
# RESUMEN DEL MÓDULO 8
# ==========================================
"""
Sintaxis aprendida:
✓ try: ... except: ... - capturar error
✓ except TipoError: - capturar específico
✓ except Exception as e: - capturar cualquier error
✓ else: - ejecutar si no hay error
✓ finally: - siempre ejecutar
✓ raise TypeError(): - lanzar error personalizado
✓ class MiError(Exception): - crear excepción propia
"""

# Fin del Módulo 8