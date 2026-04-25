# ✅ Anidación con propósito: validar antes de operar
def calcular_descuento(edad, es_cliente_frecuente, total_compra):
    if total_compra > 100:
        # Solo aplicamos descuentos si la compra supera $100
        if edad >= 65:
            descuento = 0.20  # 20% para tercera edad
        elif es_cliente_frecuente:
            descuento = 0.15  # 15% para clientes frecuentes
        else:
            descuento = 0.10  # 10% descuento base
    else:
        descuento = 0.00
    
    return total_compra * (1 - descuento)
# Ejemplo de uso
total = calcular_descuento(40, True, 110)
print(f"Total a pagar: ${total:.2f}")