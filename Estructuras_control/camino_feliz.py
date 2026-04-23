edad = 20

# ❌ Camino triste primero (confuso)
"""def verificar_acceso(edad):
    if edad >= 18:
        if edad < 65:
            if edad >= 21:
                return "Acceso completo"
            else:
                return("Acceso limitado")
        else:
            return "Descuento tercera edad"
    else:
        return "Acceso denegado"""

# ✅ Camino feliz claro (legible)
def verificar_acceso(edad):
    if edad < 18:
        return "Acceso denegado"
    if edad < 21:
        return "Acceso limitado"
    if edad >= 65:
        return "Descuento tercera edad"
    return "Acceso completo"

verificar_acceso(edad)