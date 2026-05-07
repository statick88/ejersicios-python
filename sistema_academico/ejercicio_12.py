#!/usr/bin/env python3
"""
Ejercicio M10.1: Proyecto Integrador
=====================================

练习: Proyecto que integra todos los conceptos

Libro: M10_Proyecto_Integrador.md
"""

# ==========================================
# PROYECTO: Sistema de Gestión de Tareas
# ==========================================

class Tarea:
    """Una tarea pendiente"""
    def __init__(self, titulo, descripcion="", prioridad=1):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
    
    def __str__(self):
        estado = "✓" if self.completada else " "
        return f"[{estado}] {self.titulo} (Prioridad: {self.prioridad})"
    
    def completar(self):
        self.completada = True


class GestorTareas:
    """Gestor de tareas"""
    def __init__(self):
        self.tareas = []
    
    def agregar(self, tarea):
        self.tareas.append(tarea)
    
    def completar(self, titulo):
        for t in self.tareas:
            if t.titulo == titulo:
                t.completar()
                return True
        return False
    
    def pendientes(self):
        return [t for t in self.tareas if not t.completada]
    
    def completar_todas(self):
        for t in self.tareas:
            t.completar()
    
    def __str__(self):
        lineas = ["=" * 40, "GESTOR DE TAREAS", "=" * 40]
        for i, tarea in enumerate(self.tareas, 1):
            lineas.append(f"{i}. {tarea}")
        lineas.append("=" * 40)
        lineas.append(f"Total: {len(self.tareas)} | "
                    f"Pendientes: {len(self.pendientes())}")
        return "\n".join(lineas)


# ==========================================
# USAR EL SISTEMA
# ==========================================

gestor = GestorTareas()

# Agregar tareas
gestor.agregar(Tarea("Estudiar Python", "Revisar M0-M5", 3))
gestor.agregar(Tarea("Hacer ejercicios", "Completar todos los labs", 2))
gestor.agregar(Tarea("Crear proyecto final", "Aplicar todos los conceptos", 1))

# Mostrar todas
print(gestor)

# Completar una tarea
gestor.completar("Estudiar Python")

# Mostrar pendientes
print("\nTareas pendientes:")
for t in gestor.pendientes():
    print(f"  - {t}")

# Completar todas
gestor.completar_todas()
print(f"\n¡Todas las tareas completadas!")

# ==========================================
# GUARDAR EN ARCHIVO (Persistencia - M7)
# ==========================================

import json

def guardar_tareas(gestor, archivo):
    """Guardar tareas en JSON"""
    datos = []
    for t in gestor.tareas:
        datos.append({
            "titulo": t.titulo,
            "descripcion": t.descripcion,
            "prioridad": t.prioridad,
            "completada": t.completada
        })
    with open(archivo, "w") as f:
        json.dump(datos, f, indent=2)
    print(f"\n✓ Tareas guardadas en {archivo}")

def cargar_tareas(archivo):
    """Cargar tareas desde JSON"""
    with open(archivo, "r") as f:
        datos = json.load(f)
    
    gestor = GestorTareas()
    for d in datos:
        tarea = Tarea(d["titulo"], d["descripcion"], d["prioridad"])
        tarea.completada = d["completada"]
        gestor.agregar(tarea)
    return gestor

# Guardar
guardar_tareas(gestor, "tareas.json")

# Cargar
gestor2 = cargar_tareas("tareas.json")
print(f"\n✓ Tareas cargadas: {len(gestor2.tareas)}")

# Limpiar
import os
os.remove("tareas.json")

print("\n¡Proyecto completado!")