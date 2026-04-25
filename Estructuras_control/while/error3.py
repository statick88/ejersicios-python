# ❌ Bucle infinito: 'i' nunca llega a 5 si es impar
"""i = 0
while i < 10:
    if i % 2 != 0:
        continue  # ¡Salta sin incrementar i!
    print(i)
    i = i + 1"""

# ✅ Actualizar ANTES del continue
i = 0
while i < 10:
    if i % 2 != 0:
        i = i + 1
        continue
    print(i)
    i = i + 1