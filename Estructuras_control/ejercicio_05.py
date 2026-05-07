#!/usr/bin/env python3
"""
Ejercicio M3.1: Control de Flujo
================================

练习: if/elif/else, for, while

Libro: M3_Control_Flujo.md
"""

# ==========================================
# 1. CONDICIONALES: if/elif/else
# ==========================================

nota = 85

if nota >= 90:
    print("Excelente: A")
elif nota >= 80:
    print("Muy bien: B")
elif nota >= 70:
    print("Bien: C")
elif nota >= 60:
    print("Aprobado: D")
else:
    print("Reprobado: F")

# ==========================================
# 2. BUCLE: for
# ==========================================

print("\n--- for con range ---")
for i in range(1, 6):
    print(f"Número: {i}")

print("\n--- for con lista ---")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

print("\n--- for con enumerate ---")
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# ==========================================
# 3. BUCLE: while
# ==========================================

print("\n--- while ---")
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

# ==========================================
# 4. break y continue
# ==========================================

print("\n--- break (detener) ---")
for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ")
print(" ← se detuvo en 5")

print("\n--- continue (saltar) ---")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print(" ← saltó el 3")

# ==========================================
# 5. List Comprehension
# ==========================================

print("\n--- List Comprehension ---")
numeros = [1, 2, 3, 4, 5]

# Cuadrados
cuadrados = [x**2 for x in numeros]
print(f"Cuadrados: {cuadrados}")

# Solo pares
pares = [x for x in numeros if x % 2 == 0]
print(f"Pares: {pares}")

# ==========================================
# DESAFÍO: Tabla de multiplicar
# ==========================================

def tabla_multiplicar(numero, limite=10):
    """Imprime la tabla de multiplicar"""
    print(f"\nTabla del {numero}:")
    for i in range(1, limite + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabla_multiplicar(7)