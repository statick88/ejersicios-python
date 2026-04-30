# Patrón recomendado para leer archivos
try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido cargado exitosamente")
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe")
#except PermissionError:
    #print("Error: No tienes permiso para leer este archivo")
except Exception as e:
    print(f"Error inesperado: {e}")