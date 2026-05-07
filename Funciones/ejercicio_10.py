#!/usr/bin/env python3
"""
Ejercicio M8.1: Errores y Excepciones
=====================================

练习: Manejar errores con try/except

Libro: M8_Errores.md
"""

# ==========================================
# 1. try/except básico
# ==========================================

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("1. Error: No se puede dividir entre cero")

# ==========================================
# 2. Múltiples except
# ==========================================

try:
    numero = int("hola")
except ValueError:
    print("2. Error: No es un número válido")

try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("2. Error: Índice fuera de rango")

# ==========================================
# 3. except con excepción base
# ==========================================

try:
    variable = no_existe
except NameError:
    print("3. Error: Variable no definida")

# ==========================================
# 4. try/except/else/finally
# ==========================================

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: División entre cero"
    else:
        return f"Resultado: {resultado}"
    finally:
        print("   → finally siempre se ejecuta")

print("\n4. Con else y finally:")
print(dividir(10, 2))
print(dividir(10, 0))

# ==========================================
# 5. raise (lanzar excepciones)
# ==========================================

def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 150:
        raise ValueError("Edad inválida")
    return "Edad válida"

try:
    print(verificar_edad(25))
    print(verificar_edad(-5))
except ValueError as e:
    print(f"5. {e}")

# ==========================================
# 6. Crear excepción personalizada
# ==========================================

class MiError(Exception):
    """Mi excepción personalizada"""
    pass

def verificar_numero(numero):
    if numero < 0:
        raise MiError("Número negativo no permitido")
    return numero

try:
    print(verificar_numero(10))
    print(verificar_numero(-5))
except MiError as e:
    print(f"6. Error personalizado: {e}")

# ==========================================
# 7. Manejo seguro de archivos
# ==========================================

def leer_archivo_seguro(nombre):
    try:
        with open(nombre, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Archivo no encontrado"
    except PermissionError:
        return "Sin permiso"

print(f"\n7. Leer archivo: {leer_archivo_seguro('noExiste.txt')}")