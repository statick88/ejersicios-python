# ✅ Seguro: el archivo se cierra AUTOMÁTICAMENTE, incluso si hay errores
"""with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)"""

# Lo que Python hace por ti con 'with':
archivo = open("/Users/statick/dev/apps/ejersicios-python/Archivos/datos.txt", "r")  # __enter__()
try:
    contenido = archivo.read()
finally:
    archivo.close()  # __exit__() — siempre se ejecuta