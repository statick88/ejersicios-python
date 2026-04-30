# ❌ Lambda con nombre para algo complejo
#procesar_datos = lambda datos: [x * 2 for x in datos if x > 0]
#print(procesar_datos([-3, 0, 2, 5, -1]))  # [4, 10]
# ✅ Si le pusiste nombre y es compleja, usa def
def procesar_datos(datos):
    """Duplica solo los valores positivos."""
    return [x * 2 for x in datos if x > 0]

print(procesar_datos([-3, 0, 2, 5, -1]))  # [4, 10]