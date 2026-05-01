try:
    with open("reporte_final.txt", "x") as archivo:
        archivo.write("Reporte generado el 2026-04-30\n")
        print("Archivo creado exitosamente")
except FileExistsError:
    print("Error: El archivo 'reporte_final.txt' ya existe")
    print("Usa un nombre diferente o elimina el archivo existente")