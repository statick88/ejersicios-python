# Comprensión de diccionario {clave: valor for ...}
numeros = [1, 2, 3, 4, 5]
cuadrados_dict = {n: n ** 2 for n in numeros}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Comprensión de conjunto {expresion for ...}
palabras = ["hola", "mundo", "python", "hola", "mundo"]
primeras_letras = {p[0] for p in palabras}
print(primeras_letras)
# {'h', 'm', 'p'}