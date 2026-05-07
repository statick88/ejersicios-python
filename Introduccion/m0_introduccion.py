#!/usr/bin/env python3
"""
Módulo 0: Introducción a Python
==========================

 Este módulo cubre los fundamentos básicos de Python:
 - Tu primer programa
 - Cómo executar código
 - Comentarios
 - Variables básicas

 Ebook: Ver M0_Pensamiento_Computacional.md para teoría completa
"""

# ==========================================
# 1. TU PRIMER PROGRAMA EN PYTHON
# ==========================================

# La función print() muestra texto en pantalla
# Este es tu primer programa real
print("¡Hola, Mundo!")

# También puedes usar comillas simples
print('Bienvenido a Python')

# ==========================================
# 2. COMENTARIOS EN CÓDIGO
# ==========================================

# Los comentarios start with # (almohadilla/gato)
# Python ignora todo lo que sigue después de #

# Comentario de una línea
# Otra línea de comentario

"""
Comentarios de múltiples líneas
se escriben entre triple comilla
(no exécut代 en este caso)
"""

# ==========================================
# 3. VARIABLES BÁSICAS
# ==========================================

# Una variable es un contenedor para guardar datos
nombre = "Ana"           # Texto (string/cadena)
edad = 25                  # Número entero (integer)
altura = 1.65             # Número decimal (float)
es_estudiante = True        # Boolean (True/False)

# Mostrar variables
print(nombre)
print(edad)
print(altura)
print(es_estudiante)

# ==========================================
# 4. PEDIR DATOS AL USUARIO
# ==========================================

# input() permite pedir datos al usuario
# El texto dentro de input() es la pregunta
# nombre = input("¿Cómo te llamas? ")
# print(f"Hola, {nombre}!")

# ==========================================
# 5. TYPE() - VERIFICAR TIPO DE DATO
# ==========================================

# type() muestra el tipo de dato
print(type("Hola"))        # <class 'str'>
print(type(42))          # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))        # <class 'bool'>

# ==========================================
# RESUMEN DEL MÓDULO 0
# ==========================================
"""
Conceptos aprendidos:
✓ print()    - Mostrar en pantalla
✓ input()   - Pedir datos al usuario
✓ type()     - Verificar tipo de dato
✓ Variables - Contenedores de datos
✓ Comentarios - Notas en el código

Siguiente unidad: M1 - Variables y Tipos
Ebook: M1_Variables_Tipos.md
"""

# Fin del Módulo 0