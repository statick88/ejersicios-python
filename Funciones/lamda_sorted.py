estudiantes = [
    ("Ana", 85),
    ("Carlos", 92),
    ("María", 78),
    ("Diego", 92),
]

# Ordenar por nombre (primer elemento de la tupla)
#por_nombre = sorted(estudiantes, key=lambda est: est[0])
#print(por_nombre)
# [('Ana', 85), ('Carlos', 92), ('Diego', 92), ('María', 78)]

# Ordenar por nota (segundo elemento), de mayor a menor
por_nota = sorted(estudiantes, key=lambda est: est[1], reverse=False)
print(por_nota)
# [('Carlos', 92), ('Diego', 92), ('Ana', 85), ('María', 78)]