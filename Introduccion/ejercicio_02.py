#!/usr/bin/env python3
"""
Ejercicio M0.2: Comentarios
==========================

练习: Usar comentarios correctamente

Libro: M0_Pensamiento_Computacional.md
"""

# Este es un comentario de una línea

# ==========================================
# Sección 1: Comentarios informativos
# ==========================================
# Autor: Tu nombre
# Fecha: 2026
# Propósito: Aprender Python

"""
Este es un comentario
de múltiples líneas
"""

# ==========================================
# Sección 2: Comentar código temporalmente
# ==========================================
# print("Esto está comentado")
print("Esto sí se ejecuta")

# ==========================================
# Sección 3: Docstrings
# ==========================================
def saludar():
    """Esta función salute al usuario"""
    print("¡Hola!")
    return "Función ejecutada"

resultado = saludar()
print(f"Resultado: {resultado}")

# ==========================================
# EJERCICIO: Escribe tu propio comentario
# ==========================================
# Escribe tu nombre, fecha y objetivo aquí:
# 

print("¡Ejercicio completado!")