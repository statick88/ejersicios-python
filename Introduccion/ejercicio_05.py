#!/usr/bin/env python3
"""
Ejercicio M6.1: Colecciones
=============================

练习: Practicar colecciones en Python

Libro: M6_Colecciones.md
"""

# ==========================================
#Ejercicio 1: Listas
# ==========================================

# Crear lista de números
numeros = [1, 2, 3, 4, 5]
print("=== Listas ===")
print(f"Números: {numeros}")

# Agregar número
numeros.append(6)
print(f"Después de append: {numeros}")

# Ordenar
numeros.sort(reverse=True)
print(f"Ordenado (desc): {numeros}")

# ==========================================
# Ejercicio 2: Diccionarios
# ==========================================

estudiante = {
    "nombre": "Carlos",
    "notas": [8.5, 9.0, 7.5]
}
print("\n=== Diccionarios ===")
print(f"Estudiante: {estudiante}")

# Calcular promedio
promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
print(f"Promedio: {promedio:.2f}")

# ==========================================
# Ejercicio 3: Conjuntos
# ==========================================

# Eliminar duplicados
nombres = ["Ana", "Bob", "Ana", "Carol", "Bob", "Ana"]
unicos = set(nombres)
print("\n=== Conjuntos ===")
print(f"Original: {nombres}")
print(f"Únicos: {unicos}")

# ==========================================
# DESAFÍO: Agenda de contactos
# ==========================================

contactos = [
    {"nombre": "Ana", "teléfono": "0991234567"},
    {"nombre": "Bob", "teléfono": "0987654321"},
    {"nombre": "Ana", "teléfono": "0991234567"}  # duplicado
]

# Eliminar duplicados por nombre
nombres_unicos = set(c["nombre"] for c in contactos)
print(f"\n=== Agenda ===")
for nombre in nombres_unicos:
    for c in contactos:
        if c["nombre"] == nombre:
            print(f"{nombre}: {c['teléfono']}")
            break