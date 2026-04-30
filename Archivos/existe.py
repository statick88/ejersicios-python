import os

ruta = "datos.txt"

if os.path.exists(ruta):
    with open(ruta, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
else:
    print(f"El archivo '{ruta}' no existe")