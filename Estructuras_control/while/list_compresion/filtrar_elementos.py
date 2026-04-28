# Bucle tradicional
precios = [12.50, 8.75, 15.00, 3.25, 20.00, 5.50]
caros = []
"""for precio in precios:
    if precio >= 10:
        caros.append(precio)"""

# Comprensión con filtro
caros = [precio for precio in precios if precio >= 10]
# [12.5, 15.0, 20.0]
print(caros)
