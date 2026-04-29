def crear_perfil_completo(nombre, **kwargs):
    print(f"Nombre: {nombre}")
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")

crear_perfil_completo(
    "Ana",
    edad=28,
    ciudad="Quito",
    profesion="Desarrolladora",
    idioma="Español"
)
crear_perfil_completo(
    "Carlos",
    edad=30,
    ciudad="Madrid",
    profesion="Ingeniero",
    idioma="Español",
    hobbies=["fútbol", "cocina"],
    pais="España"
)