# Módulo 1: Variables y Tipos de Datos

---

## Objetivo

Comprender los tipos de datos fundamentales en Python y cómo trabajar con ellos.

---

## 1.1 ¿Qué son las Variables?

Una **variable** es un contenedor para guardar datos. Piensa en ella como una caja etiquetada donde guardas un valor.

```python
# Crear variable
nombre = "Carlos"
```

- `nombre` = nombre de la variable (la etiqueta)
- `=` = operador de asignación
- `"Carlos"` = valor guardado

---

## 1.2 Tipos de Datos Fundamentales

### String (str) - Texto

```python
nombre = "Carlos"
apellido = 'García'
multilinea = """Este es un
texto de múltiples
líneas"""
```

### Integer (int) - Números Enteros

```python
edad = 30
año = 2026
temperatura = -10
```

### Float (float) - Números Decimales

```python
altura = 1.75
precio = 19.99
pi = 3.14159
```

### Boolean (bool) - Verdadero/Falso

```python
es_estudiante = True
tiene_credito = False
```

---

## 1.3 type() - Verificar el Tipo

```python
nombre = "Carlos"
print(type(nombre))  # <class 'str'>

edad = 30
print(type(edad))    # <class 'int'>
```

---

## 1.4 Casting (Conversión entre Tipos)

```python
# String → Integer
edad = int("25")     # 25

# Integer → String  
numero = str(42)     # "42"

# String → Float
precio = float("19.99")  # 19.99

# Integer → Float
decimal = float(10)   # 10.0
```

---

## 1.5 f-strings (Formato Moderno)

```python
nombre = "Carlos"
edad = 30

# Forma moderna
print(f"Me llamo {nombre} y tengo {edad} años")
# Resultado: Me llamo Carlos y tengo 30 años
```

---

## Ejercicios

### Ejercicio 1.1: Variables básicas
```python
# Crea variables para tu información personal
nombre = "Tu nombre"
edad = Tu edad
altura = Tu altura
es_estudiante = True/False

# Imprime cada variable con su tipo
print(f"{nombre} - {type(nombre)}")
```

### Ejercicio 1.2: Conversión
```python
# Convierte tipos
texto = "42"
numero = int(texto)
print(f"{texto} → {numero} (tipo: {type(numero)})")
```

---

## Resumen

| Tipo | Ejemplo | Función |
|------|--------|---------|
| str | "hola" | Texto |
| int | 42 | Entero |
| float | 3.14 | Decimal |
| bool | True/False | Booleano |

---

## Checklist

- [ ] Comprendo qué son variables
- [ ] Conozco los 4 tipos fundamentales
- [ ] Puedo usar type() para verificar
- [ ] Sé convertir entre tipos
- [ ] Uso f-strings para formatear

---

*Variables y Tipos - Fundamentos de Python*