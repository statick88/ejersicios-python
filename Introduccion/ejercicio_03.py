#!/usr/bin/env python3
"""
Ejercicio M1.1: Variables y Tipos
==================================

练习: Crear y usar variables de diferentes tipos

Libro: M1_Variables_Tipos.md
"""

# ==========================================
# Ejercicio 1: Variables básicas
# ==========================================

# String (texto)
nombre = "Carlos"
print(f"Nombre: {nombre}")
print(f"Tipo: {type(nombre)}")

# Integer (número entero)
edad = 30
print(f"Edad: {edad}")
print(f"Tipo: {type(edad)}")

# Float (número decimal)
altura = 1.75
print(f"Altura: {altura}")
print(f"Tipo: {type(altura)}")

# Boolean (True/False)
es_estudiante = False
print(f"¿Es estudiante?: {es_estudiante}")
print(f"Tipo: {type(es_estudiante)}")

# ==========================================
# Ejercicio 2: Conversión entre tipos
# ==========================================

# String → Integer
numero_texto = "42"
numero = int(numero_texto)
print(f"String '{numero_texto}' → int {numero}")

# Integer → String
numero = 100
texto = str(numero)
print(f"int {numero} → String '{texto}'")

# String → Float
precio = float("19.99")
print(f"String '19.99' → float {precio}")

# ==========================================
# Ejercicio 3: Verificar tipo
# ==========================================

valor = 42

print(f"Valor: {valor}")
print(f"¿Es int?: {isinstance(valor, int)}")
print(f"¿Es str?: {isinstance(valor, str)}")
print(f"¿Es número?: {isinstance(valor, (int, float))}")

# ==========================================
# DESAFÍO: Crea tu propia agenda
# ==========================================

# Crea variables para:
# - Tu nombre (string)
# - Tu edad (int)
# - Tu nota promedio (float)
# - ¿Te gusta Python? (bool)

# Then printed:
tu_nombre = "Ana"
tu_edad = 22
tu_nota = 8.5
te_gusta = True

print(f"\nMi agenda:")
print(f"Nombre: {tu_nombre}")
print(f"Edad: {tu_edad}")
print(f"Nota: {tu_nota}")
print(f"¿Me gusta Python?: {te_gusta}")