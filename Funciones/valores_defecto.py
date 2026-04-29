def crear_cuenta(usuario, rol="estudiante", activo=True):
    print(f"Usuario: {usuario}")
    print(f"Rol: {rol}")
    print(f"Activo: {activo}")

crear_cuenta("ana_garcia")
crear_cuenta("carlos_dev", rol="profesor")
crear_cuenta("maria_123", "admin", False)