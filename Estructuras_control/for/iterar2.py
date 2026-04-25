precios = {"manzana": 1.50, "banana": 0.75, "cereza": 2.00}

# Solo claves (por defecto)
for fruta in precios:
    print(fruta)

# Solo valores
for precio in precios.values():
    print(precio)

# Clave y valor al mismo tiempo
for fruta, precio in precios.items():
    print(f"{fruta} cuesta ${precio}")