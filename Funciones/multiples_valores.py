def dividir(dividendo, divisor):
    if divisor == 0:
        return None, None
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    return cociente, residuo

q, r = dividir(17, 5)
print(f"Cociente: {q}, Residuo: {r}")  # Cociente: 3, Residuo: 2