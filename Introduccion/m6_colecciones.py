#!/usr/bin/env python3
"""
Módulo 6: Colecciones
====================

 Python tiene 4 tipos principales de colecciones:
 - Listas: ordenadas y mutables
 - Tuplas: ordenadas e immutables
 - Diccionarios: clave-valor
 - Sets: sin duplicados

 Ebook: Ver M6_Colecciones.md para teoría completa
"""

# ==========================================
# 1. LISTAS
# ==========================================

# Crear lista
frutas = ["manzana", "banana", "cereza"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", True, 3.14]

# Acceder por índice (0-based)
print(frutas[0])   # manzana
print(frutas[-1])   # cereza (último)

# Modificar
frutas[0] = "pera"
print(frutas)  # ['pera', 'banana', 'cereza']

# Métodos útiles
frutas.append("uva")           # agregar
frutas.insert(1, "naranja")     # insertar en posición
frutas.remove("banana")         # remover por valor
eliminado = frutas.pop()          # remover último
print(frutas)

# Slicing (rebanadas)
print(numeros[1:4])   # [2, 3, 4]
print(numeros[:3])      # [1, 2, 3]
print(numeros[::2])    # [1, 3, 5] (cada 2)

# ==========================================
# 2. TUPLAS
# ==========================================

# Tupla = lista inmutable
coordenadas = (10, 20)
punto = (5, 3, 8)

# Desempaquetar
x, y = coordenadas
print(f"x={x}, y={y}")

# Funciones integradas
print(len(punto))           # 3
print(min(numeros))         # 1
print(max(numeros))         # 5
print(sum(numeros))         # 15

# ==========================================
# 3. DICCIONARIOS
# ==========================================

# Clave-valor
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Quito"
}

# Acceder
print(persona["nombre"])     # Carlos
print(persona.get("edad"))    # 30

# Modificar
persona["edad"] = 31
persona["profesion"] = "ingeniero"

# Keys, values, items
print(persona.keys())    # dict_keys(['nombre', ...])
print(persona.values()) # dict_values(['Carlos', ...])
print(persona.items())  # dict_items([('nombre', 'Carlos'), ...])

# Iterar
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# ==========================================
# 4. SETS
# ==========================================

# Sin duplicados
colores = {"rojo", "verde", "azul", "rojo"}  # solo un rojo
print(colores)  # {'verde', 'azul', 'rojo'}

# Operaciones de conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # {1, 2, 3, 4, 5, 6} (unión)
print(a & b)    # {3, 4} (intersección)
print(a - b)    # {1, 2} (diferencia)
print(a ^ b)    # {1, 2, 5, 6} (diferencia simétrica)

# ==========================================
# 5. COMPREENSIÓN DE LISTAS
# ==========================================

# [expr for var in iterable if condicion]
numeros = [1, 2, 3, 4, 5]

# Cuadrado de cada número
cuadrados = [x**2 for x in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Solo pares
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4]

# Dictionary comprehension
nombres = ["Ana", "Bob", "Carla"]
longitudes = {nombre: len(nombre) for nombre in nombres}
print(longitudes)  # {'Ana': 3, 'Bob': 3, 'Carla': 6}

# ==========================================
# 6. OPERACIONES COMUNES
# ==========================================

# in: verificar existencia
print("manzana" in frutas)
print("nombre" in persona)

# sorted: ordenar
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numeros))           # [1, 1, 2, 3, 4, 5, 6, 9]
print(sorted(numeros, reverse=True))  # [9, 6, 5, 4, 3, 2, 1, 1]

# any/all
print(any([True, False, False]))  # True (al menos uno)
print(all([True, True, True]))   # True (todos)

# enumerate y zip
for i, v in enumerate(frutas):
    print(f"{i}: {v}")

nombres = ["Ana", "Bob"]
edades = [25, 30]
for n, e in zip(nombres, edades):
    print(f"{n}: {e}")

# ==========================================
# RESUMEN DEL MÓDULO 6
# ==========================================
"""
Colecciones aprendidas:
✓ listas []      - mutables, ordenadas
✓ tuplas ()     - immutables
✓ diccionarios {} - clave-valor
✓ sets {}       - sin duplicados

Métodos importantes:
✓ append(), pop()       - listas
✓ get(), keys(), values() - diccionarios
✓ add(), remove()       - sets

Siguiente unidad: M7 - Archivos
Ebook: M7_Archivos.md
"""

# Fin del Módulo 6