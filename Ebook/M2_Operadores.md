# Módulo 2: Operadores y Expresiones

---

## Objetivo

Aprender a realizar operaciones y comparaciones en Python.

---

## 2.1 Operadores Aritméticos

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|----------|
| + | Suma | 10 + 5 | 15 |
| - | Resta | 10 - 5 | 5 |
| * | Multiplicación | 10 * 5 | 50 |
| / | División | 10 / 5 | 2.0 |
| // | División entera | 10 // 5 | 2 |
| % | Módulo (resto) | 10 % 3 | 1 |
| ** | Exponente | 2 ** 3 | 8 |

```python
a = 10
b = 3

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo: {a % b}")
print(f"Exponente: {a ** b}")
```

---

## 2.2 Operadores de Comparación

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|----------|
| == | Igual a | 5 == 5 | True |
| != | Diferente de | 5 != 3 | True |
| < | Menor que | 3 < 5 | True |
| > | Mayor que | 5 > 3 | True |
| <= | Menor o igual | 3 <= 5 | True |
| >= | Mayor o igual | 5 >= 5 | True |

```python
x = 5
y = 10

print(f"x == y: {x == y}")  # False
print(f"x != y: {x != y}")  # True
print(f"x < y: {x < y}")    # True
```

---

## 2.3 Operadores Lógicos

| Operador | Descripción | Ejemplo | Resultado |
|----------|--------------|---------|----------|
| and | Ambos deben ser True | True and False | False |
| or | Al menos uno debe ser True | True or False | True |
| not | Invierte el valor | not True | False |

```python
sol = True
lluvia = False

print(f"sol and lluvia: {sol and lluvia}")  # False
print(f"sol or lluvia: {sol or lluvia}")    # True
print(f"not sol: {not sol}")               # False
```

---

## 2.4 Operador Ternario

```python
edad = 18

# Forma larga:
if edad >= 18:
    resultado = "Mayor"
else:
    resultado = "Menor"

# Forma ternaria (una línea):
resultado = "Mayor" if edad >= 18 else "Menor"
```

---

## 2.5 Precedencia de Operadores

Orden de evaluación (igual que matemáticas):

1. `()` - Paréntesis
2. `**` - Exponente
3. `* / // %` - Multiplicación/división
4. `+ -` - Suma/resta
5. `== != < > <= >=` - Comparación
6. `not` - Negación
7. `and` - Y lógico
8. `or` - O lógico

```python
# 2 + 3 * 4 = 14 (primero multiplica)
# (2 + 3) * 4 = 20 (paréntesis primero)
```

---

## Ejercicios

### Ejercicio 2.1: Calculadora
```python
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b

print(sumar(10, 5))      # 15
print(restar(10, 5))     # 5
print(multiplicar(10, 5)) # 50
print(dividir(10, 5))    # 2.0
```

### Ejercicio 2.2: Comparaciones
```python
edad = 20
print(f"¿Es mayor de edad? {edad >= 18}")
print(f"¿Es adulto mayor? {edad >= 65}")
```

---

## Resumen

| Categoría | Operadores |
|----------|------------|
| Aritméticos | + - * / // % ** |
| Comparación | == != < > <= >= |
| Lógicos | and or not |
| Ternario | valor1 if cond else valor2 |

---

## Checklist

- [ ] Uso operadores aritméticos
- [ ] Comparo valores
- [ ] Combino condiciones con and/or/not
- [ ] Uso el operador ternario
- [ ] Conozco la precedencia

---

*Operadores - Fundamentos de Python*