# Sin parámetros
saludar = lambda: "¡Hola!"
print(saludar())  # ¡Hola!

# Un parámetro
cuadrado = lambda x: x ** 2
print(cuadrado(7))  # 49

# Dos parámetros
suma = lambda a, b: a + b
print(suma(3, 4))  # 7

# Tres parámetros con lógica
promedio = lambda a, b, c: (a + b + c) / 3
print(promedio(8, 9, 7))  # 8.0