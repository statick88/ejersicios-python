# Otro ejemplo: estadísticas básicas
def estadisticas(numeros):
    if not numeros:
        return 0, 0, 0
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, promedio = estadisticas([4, 8, 15, 16, 23, 42])
print(f"Mín: {minimo}, Máx: {maximo}, Prom: {promedio:.1f}")