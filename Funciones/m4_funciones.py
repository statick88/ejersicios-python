#!/usr/bin/env python3
"""
Módulo 4: Funciones
==================

 Una función es un bloque de código reutilizable.
 Se define con def y se llama por su nombre.

 Este módulo cubré:
 - Definir funciones
 - Parámetros y return
 - *args y **kwargs
 - Funciones lambda
 - Docstrings

 Ebook: Ver M4_Funciones.md para teoría completa
"""

# ==========================================
# 1. DEFINIR UNA FUNCIÓN
# ==========================================

# def nombre(parámetros):
#     código
#     return valor

def saludar():
    """Saluda al usuario"""
    print("¡Hola! Bienvenido")

# Llamar la función
saludar()


# ==========================================
# 2. PARÁMETROS Y RETURN
# ==========================================

def saludar_persona(nombre):
    """Saluda a una persona específica"""
    return f"¡Hola, {nombre}!"

# Llamar con argumento
mensaje = saludar_persona("Carlos")
print(mensaje)


# ==========================================
# 3. PARÁMETROS CON VALOR POR DEFECTO
# ==========================================

def saludar_persona(nombre, idioma="es"):
    """Saluda según el idioma"""
    if idioma == "es":
        return f"¡Hola, {nombre}!"
    elif idioma == "en":
        return f"Hello, {nombre}!"
    elif idioma == "fr":
        return f"Bonjour, {nombre}!"
    else:
        return f"¡Hola, {nombre}!"

print(saludar_persona("Ana"))           # usa default
print(saludar_persona("Ana", "en"))  # override


# ==========================================
# 4. *ARGS: ARGUMENTOS VARIABLES
# ==========================================

def sumar_todos(*numeros):
    """Suma cualquier cantidad de números"""
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todos(1, 2))           # 3
print(sumar_todos(1, 2, 3, 4, 5))  # 15


# ==========================================
# 5. **KWARGS: PARTE CLAVE-VALOR
# ==========================================

def mostrar_info(**datos):
    """Muestra información clave-valor"""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=30, ciudad="Quito")


# ==========================================
# 6. RETURN MÚLTIPLES VALORES
# ==========================================

def operaciones(a, b):
    """Retorna múltiples valores como tupla"""
    suma = a + b
    resta = a - b
    producto = a * b
    return suma, resta, producto

resultado = operaciones(5, 3)
print(resultado)  # (8, 2, 15)

# También puedes separar
s, r, p = operaciones(5, 3)
print(f"Suma: {s}, Resta: {r}, Producto: {p}")


# ==========================================
# 7. FUNCIONES LAMBDA (ANÓNIMAS)
# ==========================================

# lambda parámetros: expresión
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25

# Con múltiples parámetros
sumar = lambda a, b: a + b
print(sumar(3, 7))  # 10


# ==========================================
# 8. LAMBDA CON map(), filter(), sorted()
# ==========================================

numeros = [1, 2, 3, 4, 5]

# map: aplicar función a cada elemento
dobles = list(map(lambda x: x * 2, numeros))
print(f"Dobles: {dobles}")  # [2, 4, 6, 8, 10]

# filter: mantener solo los que cumplen condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares: {pares}")  # [2, 4]

# sorted: ordenar con función clave
nombres = ["Carlos", "Ana", "Bob", "Diana"]
ordenados = sorted(nombres, key=lambda x: len(x))
print(f"Por longitud: {ordenados}")


# ==========================================
# 9. DOCSTRINGS (DOCUMENTACIÓN)
# ==========================================

def calcular_area(base, altura, forma="rectangulo"):
    """
    Calcula el área de una figura geométrica.

    Argumentos:
        base: La base de la figura
        altura: La altura de la forma
        forma: Tipo de forma (rectangulo o triangulo)

    Retorna:
        float: El área calculada

    Ejemplo:
        >>> calcular_area(5, 4)
        20
    """
    if forma == "rectangulo":
        return base * altura
    elif forma == "triangulo":
        return (base * altura) / 2
    else:
        return 0

# Ver docstring
print(calcular_area.__doc__)
print(calcular_area(5, 4))


# ==========================================
# RESUMEN DEL MÓDULO 4
# ==========================================
"""
Funciones aprendidas:
✓ def nombre()         - definir función
✓ return             - retornar valor
✓ parámetros         - valores de entrada
✓ *args              - argumentos variáveis
✓ **kwargs           - argumentos clave-valor
✓ lambda             - función anónima
✓ map/filter/sorted  - funciones integradas
✓ docstring          - documentación

Siguiente unidad: M5 - POO
Ebook: M5_POO.md
"""

# Fin del Módulo 4