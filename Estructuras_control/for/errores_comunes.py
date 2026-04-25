# ❌ PELIGROSO: modificar la lista que estás recorriendo
numeros = [1, 2, 3, 4, 5]
"""for n in numeros:
    if n % 2 == 0:
        numeros.remove(n)  # ¡Puede saltar elementos!"""

# ✅ CORRECTO: crear una nueva lista
numeros = [1, 2, 3, 4, 5]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)