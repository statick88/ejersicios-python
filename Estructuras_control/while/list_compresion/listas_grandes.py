# ❌ Si el rango es muy grande, consume mucha memoria
#millones = [i ** 2 for i in range(10_000_000)]
#print(millones)
# ✅ Usa generador (paréntesis) para procesar uno a uno
for cuadrado in (i ** 2 for i in range(10_000_000)):
    print(cuadrado)