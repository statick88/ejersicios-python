
def calcular_descuento(precio):
    tasa = 0.15
    descuento = precio * tasa
    return precio - descuento

resultado = calcular_descuento(100)
print(resultado)  # 85.0
#print(tasa)  # ❌ NameError: 'tasa' no existe aquí fuera
#print(descuento)  # ❌ NameError: 'descuento' no existe aquí fuera