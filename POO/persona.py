"""
Crear una clase persona
Crear al menos 3 atributos
Crear al menos 1 metodo saludar
Crear una instancia de la clase persona y llamar al metodo saludar
"""

class Persona:
    """Clase Persona con atributos y métodos básicos"""

    def __init__(self, nombre, edad, carrera):
        """Constructor de la clase Persona"""
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def __str__(self):
        """Metodo para mostrar la informacion de la persona"""
        return f"Persona: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera} tiene el metodo saludar: {self.saludar()}"

    def saludar(self):
        """Método para saludar a otra persona"""
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años. Estudio {self.carrera}.")


estudiante1 = Persona("Maria", 20, "Ingenieria en Sistemas")
#estudiante1.saludar()

print(estudiante1.__str__())