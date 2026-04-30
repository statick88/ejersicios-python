numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar solo los pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Filtrar notas aprobatorias (>= 7)
notas = [8, 5, 9, 3, 7, 6, 10, 4]
aprobados = list(filter(lambda nota: nota >= 7, notas))
print(aprobados)  # [8, 9, 7, 10]