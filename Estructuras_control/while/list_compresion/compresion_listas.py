# Forma tradicional con bucle for
cuadrados = []
for i in range(1, 11):
    cuadrados.append(i ** 2)

print(cuadrados)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("==========================")
# Comprensión de listas — una línea, mismo resultado
cuadrados = [i ** 2 for i in range(1, 11) if i % 2 == 1]  # Solo cuadrados de números pares

print(cuadrados)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]