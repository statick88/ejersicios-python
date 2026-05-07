#!/usr/bin/env python3
"""
Módulo 6: Colecciones
=====================

Colecciones en Python:
- Listas (list) - secuencias mutables
- Tuplas (tuple) -secuencias inmutables
- Conjuntos (set) - elementos únicos
- Diccionarios (dict) - clave-valor

Libro: M6_Colecciones.md
"""

# ==========================================
# 1. LISTAS
# ==========================================

frutas = ["manzana", "plátano", "cereza"]
print(f"Lista: {frutas}")

# Agregar
frutas.append("uva")
print(f"Después de append: {frutas}")

# Acceder por índice
print(f"Primera fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")

# Slice (rebanada)
print(f"Primeras 2: {frutas[:2]}")

# Longitud
print(f"Longitud: {len(frutas)}")

# ==========================================
# 2. TUPLAS
# ==========================================

# Tupla - inmutable
coordenadas = (10, 20)
print(f"\nTupla: {coordenadas}")
print(f"X: {coordenadas[0]}, Y: {coordenadas[1]}")

# Desempaquetado
x, y = coordenadas
print(f"Desempaquetado: x={x}, y={y}")

# ==========================================
# 3. CONJUNTOS (SET)
# ==========================================

colores = {"rojo", "verde", "azul", "rojo"}
print(f"\nSet (sin duplicados): {colores}")

# Agregar
colores.add("amarillo")
print(f"Después de add: {colores}")

# Operaciones de conjuntos
otros = {"azul", "negro", "blanco"}
print(f"Unión: {colores | otros}")
print(f"Intersección: {colores & otros}")
print(f"Diferencia: {colores - otros}")

# ==========================================
# 4. DICCIONARIOS
# ==========================================

persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Quito"
}
print(f"\nDiccionario: {persona}")

# Acceder valores
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")

# Agregar/modificar
persona["profesión"] = "Ingeniera"
print(f"Después de agregar: {persona}")

# Keys y values
print(f"Keys: {persona.keys()}")
print(f"Values: {persona.values()}")

# ==========================================
# RESUMEN
# ==========================================
"""
Colecciones aprendidas:
✓ list    - [...] mutable, ordenada, duplicados
✓ tuple   - (...) inmutable
✓ set     - {...} único, sin orden
✓ dict    - {clave: valor} clave-valor

Métodos importantes:
- list: append(), extend(), pop(), remove()
- set: add(), remove(), union(), intersection()
- dict: keys(), values(), items(), get()
"""

# Fin del Módulo 6