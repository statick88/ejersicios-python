def crear_perfil(nombre, edad, profesion):
    print(f"{nombre} | {edad} años | {profesion}")

# ✅ Con nombre: el orden no importa
crear_perfil(edad=30, nombre="Carlos", profesion="Ingeniero")

# ✅ Mezclar posicionales y con nombre
crear_perfil("María", profesion="Diseñadora", edad=25)

# ❌ Posicional después de keyword — SyntaxError
# crear_perfil(nombre="Ana", 28)