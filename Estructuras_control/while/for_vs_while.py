# ✅ for: sabes exactamente cuántas veces (5)
for i in range(5):
    print(f"Iteración {i}")

# ✅ while: NO sabes cuántas veces (depende del usuario)
respuesta = ""
while respuesta != "si":
    respuesta = input("¿Quieres continuar? (si/no): ")
    if respuesta != "no":
        break