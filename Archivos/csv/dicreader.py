"""import csv

with open("/Users/statick/dev/apps/ejersicios-python/Archivos/csv/empleados.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        print(fila)"""

import csv

with open("/Users/statick/dev/apps/ejersicios-python/Archivos/csv/empleados.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    
    total_edad = 0
    contador = 0
    ciudades = set()
    
    for fila in lector:
        edad = int(fila["edad"])
        total_edad += edad
        contador += 1
        ciudades.add(fila["ciudad"])
    
    promedio = total_edad / contador
    print(f"Promedio de edad: {promedio:.1f} años")
    print(f"Ciudades: {', '.join(ciudades)}")