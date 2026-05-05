"""
Aqui voy a importar la clase Estudiante para poder usarla en la clase Docente, esto es necesario porque el docente va a tener una 
lista de estudiantes a su cargo.
"""

if __name__ == "__main__":
    from estudiante import Estudiante
    from docente import Docente

    estudiante1 = Estudiante("Maria", 20, "Ingenieria en Sistemas")
    docente1 = Docente("Dr. Smith", "Programacion")

    estudiante1.matricular()
    estudiante1.ver_informacion()
    estudiante1.actualizar_carrera("Ingenieria en Informatica")
    estudiante1.ver_informacion()

    docente1.calificar(estudiante1, 95)
    estudiante1.ver_calificaciones(docente1, {"Programacion": 95})