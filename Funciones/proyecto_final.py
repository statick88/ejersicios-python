#!/usr/bin/env python3
"""
Módulo 10: Proyecto Integrador
================================

Este módulo combina todos los conceptos aprendidos
para crear un proyecto completo.

Libro: M10_Proyecto_Integrador.md
"""

# ==========================================
# PROYECTO: Sistema de Gestión de Tareas
# ==========================================

class Tarea:
    """Representa una tarea."""
    
    def __init__(self, titulo, descripcion=""):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
    
    def completar(self):
        self.completada = True
    
    def __str__(self):
        estado = "✓" if self.completada else "○"
        return f"[{estado}] {self.titulo}"


class GestorTareas:
    """Gestor de tareas."""
    
    def __init__(self):
        self.tareas = []
    
    def agregar(self, titulo, descripcion=""):
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        return tarea
    
    def completar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completar()
    
    def mostrar(self):
        print("\n=== Mis Tareas ===")
        for i, tarea in enumerate(self.tareas):
            print(f"{i + 1}. {tarea}")
        print(f"Total: {len(self.tareas)} tareas")


# ==========================================
# Uso del proyecto
# ==========================================

gestor = GestorTareas()

# Agregar tareas
gestor.agregar("Aprender Python", "Estudiar los 11 módulos")
gestor.agregar("Hacer ejercicios", "Practicar código")
gestor.agregar("Crear proyecto final", "Aplicar todos los conceptos")

# Mostrar
gestor.mostrar()

# Completar segunda tarea
gestor.completar(1)

# Mostrar final
gestor.mostrar()

# ==========================================
# RESUMEN DEL MÓDULO 10
# ==========================================
"""
Este proyecto integrador combina:
✓ Variables y tipos (M1)
✓ Operadores (M2)
✓ Control de flujo (M3)
✓ Funciones (M4)
✓ POO (M5)
✓ Colecciones (M6)

¡Felicidades! Has completado el curso de Python.
"""

# Fin del Módulo 10