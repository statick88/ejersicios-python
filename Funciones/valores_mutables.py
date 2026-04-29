# ❌ PELIGRO: lista mutable como valor por defecto
def agregar_item(item, lista=[]):
    lista.append(item)
    return lista

resultado1 = agregar_item("manzana")
print(resultado1)  # ['manzana']

resultado2 = agregar_item("pera")
print(resultado2)  # ['manzana', 'pera'] — ¡¿Qué?!

# ✅ Solución: usa None como valor por defecto
def agregar_item_seguro(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

r1 = agregar_item_seguro("manzana")
print(r1)  # ['manzana']

r2 = agregar_item_seguro("pera")
print(r2)  # ['pera'] — Correcto