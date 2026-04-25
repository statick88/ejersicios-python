# ❌ ERROR: un solo = es asignación, no comparación
"""edad = 18
if edad = 18:  # SyntaxError
    print("Mayor de edad")"""

# ✅ CORRECTO: == compara dos valores
edad = 18
if edad == 18:
    print("Mayor de edad")