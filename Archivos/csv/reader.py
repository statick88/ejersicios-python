"""import csv

# Archivo: empleados.csv
# nombre,edad,ciudad
# Ana,28,Quito
# Carlos,35,Guayaquil
# María,22,Cuenca

with open("/Users/statick/dev/apps/ejersicios-python/Archivos/csv/empleados.csv", "r") as archivo:
    lector = csv.reader(archivo)
    
    for fila in lector:
        print(fila)"""

import csv

with open("/Users/statick/dev/apps/ejersicios-python/Archivos/csv/empleados.csv", "r") as archivo:
    lector = csv.reader(archivo)
    
    encabezado = next(lector)
    print(f"Columnas: {encabezado}")
    
    for fila in lector:
        nombre = fila[0]
        edad = int(fila[1])
        ciudad = fila[2]
        print(f"{nombre} tiene {edad} años y vive en {ciudad}")