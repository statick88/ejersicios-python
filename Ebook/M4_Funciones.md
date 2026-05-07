# Módulo 4: Funciones

---

## Objetivo

Aprender a crear y usar funciones para reutilizar código.

---

## 4.1 Definir una Función

```python
def saludar():
    """Esta función saludar"""
    print("¡Hola!")

# Llamar
saludar()
```

---

## 4.2 Parámetros y Return

```python
def saludar_persona(nombre):
    """Saluda a una persona"""
    return f"¡Hola, {nombre}!"

mensaje = saludar_persona("Carlos")
print(mensaje)  # ¡Hola, Carlos!
```

---

## 4.3 Parámetros con Valor por Defecto

```python
def saludar(nombre, idioma="es"):
    if idioma == "es":
        return f"¡Hola, {nombre}!"
    elif idioma == "en":
        return f"Hello, {nombre}!"
    return f"¡Hola, {nombre}!"

print(saludar("Ana"))        # usa default
print(saludar("Ana", "en"))  # override
```

---

## 4.4 *args y **kwargs

```python
# *args: argumentos variables
def suma(*numeros):
    return sum(numeros)

print(suma(1, 2, 3, 4))  # 10

# **kwargs: argumentos clave-valor
def mostrar(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar(nombre="Carlos", edad=30)
```

---

## 4.5 Funciones Lambda

```python
# lambda parámetro: expresión
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25

# Con map, filter, sorted
numeros = [1, 2, 3, 4, 5]

dobles = list(map(lambda x: x * 2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
```

---

## 4.6 Docstrings

```python
def calcular_area(base, altura, forma="rectangulo"):
    """
    Calcula el área de una figura.
    
    Argumentos:
        base: La base de la figura
        altura: La altura de la forma
        forma: rectangulo o triangulo
    
    Retorna:
        float: El área calculada
    """
    if forma == "rectangulo":
        return base * altura
    elif forma == "triangulo":
        return (base * altura) / 2
    return 0
```

---

## Ejercicios

### Ejercicio 4.1: Calculadora
```python
def calculadora(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b if b != 0 else "Error"
    return "Error"

print(calculadora(10, 5, "+"))  # 15
```

---

## Resumen

| Concepto | Sintaxis |
|----------|-----------|
| Definir | `def nombre():` |
| Return | `return valor` |
| Args | `*args` |
| Kwargs | `**kwargs` |
| Lambda | `lambda x: x + 1` |

---

## Checklist

- [ ] Defino funciones con def
- [ ] Uso parámetros
- [ ] Uso return
- [ ] Comprendo *args y **kwargs
- [ ] Escribo funciones lambda

---

*Funciones - Fundamentos de Python*