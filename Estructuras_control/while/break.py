# Buscar un número en una lista
numeros = [4, 8, 15, 16, 23, 42]
buscado = 16

for numero in numeros:
    if numero == buscado:
        print(f"¡Encontrado! El {buscado} está en la lista")
        break
    print(f"Revisando {numero}... no es")
else:
    print(f"El {buscado} no está en la lista")