# ❌ Sin funciones: mismo código repetido 3 veces
"""print("--- Factura #1 ---")
print("Subtotal: $100.00")
print("IVA (15%): $15.00")
print("Total: $115.00")

print("--- Factura #2 ---")
print("Subtotal: $200.00")
print("IVA (15%): $30.00")
print("Total: $230.00")

print("--- Factura #3 ---")
print("Subtotal: $50.00")
print("IVA (15%): $7.50")
print("Total: $57.50")"""

# ✅ Con funciones: una sola definición, múltiples usos
def mostrar_factura(numero, subtotal):
    iva = subtotal * 0.15
    total = subtotal + iva
    print(f"--- Factura #{numero} ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA (15%): ${iva:.2f}")
    print(f"Total: ${total:.2f}")

mostrar_factura(1, 100)
mostrar_factura(2, 200)
mostrar_factura(3, 50)