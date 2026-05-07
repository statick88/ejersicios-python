#!/usr/bin/env python3
"""
Ejercicio M4.1: Funciones
=========================

练习: Definir y llamar funciones

Libro: M4_Funciones.md
"""

# ==========================================
# 1. Función básica
# ==========================================

def saludar():
    """Saluda al usuario"""
    print("¡Hola!")

saludar()

# ==========================================
# 2. Función con parámetros
# ==========================================

def saludar_persona(nombre):
    """Saluda a una persona"""
    print(f"¡Hola, {nombre}!")

saludar_persona("Carlos")
saludar_persona("Ana")

# ==========================================
# 3. Función con return
# ==========================================

def sumar(a, b):
    """Suma dos números"""
    return a + b

resultado = sumar(5, 3)
print(f"5 + 3 = {resultado}")

# ==========================================
# 4. Parámetros con valores por defecto
# ==========================================

def saludar_persona(nombre, idioma="es"):
    """Saluda según el idioma"""
    saludos = {
        "es": f"¡Hola, {nombre}!",
        "en": f"Hello, {nombre}!",
        "fr": f"Bonjour, {nombre}!",
        "pt": f"Olá, {nombre}!"
    }
    return saludos.get(idioma, f"¡Hola, {nombre}!")

print(saludar_persona("Carlos"))
print(saludar_persona("Carlos", "en"))
print(saludar_persona("Carlos", "fr"))

# ==========================================
# 5. *args y **kwargs
# ==========================================

def suma_total(*args):
    """Suma todos los argumentos"""
    return sum(args)

print(f"\nSuma de 1,2,3,4,5: {suma_total(1, 2, 3, 4, 5)}")

def mostrar_persona(**kwargs):
    """Muestra información de persona"""
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

print("\nPersona:")
mostrar_persona(nombre="Ana", edad=25, ciudad="Quito")

# ==========================================
# 6. Lambda (función anónima)
# ==========================================

cuadrado = lambda x: x ** 2
print(f"\nCuadrado de 5: {cuadrado(5)}")

sumar = lambda a, b: a + b
print(f"3 + 7: {sumar(3, 7)}")

# ==========================================
# Lambda con map, filter, sorted
# ==========================================

numeros = [1, 2, 3, 4, 5]

# map: aplicar función a cada elemento
print(f"\nmap (dobles): {list(map(lambda x: x * 2, numeros))}")

# filter: filtrar elementos
print(f"filter (pares): {list(filter(lambda x: x % 2 == 0, numeros))}")

# sorted con key
nombres = ["Carlos", "Ana", "Bob", "Diana"]
print(f"sorted (largo): {sorted(nombres, key=len)}")

# ==========================================
# DESAFÍO: Calculadora con funciones
# ==========================================

def calculadora(a, b, operacion):
    """Calculadora básica"""
    operaciones = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else "Error"
    }
    func = operaciones.get(operacion)
    return func(a, b) if func else "Error"

print("\nCalculadora:")
print(f"10 + 5 = {calculadora(10, 5, '+')}")
print(f"10 * 5 = {calculadora(10, 5, '*')}")