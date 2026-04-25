# range(n) genera números de 0 a n-1
for i in range(5):
    print(i)  # Imprime: 0, 1, 2, 3, 4

# range(inicio, fin) genera números desde inicio hasta fin-1
for i in range(3, 8):
    print(i)  # Imprime: 3, 4, 5, 6, 7

# range(inicio, fin, paso) con incremento personalizado
for i in range(0, 20, 5):
    print(i)  # Imprime: 0, 5, 10, 15

# Cuenta regresiva
for i in range(10, 0, -1):
    print(i)
print("¡Despegue!")