# Sin funciones: repites el mismo código una y otra vez
"""print("=== BIENVENIDO ===")
print("Usuario: Ana")
print("=== BIENVENIDO ===")
print("Usuario: Carlos")
print("=== BIENVENIDO ===")
print("Usuario: María")"""

# Con funciones: escribes una vez, usas muchas veces
def mostrar_bienvenida(nombre):
    print("=== BIENVENIDO ===")
    print(f"Usuario: {nombre}")

mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")
mostrar_bienvenida("María")
mostrar_bienvenida("Luis")
mostrar_bienvenida("Nelson")