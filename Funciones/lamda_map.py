precios = [10, 20, 30, 40, 50]

# Aplicar 15% de IVA a cada precio
con_iva = list(map(lambda p: p * 1.15, precios))
print(con_iva)  # [11.5, 23.0, 34.5, 46.0, 57.5]

# Convertir a texto con formato
formateados = list(map(lambda p: f"${p:.2f}", con_iva))
print(formateados)  # ['$11.50', '$23.00', '$34.50', '$46.00', '$57.50']