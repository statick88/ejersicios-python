"""
Herencia Multinivel: En un ejemplo con animales, 
clase animal, clase mamifero, clase perro, 
la clase perro hereda de la clase mamifero y 
la clase mamifero hereda de la clase animal. 
La clase perro puede acceder a los métodos y 
atributos de ambas clases, mamifero y animal.
"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Mamifero(Animal):
    def __init__(self, nombre, tipo_pelo):
        super().__init__(nombre)
        self.tipo_pelo = tipo_pelo

    def amamantar(self):
        print(f"{self.nombre} está amamantando a sus crías.")

class Perro(Mamifero):
    def __init__(self, nombre, tipo_pelo, raza):
        super().__init__(nombre, tipo_pelo)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

perro1 = Perro("Firulais", "Corto", "Labrador")
perro1.ladrar()
perro1.amamantar()
perro1.comer()