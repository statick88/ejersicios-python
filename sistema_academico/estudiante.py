class Estudiante:
    
    def __init__(self, nombre, edad, carrera):
        """Constructor de la clase Estudiante"""
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def matricular(self):
        """Método para matricular al estudiante"""
        print(f"{self.nombre} ha sido matriculado en la carrera de {self.carrera}")

    def ver_informacion(self):
        """Método para mostrar la información del estudiante"""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")

    def actualizar_carrera(self, nueva_carrera):
        """Método para actualizar la carrera del estudiante"""
        self.carrera = nueva_carrera
        print(f"{self.nombre} ha actualizado su carrera a {self.carrera}")

    def ver_calificaciones(self, docente, calificaciones):
        """Método para mostrar las calificaciones del estudiante"""
        print(f"Calificaciones de {self.nombre}:")
        for asignatura, calificacion in calificaciones.items():
            print(f"{asignatura}: {calificacion}")
