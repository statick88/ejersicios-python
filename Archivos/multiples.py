# Leer de un archivo y escribir en otro
with open("origen.txt", "r") as origen, open("copia.txt", "w") as destino:
    contenido = origen.read()
    destino.write(contenido)
    print("Archivo copiado exitosamente")