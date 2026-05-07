#!/usr/bin/env python3
"""
Ejercicio M9.1: Testing con pytest
=====================================

练习: escribir pruebas unitarias

Libro: M9_Testing.md

Para ejecutar: pytest ejercicio_11.py -v
"""

import pytest

# ==========================================
# 1. Pruebas básicas con assert
# ==========================================

def sumar(a, b):
    """Suma dos números"""
    return a + b

# Pruebas
assert sumar(2, 3) == 5, "2 + 3 debe ser 5"
assert sumar(-1, 1) == 0, "-1 + 1 debe ser 0"
assert sumar(0, 0) == 0, "0 + 0 debe ser 0"

print("1. Pruebas de sumar() pasaron")

# ==========================================
# 2. Funciones de prueba
# ==========================================

def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-1, 1) == 0

def test_sumar_ceros():
    assert sumar(0, 0) == 0

# ==========================================
# 3. pytest con assertRaises
# ==========================================

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se divide entre cero")
    return a / b

def test_dividir_entre_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

def test_dividir_normal():
    assert dividir(10, 2) == 5

# ==========================================
# 4. Fixtures
# ==========================================

import json

@pytest.fixture
def datos_json():
    """Fixture que retorna datos JSON"""
    return {"nombre": "Carlos", "edad": 30}

def test_fixture(datos_json):
    assert datos_json["nombre"] == "Carlos"
    assert datos_json["edad"] == 30

# ==========================================
# 5. Parametrized Tests
# ==========================================

@pytest.mark.parametrize("entrada, esperado", [
    ((2, 3), 5),
    ((-1, 1), 0),
    ((0, 0), 0),
    ((10, -5), 5),
])
def test_sumar_parametrizado(entrada, esperado):
    assert sumar(entrada[0], entrada[1]) == esperado

# ==========================================
# 6. test de clase
# ==========================================

class TestOperaciones:
    
    def test_restar(self):
        def restar(a, b):
            return a - b
        assert restar(5, 3) == 2
    
    def test_multiplicar(self):
        def multiplicar(a, b):
            return a * b
        assert multiplicar(3, 4) == 12

# ==========================================
# EJECUTAR TESTS
# ==========================================

if __name__ == "__main__":
    print("\nEjecutando tests manualmente...")
    test_sumar_positivos()
    test_sumar_negativos()
    test_dividir_normal()
    print("✓ Todos los tests pasaron")
    
    # Para ejecutar con pytest:
    # pytest ejercicio_11.py -v