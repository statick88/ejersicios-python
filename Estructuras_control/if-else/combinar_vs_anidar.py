# ❌ Anidación innecesaria
temperatura = 30
humedad = 80

if temperatura > 25:
    if humedad > 70:
        print("Clima caluroso y húmedo")

# ✅ Combinación con 'and' — más directo
if temperatura > 25 and humedad > 70:
    print("Clima caluroso y húmedo")