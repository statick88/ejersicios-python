#!/usr/bin/env python3
"""
Módulo 3: Control de Flujo
=======================

 Este módulo cubré cómo controlar el flujo del programa:
 - Condicionales (if, elif, else)
 - Bucles (for, while)
 - Control de bucles (break, continue)

 Ebook: Ver M3_Control_Flujo.md para teoría completa
"""

# ==========================================
# 1. CONDICIONAL: if / elif / else
# ==========================================

edad = 18

# if: ejecutar si la condición es True
if edad >= 18:
    print("Eres mayor de edad")

# if...else: dos caminos
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# if...elif...else: múltiples condiciones
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")

# ==========================================
# 2. OPERADORES EN CONDICIONES
# ==========================================

usuario = "admin"
password = "1234"

# and: ambas condiciones deben cumplirse
if usuario == "admin" and password == "1234":
    print("¡Bienvenido, admin!")

# or: al menos una condición
rol = "invitado"
if rol == "admin" or rol == "editor":
    print("Tienes acceso completo")
else:
    print("Acceso limitado")

# ==========================================
# 3. BUCLE: for
# ==========================================

# for variable in secuencia:
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(f"Fruta: {fruta}")

# range(inicio, fin, paso)
print("\nNúmeros del 1 al 5:")
for i in range(1, 6):
    print(i)

# enumerate: obtener índice y valor
print("\nCon índice:")
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# ==========================================
# 4. BUCLE: while
# ==========================================

# while condición: ejecutar mientras sea True
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# ==========================================
# 5. CONTROL DE BUCLES
# ==========================================

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# break: salir del bucle inmediatamente
print("\nCon break (detener en 5):")
for n in numeros:
    if n > 5:
        break
    print(n, end=" ")
# Salida: 1 2 3 4 5

# continue: pasar a la siguiente iteración
print("\n\nCon continue (saltar impares):")
for n in numeros:
    if n % 2 == 1:  # impar
        continue    # saltamos
    print(n, end=" ")
# Salida: 2 4 6 8 10

# ==========================================
# 6. COMPRESIÓN DE LISTAS (LIST COMP)
# ==========================================

# [expresión for variable in iterable if condición]
cuadrados = [x**2 for x in range(1, 6)]
print(f"\nCuadrados: {cuadrados}")  # [1, 4, 9, 16, 25]

pares = [x for x in range(10) if x % 2 == 0]
print(f"Pares: {pares}")  # [0, 2, 4, 6, 8]

# ==========================================
# RESUMEN DEL MÓDULO 3
# ==========================================
"""
Control de flujo aprendido:
✓ if / elif / else   - decisiones
✓ for               - iterar sobre secuencia
✓ while             - iterar mientras condición
✓ break             - salir del bucle
✓ continue          - siguiente iteración
✓ list comprehension - crear listas cortas

Siguiente unidad: M4 - Funciones
Ebook: M4_Funciones.md
"""

# Fin del Módulo 3