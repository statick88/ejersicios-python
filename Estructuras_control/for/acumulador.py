# Calcular el total de una lista de precios
precios = [12.50, 8.75, 15.00, 6.25, 20.00]

total = 0
for precio in precios:
    total = total + precio

print(f"Total a pagar: ${total:.2f}")