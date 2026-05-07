# Laboratorio 1: Tu Primer Programa

---

## Objetivo

Ejecutar tu primer programa en Python y comprender el flujo de ejecución.

## Duración
15 minutos

## Requisitos
- Python 3.12+ instalado
- Editor de código (VS Code recomendado)

## Ejercicios

### Ejercicio 1.1: Hola Mundo
```python
# Archivo: hola.py
print("¡Hola, Mundo!")
print("Bienvenido a Desarrollo Python 2026")
print("Mi primer programa en ")
```

### Ejercicio 1.2: Saludo Personalizado
```python
# Archivo: saludo.py
nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}! Bienvenido a ")
```

### Ejercicio 1.3: Calculadora Simple
```python
# Archivo: calculadora.py
print("=== Calculadora Simple ===")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Producto: {num1 * num2}")
print(f"División: {num1 / num2}")
```

## Entregables
- [ ] Archivo `hola.py` ejecutado
- [ ] Archivo `saludo.py` ejecutado
- [ ] Archivo `calculadora.py` ejecutado

---

## Laboratorio 2: Variables en Acción

---

## Objetivo

Comprender los diferentes tipos de variables y cómo usarlas.

## Duración
20 minutos

## Ejercicios

### Ejercicio 2.1: Variables Básicas
```python
# Tipos de variables
edad = 25           # int
altura = 1.75       # float
nombre = "Juan"     # str
es_estudiante = True  # bool

print(type(edad))
print(type(altura))
print(type(nombre))
print(type(es_estudiante))
```

### Ejercicio 2.2: Conversión de Tipos
```python
# Casting
numero_texto = "42"
numero = int(numero_texto)
print(numero + 8)  # 50

precio = "9.99"
precio_float = float(precio)
print(precio_float * 2)  # 19.98
```

### Ejercicio 2.3: Variables con Input
```python
nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
altura = float(input("Tu altura (m): "))

print(f"{nombre} tiene {edad} años y mide {altura}m")
```

## Entregables
- [ ] Programa que muestra tipos de variables
- [ ] Programa con casting funcionando
- [ ] Formulario con input/output

---

## Laboratorio 3: Estructuras de Control

---

## Objetivo

Dominar condicionales y bucles.

## Duración
25 minutos

### Ejercicio 3.1: if/else
```python
edad = int(input("Edad: "))

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

### Ejercicio 3.2: if/elif/else (Comparador)
```python
nota = float(input("Nota (0-10): "))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

### Ejercicio 3.3: for (Tabla de Multiplicar)
```python
num = int(input("Número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Ejercicio 3.4: while (Adivina el Número)
```python
import random
secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Adivina (1-10): "))
    intentos += 1
    
    if intento == secreto:
        print(f"¡Acertaste en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Mayor...")
    else:
        print("Menor...")
```

## Entregables
- [ ] Condicional con if/else
- [ ] Sistema de notas con elif
- [ ] Tabla de multiplicar
- [ ] Juego adivina el número

---

## Laboratorio 4: Funciones

---

## Objetivo

Crear funciones reutilizables.

## Duración
25 minutos

### Ejercicio 4.1: Función Básica
```python
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Juan")
saludar("María")
```

### Ejercicio 4.2: Función con Retorno
```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"5 + 3 = {resultado}")
```

### Ejercicio 4.3: Función con Args
```python
def promedio(*notas):
    return sum(notas) / len(notas)

print(promedio(7, 8, 9))
print(promedio(6, 7, 8, 9, 10))
```

### Ejercicio 4.4: Lambda
```python
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25

par = lambda x: "Par" if x % 2 == 0 else "Impar"
print(par(7))  # Impar
```

## Entregables
- [ ] Función saludar
- [ ] Función con return
- [ ] Función con *args
- [ ] Lambda para cuadrado/par

---

## Laboratorio 5: Listas y Tuplas

---

## Objetivo

Manipular colecciones ordenadas.

## Duración
20 minutos

### Ejercicio 5.1: Crear y Acceder
```python
frutas = ["manzana", "banana", "uva", "naranja"]
print(frutas[0])  # manzana
print(frutas[-1]) # naranja

