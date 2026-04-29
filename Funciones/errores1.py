# ❌ Error de sintaxis
"""def saludar()
    print("Hola")"""

# ✅ Correcto
"""def saludar():
    print("Hola")

saludar()"""

# ❌ El cuerpo debe estar indentado
"""def saludar():
print("Hola")  # IndentationError"""

# ✅ 4 espacios de indentación
"""def saludar():
    print("Hola")

saludar()"""

# ❌ La función no existe aún
"""despedir()  # NameError

def despedir():
    print("¡Hasta luego!")"""

# ✅ Primero define, luego llama
"""def despedir():
    print("¡Hasta luego!")

despedir()"""

# ❌ Esto solo define la función, NO la ejecuta
def saludar():
    print("Hola")

# ✅ Necesitas los paréntesis para ejecutarla
saludar()