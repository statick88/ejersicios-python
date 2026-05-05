"""
Ejemplo de Polimorfismo con animales
"""

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
# Función que utiliza polimorfismo
def escuchar_animal(animal):
    print(animal.hacer_sonido())
# Ejemplo de uso
perro = Perro()
gato = Gato()

escuchar_animal(perro)  # Salida: Guau
escuchar_animal(gato)   # Salida: Miau