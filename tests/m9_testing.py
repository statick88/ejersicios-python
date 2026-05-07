#!/usr/bin/env python3
"""
Módulo 9: Testing y QA
========================

Este módulo cubre testing básico con pytest
para asegurar calidad del código.

Libro: M9_Testing.md
"""

# ==========================================
# 1. ASSERT (VERIFICACIÓN BÁSICA)
# ==========================================

print("=== Assert Básico ===")

def suma(a, b):
    return a + b

# Verificaciones simples
assert suma(2, 3) == 5, "2 + 3 debe ser 5"
assert suma(-1, 1) == 0, "-1 + 1 debe ser 0"
print("¡Todas las aserciones pasaron!")

# ==========================================
# 2. PYTEST - TESTS BÁSICOS
# ==========================================

print("\n=== pytest Tests ===")

# Instalar: pip install pytest
# Ejecutar: pytest archivo.py -v

def test_suma():
    """Test de función suma."""
    assert suma(2, 3) == 5
    assert suma(0, 0) == 0
    assert suma(-1, 1) == 0

def test_resta():
    """Test de función resta."""
    def resta(a, b):
        return a - b
    assert resta(5, 3) == 2
    assert resta(10, 5) == 5

# ==========================================
# 3. FIXTURES (SETUP/TEARDOWN)
# ==========================================

print("\n=== Fixtures ===")
print("""
# Ejemplo de fixture
import pytest

@pytest.fixture
def lista_vacia():
    return []

def test_agregar(lista_vacia):
    lista_vacia.append(1)
    assert len(lista_vacia) == 1
""")

# ==========================================
# 4. TEST PARAMETERIZED
# ==========================================

print("\n=== Parametrized Tests ===")
print("""
# Tests con múltiples valores
import pytest

@pytest.mark.parametrize("entrada,esperado", [
    (2, 4),
    (3, 9),
    (0, 0),
])
def test_cuadrado(entrada, esperado):
    assert entrada ** 2 == esperado
""")

# ==========================================
# 5. MOKS (SIMULACIONES)
# ==========================================

print("\n=== Mocks ===")
print("""
# Simular comportamiento
from unittest.mock import Mock

# Crear mock
api = Mock()
api.get_user.return_value = {"nombre": "Ana"}

# Usar
resultado = api.get_user()
assert resultado["nombre"] == "Ana"
""")

# ==========================================
# RESUMEN DEL MÓDULO 9
# ==========================================
"""
Herramientas aprendidas:
✓ assert - verificación básica
✓ pytest - framework de testing
✓ @pytest.fixture - setup/teardown
✓ @pytest.mark.parametrize - tests múltiples valores
✓ unittest.mock - simular dependencias
✓ pytest -v - verbose output
✓ pytest --cov - coverage

Comandos útiles:
✓ pytest archivo.py - ejecutar tests
✓ pytest archivo.py -v - verbose
✓ pytest --cov=carpeta - coverage report
"""

# Fin del Módulo 9