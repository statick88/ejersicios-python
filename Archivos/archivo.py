# Abrir un archivo en modo lectura
archivo = open("datos.txt", "r")

# Leer todo el contenido
contenido = archivo.read()
print(contenido)

# IMPORTANTE: siempre cerrar el archivo
archivo.close()