# ❌ SyntaxError: break solo funciona dentro de for o while
"""if True:
    break  # Error: no está dentro de un bucle"""

# ✅ Correcto
while True:
    if True:
        print("Dentro del bucle")
        break  # OK: está dentro del while