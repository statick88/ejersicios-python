  # Iterar sobre una cadena de texto
lenguaje = "Python"
for letra in lenguaje:
    print(letra, end="-")
# Resultado: P-y-t-h-o-n-
print("------------")
# Iterar sobre una tupla
coordenadas = (10, 20, 30)
for valor in coordenadas:
    print(f"Coordenada: {valor}")

# Iterar sobre un diccionario
precios = {"manzana": 1.50, "banana": 0.75, "cereza": 2.00}
for fruta in precios:
    print(f"{fruta}: ${precios[fruta]}")