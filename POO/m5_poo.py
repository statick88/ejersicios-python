#!/usr/bin/env python3
"""
Módulo 5: POO - Programación Orientada a Objetos
===========================================

 POO es un paradigma que usa "objetos" para representar
 datos y funcionalidades. Los objetos tienen:
 - atributos (datos)
 - métodos (funciones)

 Este módulo cubré:
 - Clases y objetos
 - Constructor __init__
 - Herencia
 - Encapsulación

 Ebook: Ver M5_POO.md para teoría completa
"""

# ==========================================
# 1. DEFINIR UNA CLASE
# ==========================================

class Persona:
    """Una persona con nombre y edad"""
    
    # Constructor: inicializa el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre    # atributo
        self.edad = edad      # atributo
    
    # Método: función dentro de clase
    def saludar(self):
        return f"Hola, soy {self.nombre}"

# Crear objeto (instancia)
persona1 = Persona("Carlos", 30)
print(persona1.saludar())


# ==========================================
# 2. ATRIBUTOS Y MÉTODOS
# ==========================================

class Calculadora:
    """Calculadora simple"""
    
    def __init__(self):
        self.resultado = 0
    
    def sumar(self, num):
        self.resultado += num
        return self
    
    def restar(self, num):
        self.resultado -= num
        return self
    
    def obtener(self):
        return self.resultado

# Encadenar operaciones (method chaining)
calc = Calculadora()
calc.sumar(10).restar(3).sumar(5)
print(f"Resultado: {calc.obtener()}")  # 12


# ==========================================
# 3. HERENCIA
# ==========================================

# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "..."
    
    def mostrar(self):
        return f"{self.nombre} hace: {self.hacer_sonido()}"


# Clase hija hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"


# Usar herencia
animales = [Perro("Buddy"), Gato("Whiskers")]
for a in animales:
    print(a.mostrar())


# ==========================================
# 4. ENCAPSULACIÓN (PROTEGER DATOS)
# ==========================================

class CuentaBancaria:
    """Cuenta con saldo protegido"""
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # __ = privado
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return True
        return False
    
    def consultar(self):
        return f"Saldo: ${self.__saldo}"
    
    def get_saldo(self):  # getter
        return self.__saldo


cuenta = CuentaBancaria("Carlos", 1000)
cuenta.depositar(500)
print(cuenta.consultar())
# print(cuenta.__saldo)  # Error! Es privado


# ==========================================
# 5. POLIMORFISMO
# ==========================================

class Archivo:
    def abrir(self):
        return "Abriendo archivo..."
    
    def cerrar(self):
        return "Cerrando archivo..."


class PDF(Archivo):
    def abrir(self):
        return "Abriendo PDF en visor..."


class DOC(Archivo):
    def abrir(self):
        return "Abriendo en Word..."


# Mismo método, diferente comportamiento
for archivo in [Archivo(), PDF(), DOC()]:
    print(archivo.abrir())


# ==========================================
# 6. __STR__ Y __REPR__
# ==========================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        """Para usuarios"""
        return f"Persona({self.nombre}, {self.edad})"
    
    def __repr__(self):
        """Para desarrolladores"""
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"


p = Persona("Ana", 25)
print(str(p))   # Persona(Ana, 25)
print(repr(p))  # Persona(nombre='Ana', edad=25)


# ==========================================
# RESUMEN DEL MÓDULO 5
# ==========================================
"""
POO aprendido:
✓ class           - definir clase
✓ __init__       - constructor
✓ self           - referencia al objeto
✓ atributos      - datos del objeto
✓ métodos        - funciones del objeto
✓ herencia      - clase hija de padre
✓ encapsulación  - datos privados (__)
✓ polimorfismo   - mismo método, diferente comportamiento
✓ __str__, __repr__ - representación

Siguiente unidad: M6 - Colecciones
Ebook: M6_Colecciones.md
"""

# Fin del Módulo 5