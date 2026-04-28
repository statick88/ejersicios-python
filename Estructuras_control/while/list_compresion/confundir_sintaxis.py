# ❌ Paréntesis en vez de corchetes — esto crea un generador, no una lista
cuadrados = (i ** 2 for i in range(5))  # Esto es un generador
print(cuadrados)
# ✅ Corchetes para listas
cuadrados = [i ** 2 for i in range(5)]  # Esto es una lista
print(cuadrados)