# Slicing
print(frutas[1:3])  # ['banana', 'uva']
```

### Ejercicio 5.2: Métodos de Lista
```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
numeros.append(0)
numeros.sort()
print(numeros)

numeros.remove(1)  # Elimina primera ocurrencia
print(numeros)
```

### Ejercicio 5.3: Listas por Comprensión
```python
# Cuadrados del 1 al 10
cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)

# Pares
pares = [x for x in range(20) if x % 2 == 0]
print(pares)
```

### Ejercicio 5.4: Tuplas
```python
coordenadas = (10, 20)
x, y = coordenadas
print(f"X: {x}, Y: {y}")

# Tupla nombrada
from collections import namedtuple
Punto = namedtuple("Punto", ["x", "y"])
p = Punto(5, 3)
print(p.x, p.y)
```

## Entregables
- [ ] Lista con acceso y slicing
- [ ] Métodos append, sort, remove
- [ ] List comprehension
- [ ] Tupla básica y namedtuple

---

## Laboratorio 6: Diccionarios y Sets

---

## Objetivo

Usar colecciones clave-valor y conjuntos.

## Duración
20 minutos

### Ejercicio 6.1: Diccionarios
```python
estudiante = {
    "nombre": "Juan",
    "edad": 25,
    "carrera": "Desarrollo Python"
}
print(estudiante["nombre"])

# Agregar
estudiante["nota"] = 8.5

# Iterar
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
```

### Ejercicio 6.2: Diccionario con Funciones
```python
def buscar(diccionario, clave):
    return diccionario.get(clave, "No encontrado")

contactos = {"Juan": "juan@email.com", "María": "maria@email.com"}
print(buscar(contactos, "Juan"))
print(buscar(contactos, "Pedro"))
```

### Ejercicio 6.3: Sets
```python
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7}

# Unión
print(pares | impares)

# Intersección
print({1, 2, 3, 4} & {3, 4, 5, 6})  # {3, 4}
```

### Ejercicio 6.4: Contador de Palabras
```python
texto = "hola mundo hola python hola"
palabras = texto.split()
contador = {}

for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print(contador)  # {'hola': 3, 'mundo': 1, 'python': 1}
```

## Entregables
- [ ] Diccionario con CRUD
- [ ] Búsqueda con get
- [ ] Operaciones con sets
- [ ] Contador de palabras

---

## Laboratorio 7: Manejo de Archivos

---

## Objetivo

Leer y escribir archivos.

## Duración
25 minutos

### Ejercicio 7.1: Escribir Archivo
```python
with open("saludo.txt", "w") as archivo:
    archivo.write("Hola, Mundo!\n")
    archivo.write("Bienvenido a ")

