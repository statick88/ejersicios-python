# Agregar una entrada al diario sin borrar las anteriores
with open("mi_diario.txt", "a") as archivo:
    archivo.write("Día 4: Hoy aprendí a escribir archivos\n")
    archivo.write("Fue más fácil de lo que pensé\n")