def calcular_area_rectangulo(base=0, altura=0):
    """Calcula el área de un rectángulo."""
    area = base * altura
    return area

resultado = calcular_area_rectangulo(altura=3, base=5)
print(f"El área es: {resultado}")