print("Archivo creado!")
```

### Ejercicio 7.2: Leer Archivo
```python
with open("saludo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

### Ejercicio 7.3: CSV
```python
import csv

# Escribir
with open("datos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Juan", "25"])
    writer.writerow(["María", "30"])

# Leer
with open("datos.csv", "r") as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)
```

### Ejercicio 7.4: JSON
```python
import json

data = {
    "estudiantes": [
        {"nombre": "Juan", "nota": 8.5},
        {"nombre": "María", "nota": 9.0}
    ]
}

# Escribir
with open("datos.json", "w") as f:
    json.dump(data, f, indent=2)

# Leer
with open("datos.json", "r") as f:
    data = json.load(f)
    print(data)
```

## Entregables
- [ ] Archivo de texto escrito y leído
- [ ] Archivo CSV
- [ ] Archivo JSON

---

## Laboratorio 8: Módulos y Paquetes

---

## Objetivo

Crear y usar módulos.

## Duración
20 minutos

### Ejercicio 8.1: Módulo Personal
```python
# archivo: micodigo.py
def saludar():
    print("¡Hola!")

def sumar(a, b):
    return a + b
```

```python
# archivo: main.py
import micodigo

micodigo.saludar()
print(micodigo.sumar(5, 3))
```

### Ejercicio 8.2: from import
```python
from micodigo import saludar, sumar

saludar()
print(sumar(5, 3))
```

### Ejercicio 8.3: Biblioteca Estándar
```python
import random
print(random.randint(1, 10))

import datetime
print(datetime.datetime.now())

import math
print(math.sqrt(16))
```

### Ejercicio 8.4: Paquete
```
mi_paquete/
├── __init__.py
├── modulo1.py
└── modulo2.py
```

```python
from mi_paquete import modulo1
```

## Entregables
- [ ] Módulo personalizado creado
- [ ] Import funcionando
- [ ] Biblioteca estándar usada

---

## Laboratorio 9: Buenas Prácticas

---

## Objetivo

Aplicar PEP 8 y documentación.

## Duración
20 minutos

### Ejercicio 9.1: Docstrings
```python
def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base: Base del rectángulo
        altura: Altura del rectángulo
    
    Returns:
        Área calculada
    """
    return base * altura
```

### Ejercicio 9.2: TypeHints
```python
def saludar(nombre: str) -> str:
    """Saluda al usuario."""
    return f"¡Hola, {nombre}!"

def sumar(a: int, b: int) -> int:
    """Suma dos números."""
    return a + b

print(saludar("Juan"))
print(sumar(5, 3))
```

### Ejercicio 9.3: Excepciones
```python
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero"

print(dividir(10, 2))
print(dividir(10, 0))
```

### Ejercicio 9.4: Testing Básico
```python
def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def sumar(a, b):
    return a + b

test_sumar()
print("Todos los tests pasaron!")
```

## Entregables
- [ ] Docstrings en funciones
- [ ] TypeHints aplicados
- [ ] Manejo de excepciones
- [ ] Test básico pass

---

## Laboratorio 10: Proyecto Integrador

---

## Objetivo

Crear un sistema completo de gestión.

## Duración
60 minutos

### Sistema: Gestor de Estudiantes 

```python
# sistema.py
class Estudiante:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.notas = []
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

class Gestor:
    def __init__(self):
        self.estudiantes = {}
    
    def agregar(self, estudiante):
        self.estudiantes[estudiante.email] = estudiante
    
    def buscar(self, email):
        return self.estudiantes.get(email, None)
    
    def listar(self):
        return list(self.estudiantes.values())

# Uso
gestor = Gestor()

e1 = Estudiante("Juan", "juan@abacom.com")
e1.agregar_nota(8.5)
e1.agregar_nota(9.0)

e2 = Estudiante("María", "maria@abacom.com")
e2.agregar_nota(7.5)

gestor.agregar(e1)
gestor.agregar(e2)

for e in gestor.listar():
    print(f"{e.nombre}: {e.promedio():.2f}")
```

## Entregables
- [ ] Clase Estudiante funcionando
- [ ] Clase Gestor con CRUD
- [ ] Sistema completo ejecutándose

---

## Laboratorio 11: Git y GitHub

---

## Objetivo

Control de versiones para proyectos Python.

## Duración
30 minutos

### Ejercicio 11.1: Iniciar Repositorio
```bash
git init
git config user.name "Tu Nombre"
git config user.email "tu@email.com"
```

### Ejercicio 11.2: Comandos Básicos
```bash
# Ver estado
git status

# Agregar archivos
git add .
git add archivo.py

# Commit
git commit -m "Primer commit"

# Historial
git log --oneline

# Diferencias
git diff
```

### Ejercicio 11.3: Ramas
```bash
# Crear rama
git checkout -b feature/nueva

# Cambiar rama
git checkout main

# Merge
git merge feature/nueva
```

### Ejercicio 11.4: GitHub
```bash
# Crear repo en GitHub, luego:
git remote add origin https://github.com/user/repo.git
git push -u origin main
```

## Entregables
- [ ] Repositorio inicializado
- [ ] Commit realizado
- [ ] Repo en GitHub

---

*Desarrollo Python 2026*
*Licencia Creative Commons CC BY-NC-SA 4.0*