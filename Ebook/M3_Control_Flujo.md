# Módulo 3: Control de Flujo

---

## Objetivo

Aprender a controlar el flujo de ejecución del programa.

---

## 3.1 Condicionales: if / elif / else

```python
edad = 18

# ifsimple
if edad >= 18:
    print("Mayor de edad")

# if...else
if edad >= 18:
    print("Mayor")
else:
    print("Menor")

# if...elif...else
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
else:
    print("Reprobado")
```

---

## 3.2 Bucle: for

```python
# Iterar sobre lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Iterar con range
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# enumerate (índice + valor)
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
```

---

## 3.3 Bucle: while

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

## 3.4 Control de Bucles

```python
# break: salir del bucle
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")  # 0 1 2 3 4

# continue: siguiente iteración
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")  # 1 2 4 5
```

---

## 3.5 List Comprehension

```python
# Crear lista de cuadrados
cuadrados = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# Filtrar con condición
pares = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

---

## Ejercicios

### Ejercicio 3.1: Calculadora de edad
```python
edad = int(input("Tu edad: "))
if edad < 0:
    print("Edad inválida")
elif edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")
```

### Ejercicio 3.2: Tabla de multiplicar
```python
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

---

## Resumen

| Estructura | Uso |
|------------|-----|
| if/elif/else | Decisiones |
| for | Iterar sobre secuencia |
| while | Iterar mientras condición |
| break | Salir del bucle |
| continue | Siguiente iteración |

---

## Checklist

- [ ] Uso if/elif/else para decisiones
- [ ] Creo bucles con for
- [ ] Creo bucles con while
- [ ] Uso break/continue
- [ ] Comprendo list comprehension

---

*Control de Flujo - Fundamentos de Python*