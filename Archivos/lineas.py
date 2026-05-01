# Generar un archivo con números del 1 al 10
with open("numeros.txt", "w") as archivo:
    lineas = [f"Número {i}\n" for i in range(1, 11)]
    archivo.writelines(lineas)