productos = [
    {"nombre": "Laptop", "precio": 999, "stock": 5},
    {"nombre": "Mouse", "precio": 25, "stock": 150},
    {"nombre": "Teclado", "precio": 75, "stock": 80},
    {"nombre": "Monitor", "precio": 350, "stock": 20},
]

# Ordenar por precio (más barato primero)
mas_baratos = sorted(productos, key=lambda p: p["precio"])
for prod in mas_baratos:
    print(f"{prod['nombre']}: ${prod['precio']}")

# Filtrar productos con poco stock
poco_stock = list(filter(lambda p: p["stock"] < 30, productos))
print(f"Productos con poco stock: {len(poco_stock)}")