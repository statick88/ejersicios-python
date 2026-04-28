# Bucle tradicional
nombres = ["ana", "BENITO", "carlos", "DIANA"]
nombres_capitalizados = []
"""for nombre in nombres:
    nombres_capitalizados.append(nombre.capitalize())"""

# Comprensión de listas
nombres_capitalizados = [nombre.capitalize() for nombre in nombres]
print(nombres_capitalizados)

# ['Ana', 'Benito', 'Carlos', 'Diana']