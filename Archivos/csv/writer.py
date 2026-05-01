import csv

# Datos a escribir
productos = [
    ["Producto", "Precio", "Stock"],
    ["Teclado", 25.99, 150],
    ["Mouse", 12.50, 89],
    ["Monitor", 199.99, 23],
]

with open("/Users/statick/dev/apps/ejersicios-python/Archivos/csv/productos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(productos)

print("Archivo 'productos.csv' creado exitosamente")