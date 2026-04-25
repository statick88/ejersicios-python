# ❌ Quería saltar este caso, pero salió del bucle entero
numeros = [1, 2, 3, 4, 5]
"""for n in numeros:
    if n == 3:
        break  # ¡Esto sale del bucle! Solo imprime 1, 2
    print(n)"""

# ✅ Quería saltar el 3 y continuar con el resto
for n in numeros:
    if n == 3:
        continue  # Salta el 3, pero sigue con 4 y 5
    print(n)  # Imprime: 1, 2, 4, 5