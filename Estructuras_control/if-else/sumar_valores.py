# Contar cuántos números son pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares = pares + 1

print(f"Hay {pares} números pares")