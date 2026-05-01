import csv

# Lista de diccionarios — cada diccionario es una fila
contactos = [
    {"nombre": "Ana", "email": "ana@ejemplo.com", "telefono": "0991234567"},
    {"nombre": "Carlos", "email": "carlos@ejemplo.com", "telefono": "0987654321"},
    {"nombre": "María", "email": "maria@ejemplo.com", "telefono": "0976543210"},
]

campos = ["nombre", "email", "telefono"]

with open("/Users/statick/dev/apps/ejersicios-python/Archivos/csv/contactos.csv", "w", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(contactos)