from estudiante import Estudiante

class Docente:
    def __init__(self, nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura

    def calificar(self, estudiante, calificacion):
        print(f"{self.nombre} ha calificado a {estudiante.nombre} con una calificación de {calificacion} en la asignatura de {self.asignatura}")


