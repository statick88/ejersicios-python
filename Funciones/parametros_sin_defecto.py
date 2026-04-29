# ✅ Correcto: obligatorios primero, opcionales después
def registrar(nombre, email, newsletter=True):
    pass

# ❌ Error: parámetro sin defecto después de uno con defecto
#def registrar(newsletter=True, email):  # SyntaxError
#     pass