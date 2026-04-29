def convertir_temperatura(celsius):
    """Convierte grados Celsius a Fahrenheit.

    Args:
        celsius: Temperatura en grados Celsius.

    Returns:
        La temperatura equivalente en grados Fahrenheit.
    """
    return celsius * 9/5 + 32

# Puedes ver el docstring así:
print(convertir_temperatura.__doc__)