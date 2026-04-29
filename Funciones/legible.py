# ❌ Código sin funciones: ¿qué hace esto?
"""p = 3.14159 * 5 ** 2
c = 2 * 3.14159 * 5
print(f"Área: {p}, Circunferencia: {c}")"""

# ✅ Código con funciones: se lee como una oración
def calcular_area_circulo(radio):
    return 3.14159 * radio ** 2

def calcular_circunferencia(radio):
    return 2 * 3.14159 * radio

area = calcular_area_circulo(5)
circunferencia = calcular_circunferencia(5)
print(f"Área: {area}, Circunferencia: {circunferencia}")