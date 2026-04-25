# ✅ Guard clauses — código plano y claro
def procesar_pedido(producto, cantidad, usuario):
    if not usuario:
        return "Usuario no autenticado"
    if not usuario.activo:
        return "Usuario inactivo"
    if not producto:
        return "Producto no existe"
    if producto.stock < cantidad:
        return "Sin stock suficiente"
    if usuario.saldo < producto.precio * cantidad:
        return "Saldo insuficiente"
    
    return "Pedido procesado"