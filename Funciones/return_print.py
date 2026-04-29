# ❌ print() solo muestra en pantalla — no puedes usar el resultado
"""def mostrar_doble(numero):
    print(numero * 2)

resultado = mostrar_doble(5)  # Muestra: 10
print(resultado) """             # Muestra: None — ¡no hay valor!

# ✅ return devuelve un valor — puedes usarlo después
"""def calcular_doble(numero):
    return numero * 2

resultado = calcular_doble(5)  # No muestra nada
print(resultado)  """         # Muestra: 10 — ¡ahora sí tienes el valor!

# print() — el barista grita
"""def gritar_pedido():
    print("¡Café latte para Ana!")

gritar_pedido() """ # Lo escuchas, pero no tienes café

# return() — el barista te entrega
"""def entregar_pedido():
    return "Café latte para Ana"

mi_cafe = entregar_pedido()  # Ahora tienes el café en tu variable
print(mi_cafe) """           # "Café latte para Ana"

"""def calcular_iva(precio):
    return precio * 0.15

iva = calcular_iva(100)
print(f"El IVA es: ${iva}")  # $15.0"""

def verificar_acceso(edad):
    if edad < 0:
        return "Error: edad inválida"
    if edad < 18:
        return "Acceso denegado: menor de edad"
    if edad >= 65:
        return "Acceso preferencial: adulto mayor"
    return "Acceso permitido"

print(verificar_acceso(-5))   # Error: edad inválida
print(verificar_acceso(15))   # Acceso denegado: menor de edad
print(verificar_acceso(70))   # Acceso preferencial: adulto mayor
print(verificar_acceso(30))   # Acceso permitido