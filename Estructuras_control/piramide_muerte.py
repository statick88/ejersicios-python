# ❌ Pirámide de la muerte — NO hagas esto
def procesar_pedido(producto, cantidad, usuario):
    if usuario:
        if usuario.activo:
            if producto:
                if producto.stock >= cantidad:
                    if usuario.saldo >= producto.precio * cantidad:
                        print("Pedido procesado")
                    else:
                        print("Saldo insuficiente")
                else:
                    print("Sin stock")
            else:
                print("Producto no existe")
        else:
            print("Usuario inactivo")
    else:
        print("Usuario no autenticado")

procesar_pedido("Camiseta", 2, "juan")