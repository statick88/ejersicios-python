#!/usr/bin/env python3
"""
Ejercicio M5.1: POO - Clases y Objetos
====================================

练习: Programación Orientada a Objetos

Libro: M5_POO.md
"""

# ==========================================
# 1. Clase básica
# ==========================================

class Persona:
    """Una persona con nombre y edad"""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    def cumple_anos(self):
        self.edad += 1
        return f"Ahora tengo {self.edad} años"

# Crear objeto
persona = Persona("Carlos", 30)
print(persona.saludar())
print(persona.cumple_anos())

# ==========================================
# 2. Herencia
# ==========================================

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "..."

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Usar herencia
animales = [Perro("Buddy"), Gato("Whiskers")]
for animal in animales:
    print(f"{animal.nombre}: {animal.hacer_sonido()}")

# ==========================================
# 3. Encapsulación (datos privados)
# ==========================================

class Cuenta:
    def __init__(self, saldo=0):
        self.__saldo = saldo  # privado
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return True
        return False
    
    def get_saldo(self):
        return self.__saldo

cuenta = Cuenta(1000)
cuenta.depositar(500)
print(f"\nSaldo: ${cuenta.get_saldo()}")

# ==========================================
# 4. Polimorfismo
# ==========================================

class Ave:
    def volar(self):
        return "Las aves vuelan"

class Pinguino(Ave):
    def volar(self):
        return "Los pingüinos no vuelan"

aves = [Ave(), Pinguino()]
for ave in aves:
    print(ave.volar())

# ==========================================
# 5. Métodos especiales
# ==========================================

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"
    
    def __repr__(self):
        return f"Libro(titulo='{self.titulo}')"
    
    def __len__(self):
        return self.paginas

libro =Libro("Cien años", "García Márquez", 300)
print(f"\n{libro}")
print(f"Páginas: {len(libro)}")

# ==========================================
# DESAFÍO: Sistema de empleados
# ==========================================

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario
    
    def get_salario(self):
        return self.__salario
    
    def calcular_bono(self, porcentaje):
        return self.__salario * porcentaje

emp = Empleado("Ana", 1000)
print(f"\nEmpleado: {emp.nombre}")
print(f"Salario: ${emp.get_salario()}")
print(f"Bono 10%: ${emp.calcular_bono(0.10)}")