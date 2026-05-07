#!/usr/bin/env python3
"""
Ejercicio M7.1: Archivos y Persistencia
===================================

练习: Leer y escribir archivos

Libro: M7_Archivos.md
"""

import os
import json
import csv

# ==========================================
# 1. ESCRIBIR ARCHIVO DE TEXTO
# ==========================================

contenido = """Línea 1
Línea 2
Línea 3
"""

with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

print("1. Archivo de texto creado")

# ==========================================
# 2. LEER ARCHIVO DE TEXTO
# ==========================================

with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()
    print(f"2. Contenido: {repr(texto)}")

# ==========================================
# 3. LEER LÍNEA POR LÍNEA
# ==========================================

with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(f"   Línea: {linea.strip()}")

# ==========================================
# 4. ARCHIVOS JSON
# ==========================================

datos = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Quito"
}

# Escribir JSON
with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=2)

print("\n4. Archivo JSON creado")

# Leer JSON
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos_leidos = json.load(archivo)
    print(f"   Leído: {datos_leidos}")

# ==========================================
# 5. ARCHIVOS CSV
# ==========================================

datos_csv = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", "25", "Quito"],
    ["Bob", "30", "Guayaquil"],
    ["Carla", "28", "Cuenca"]
]

# Escribir CSV
with open("personas.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos_csv)

print("5. Archivo CSV creado")

# Leer CSV
with open("personas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(f"   {fila}")

# ==========================================
# 6. MANEJO DE ERRORES
# ==========================================

try:
    with open("no_existe.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("\n6. Error: Archivo no encontrado")

# ==========================================
# LIMPIAR ARCHIVOS
# ==========================================

archivos_temporales = ["ejemplo.txt", "datos.json", "personas.csv"]
for archivo in archivos_temporales:
    if os.path.exists(archivo):
        os.remove(archivo)

print("7. Archivos temporales eliminados")