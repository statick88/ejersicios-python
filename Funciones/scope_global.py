# Variables globales
impuesto_base = 0.15
moneda = "USD"

def calcular_precio_final(precio):
    # Puede LEER variables globales
    total = precio * (1 + impuesto_base)
    return f"{total:.2f} {moneda}"

print(calcular_precio_final(100))  # 115.00 USD
print(f"Impuesto configurado: {impuesto_base}")  # 0.15