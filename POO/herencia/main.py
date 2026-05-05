"""
Concepto de Herencia en Programación Orientada a Objetos (POO)
"""

class Profesion:
    def __init__(self, profesion):
        self.profesion = profesion

    def mostrar_profesion(self):
        print(f"Profesión: {self.profesion}")

class Medico(Profesion):
    def __init__(self, profesion, especialidad):
        super().__init__(profesion)
        self.especialidad = especialidad

    def mostrar_especialidad(self):
        print(f"Especialidad: {self.especialidad}")

cardiologo = Medico("Medico", "Cardiología")
cardiologo.mostrar_especialidad()
cardiologo.mostrar_profesion()