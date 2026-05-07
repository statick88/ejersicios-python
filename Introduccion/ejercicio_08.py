#!/usr/bin/env python3
"""
Ejercicio M6.1: Colecciones
============================

练习: Listas, Tuplas, Diccionarios, Sets

Libro: M6_Colecciones.md
"""

# ==========================================
# 1. LISTAS
# ==========================================

frutas = ["manzana", "banana", "cereza"]
print(f"Lista: {frutas}")

# Acceder elementos
print(f"Primera: {frutas[0]}")
print(f"Última: {frutas[-1]}")

# Métodos
frutas.append("uva")           # agregar
frutas.insert(1, "naranja")    # insertar
frutas.remove("banana")         # remover
print(f"Modificada: {frutas}")

# Slicing (rebanadas)
numeros = [0, 1, 2, 3, 4, 5]
print(f"numeros[1:4]: {numeros[1:4]}")  # [1, 2, 3]
print(f"numeros[:3]: {numeros[:3]}")    # [0, 1, 2]
print(f"numeros[::2]: {numeros[::2]}")  # [0, 2, 4]

# ==========================================
# 2. TUPLAS
# ==========================================

# Tupla = inmutable
coordenadas = (10, 20)
print(f"\nTupla: {coordenadas}")

# Desempaquetar
x, y = coordenadas
print(f"x: {x}, y: {y}")

# ==========================================
# 3. DICCIONARIOS
# ==========================================

persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Quito"
}
print(f"\nDiccionario: {persona}")

# Acceder valores
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")

# Agregar/modificar
persona["profesion"] = "ingeniero"
persona["edad"] = 31
print(f"Modificado: {persona}")

# Iterar
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# ==========================================
# 4. SETS
# ==========================================

colores = {"rojo", "verde", "azul", "rojo"}
print(f"\nSet: {colores}")  # sin duplicados

# Operaciones de conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"A | B (unión): {a | b}")
print(f"A & B (intersección): {a & b}")
print(f"A - B (diferencia): {a - b}")
print(f"A ^ B (diferencia sim): {a ^ b}")

# ==========================================
# 5. COMPREENSIÓN DE LISTAS
# ==========================================

numeros = [1, 2, 3, 4, 5]

# Cuadrados
cuadrados = [x**2 for x in numeros]
print(f"\nCuadrados: {cuadrados}")

# Filtrar
pares = [x for x in numeros if x % 2 == 0]
print(f"Pares: {pares}")

# Dictionary comprehension
palabras = ["hola", "mundo", "python"]
largos = {p: len(p) for p in palabras}
print(f"Largos: {largos}")

# ==========================================
# DESAFÍO: Inventario
# ==========================================

inventario = {
    "manzana": {"cantidad": 10, "precio": 0.50},
    "banana": {"cantidad": 5, "precio": 0.30},
    "cereza": {"cantidad": 20, "precio": 1.00}
}

# Calcular valor total
valor_total = sum(item["cantidad"] * item["precio"] 
               for item in inventario.values())
print(f"\nValor total inventario: ${valor_total:.2f}")

# Agregar nueva fruta
inventario["uva"] = {"cantidad": 15, "precio": 0.80}
print(f"Inventario actualizado: {len(inventario)} artículos")