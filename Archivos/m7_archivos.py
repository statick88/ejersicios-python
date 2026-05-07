#!/usr/bin/env python3
"""
Módulo 7: Archivos y Persistencia
================================

Este módulo cubre lectura y escritura de archivos
en Python para persistir datos.

Libro: M7_Archivos.md
"""

# ==========================================
# 1. ESCRIBIR ARCHIVOS
# ==========================================

# Escribir archivo de texto
with open("datos.txt", "w") as archivo:
    archivo.write("Línea 1\n")
    archivo.write("Línea 2\n")

print("=== Escribir_archivos ===")
print("Archivo 'datos.txt' creado")

# ==========================================
# 2. LEER ARCHIVOS
# ==========================================

# Leer todo el archivo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(f"Contenido: {contenido}")

# Leer líneas una por una
with open("datos.txt", "r") as archivo:
    for línea in archivo:
        print(f"Línea: {línea.strip()}")

# ==========================================
# 3. MODO APPEND (AGREGAR)
# ==========================================

with open("datos.txt", "a") as archivo:
    archivo.write("Línea agregada\n")

print("\n=== Modo Append ===")
with open("datos.txt", "r") as archivo:
    print(archivo.read())

# ==========================================
# 4. ARCHIVOS JSON
# ==========================================

import json

# Guardar datos JSON
datos = {"nombre": "Ana", "edad": 30, "ciudades": ["Quito", "Cuenca"]}
with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=2)

print("\n=== JSON ===")
print("Archivo JSON creado")

# Leer JSON
with open("datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)
    print(f"Datos cargados: {datos_cargados}")

# ==========================================
# 5. ARCHIVOS CSV
# ==========================================

import csv

# Escribir CSV
with open("datos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad"])
    escritor.writerow(["Ana", 30])
    escritor.writerow(["Bob", 25])

print("\n=== CSV ===")
print("Archivo CSV creado")

# Leer CSV
with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(f"Fila: {fila}")

# ==========================================
# 6. with (CONTEXTO_manager)
# ==========================================

print("\n=== with (Context Manager) ===")
print("""
withopen("archivo.txt", "r") as f:
    contenido = f.read()
# El archivo se cierra automáticamente
# даже si hay error
""")

# ==========================================
# RESUMEN DEL MÓDULO 7
# ==========================================
"""
Métodos aprendidos:
✓ open("archivo", "w") - escribir
✓ open("archivo", "r") - leer
✓ open("archivo", "a") - agregar
✓ json.dump() / json.load() - JSON
✓ csv.writer() / csv.reader() - CSV
✓ with - context manager (automático)
"""

# Fin del Módulo 7