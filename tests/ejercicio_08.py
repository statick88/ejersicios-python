#!/usr/bin/env python3
"""
Ejercicio M9.1: Testing y QA
==============================

练习: Practicar testing con pytest

Libro: M9_Testing.md
"""

# ==========================================
# Ejercicio 1: Test básico
# ==========================================

def es_par(numero):
    """Verifica si número es par."""
    return numero % 2 == 0

print("=== Ejercicio 1: Test Básico ===")

# Verificar con assert
assert es_par(4) == True, "4 debe ser par"
assert es_par(3) == False, "3 debe ser impar"
assert es_par(0) == True, "0 es par"
print("Tests pasaron!")

# ==========================================
# Ejercicio 2: Test de calculadora
# ==========================================

class Calculadora:
    """Calculadora simple."""
    
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

print("\n=== Ejercicio 2: Tests de Calculadora ===")

calc = Calculadora()

# Tests
assert calc.sumar(2, 3) == 5
assert calc.restar(10, 5) == 5
assert calc.multiplicar(3, 4) == 12
assert calc.dividir(10, 2) == 5

try:
    calc.dividir(10, 0)
    assert False, "Debió lanzar error"
except ValueError:
    print("Manejo de error: OK")

print("Todos los tests pasaron!")

# ==========================================
# Ejercicio 3: Test con pytest
# ==========================================

print("\n=== Ejercicio 3: Con pytest ===")
print("""
# Archivo test_ejemplo.py

def test_es_par():
    assert es_par(4) == True
    assert es_par(3) == False

def test_calculadora():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5
    assert calc.dividir(10, 2) == 5
""")

# ==========================================
# DESAFÍO: Test integrador
# ==========================================

class ValidarEmail:
    """Validador de emails."""
    
    def es_valido(self, email):
        """Verifica si email es válido."""
        if not email:
            return False
        if "@" not in email:
            return False
        if "." not in email:
            return False
        return True

print("\n=== Desafío: Validar Email ===")

validador = ValidarEmail()

# Tests básicos
assert validador.es_valido("ana@correo.com") == True
assert validador.es_valido("invalid") == False
assert validador.es_valido("") == False
assert validador.es_valido("sin@arroba") == False

print("Todos los tests de email pasaron!")

# Ejecutar con pytest:
# pip install pytest
# pytest test_ejercicio.py -v