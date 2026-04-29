"""def sumar_todo(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(sumar_todo(1, 2, 3))
print(sumar_todo(10, 20, 30, 40))
print(sumar_todo(5))"""

# Ejemplo práctico: calcular promedio de notas variables
def calcular_promedio(*notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

print(calcular_promedio(8, 9, 7))
print(calcular_promedio(10, 8, 9, 7, 6))