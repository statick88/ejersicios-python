# Bucle tradicional
temperaturas = [22, 35, 18, 40, 28, 15, 38]
alertas = []
"""for temp in temperaturas:
    if temp > 30:
        alertas.append(f"ALERTA: {temp}°C")"""
# Comprensión con transformación y filtro
alertas = [f"ALERTA: {temp}°C" for temp in temperaturas if temp > 30]
print(alertas)

# ['ALERTA: 35°C', 'ALERTA: 40°C', 'ALERTA: 38°C']
