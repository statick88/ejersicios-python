#!/usr/bin/env python3
"""
Ejercicio M7.1: Archivos y Persistencia
=======================================

练习: Practicar con archivos

Libro: M7_Archivos.md
"""

import json
import csv
import os

# ==========================================
# Ejercicio 1: Guardar y carregar agenda
# ==========================================

agenda = [
    {"nombre": "Ana", "teléfono": "0991234567"},
    {"nombre": "Bob", "teléfono": "0987654321"},
]

# Guardar como JSON
nombre_archivo = "agenda.json"
with open(nombre_archivo, "w") as f:
    json.dump(agenda, f, indent=2)

print("=== Ejercicio 1: Agenda JSON ===")
print(f"Guardado en: {nombre_archivo}")

# Leer agenda
with open(nombre_archivo, "r") as f:
    agenda_leida = json.load(f)
    for contacto in agenda_leida:
        print(f"{contacto['nombre']}: {contacto['teléfono']}")

# ==========================================
# Ejercicio 2: Exportar a CSV
# ==========================================

with open("agenda.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["Nombre", "Teléfono"])
    for contacto in agenda:
        escritor.writerow([contacto["nombre"], contacto["teléfono"]])

print("\n=== Ejercicio 2: Agenda CSV ===")
print("Archivo CSV creado")

# ==========================================
# Ejercicio 3: Leer CSV
# ==========================================

with open("agenda.csv", "r") as f:
    lector = csv.reader(f)
    next(f)  # Saltar header
    print("Contactos:")
    for nombre, telefono in lector:
        print(f"  {nombre}: {telefono}")

# ==========================================
# DESAFÍO: Backup automático
# ==========================================

# Simular backup (copiar a archivo .bak)
contenido_original = ""
with open("agenda.json", "r") as f:
    contenido_original = f.read()

with open("agenda.json.bak", "w") as f:
    f.write(contenido_original)

print("\n=== Desafío: Backup ===")
print("Backup creado: agenda.json.bak")

# Limpiar archivos de prueba
for archivo in ["datos.txt", "datos.json", "datos.csv", "agenda.json", "agenda.csv", "agenda.json.bak"]:
    if os.path.exists(archivo):
        os.remove(archivo)

print("Archivos de prueba eliminados")