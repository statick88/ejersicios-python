# Módulo 0: Pensamiento Computacional

---

## Objetivo

Desarrollar la capacidad de abordar problemas y resolverlos mediante procedimientos paso a paso, sentando las bases del pensamiento algorítmico antes de escribir código.

---

## 0.1 ¿Qué es la Computación?

### De Recetas a Algoritmos

La computación no es solo "usar computadoras". Es **pensar de manera sistemática** para resolver problemas.

**Analogía: Receta de cocina = Algoritmo**

```
Receta (cocina)              Algoritmo (computación)
─────────────────────────────────────────────────
Ingredientes    →           Datos de entrada
Pasos específicos →          Instrucciones
Resultado      →           Salida
Tiempo/horno   →            Procesador
```

### Ejemplo: Hacer un café

```
Algoritmo: Hacer café
────────────────────
1. Hierve agua
2. Muele café
3. poné café en filtro
4. Verter agua caliente
5. Servir en taza
```

---

## 0.2 Descomposición: Dividir para Conquistar

### El Problema Grande → Piezas Pequeñas

Cuando enfrentas un problema grande, **divídelo en partes manejables**.

**Problema:** Gestionar una lista de estudiantes

**Descomposición:**
```
├── Registrar estudiante
│   ├── Pedir nombre
│   ├── Pedir email
│   └── Guardar en lista
├── Mostrar estudiantes
│   ├── Acceder a lista
│   └── Imprimir cada uno
├── Buscar estudiante
│   ├── Pedir nombre a buscar
│   └── Comparar con lista
└── Eliminar estudiante
    ├── Pedir identificación
    └── Remover de lista
```

---

## 0.3 Patrones y Abstracción

### Reconocer lo Repetitivo

No resuelvas lo mismo dos veces. **Identifica patrones**.

**Ejemplo: Calculadora de áreas**

```
Área cuadrado: lado × lado
Área rectángulo: base × altura  
Área triángulo: (base × altura) / 2

¿Ves el patrón?
Todos son "multiplicar dos valores"
→ Abstracción: área = valor1 × valor2
```

### Abstracción

**Abstraer** = Ignorar detalles innecesarios, enfocar lo esencial.

```
Sistema de archivos     →   Pensamos en "carpetas y archivos"
(no pensamos en bits) →   (abstracción)

Calculadora           →   Pensamos en "operaciones"  
(no pensamos en circuitos)
```

---

## 0.4 Diseño de Algoritmos: Pseudocódigo

### Antes que Python: Pseudocódigo

El **pseudocódigo** es escribir el algoritmo en lenguaje humano simplificado.

### Estructuras Básicas

```
SECUENCIA (orden lineal)
─────────────────────
instrucción 1
instrucción 2
instrucción 3

CONDICIÓN (if/else)
───────────────────
SI condición ENTONCES
    hacer algo
SINO
    hacer otra cosa
FIN SI

REPETICIÓN (for/while)
──────────────────────
PARA cada elemento EN lista
    hacer algo
FIN PARA

MIENTRAS condición
    hacer algo
FIN MIENTRAS
```

### Ejemplo: Encontrar el mayor

```
Pseudocódigo:
────────────────
1. Iniciar mayor = 0
2. PARA cada número EN lista
3.     SI número > mayor ENTONCES
4.         mayor = número
5.     FIN SI
6. FIN PARA
7. RETORNAR mayor
```

### Traducción a Python

```python
def encontrar_mayor(numeros):
    mayor = 0
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor

# Prueba
assert encontrar_mayor([3, 7, 2, 9, 1]) == 9
print("¡Funciona!")
```

---

## 0.5 Evaluación deErrores

### Errores Comunes

| Error | Descripción | Solución |
|-------|-------------|----------|
| **Asumir** | No entender el problema completo | Leer varias veces |
| **Saltar pasos** | Ir directo a código | Pseudocódigo primero |
| **No probar** | No verificar con datos reales | Testear siempre |
| **Una solución** | No buscar alternativas | Pensar múltiples formas |

### Metodología de Debug

```
1. Reproducir el error
2. Aislar el problema  
3. Hipotetizar causa
4. Probar fix
5. Verificar y documentar
```

---

## Resumen del Módulo 0

| Concepto | Descripción |
|---------|-------------|
| **Algoritmo** | Paso a paso para resolver problema |
| **Descomponer** | Dividir problema grande en partes |
| **Abstraer** | Enfocarse en lo esencial |
| **Pseudocódigo** | Algoritmo en lenguaje humano |
| **Debugging** | Encontrar y corregir errores |

---

## Ejercicios Pensamiento Computacional

### Ejercicio 0.1: Pseudocódigo
```
Escribir pseudocódigo para:
- Hacer un sandwich
- Buscar una palabra en un libro
- Calculadora de promedio de notas
```

### Ejercicio 0.2: Descomponer
```
Descomponer en 3 partes:
- Sistema de reservas de cine
- Carrito de compras
- Traductor idiomas
```

### Ejercicio 0.3: Encontrar patrón
```
¿Qué patrón observas?
- 2, 4, 6, 8, 10...
- a, e, i, o, u
- lunes, martes, mércoles...
```

---

## Checklist de Módulo 0

- [ ] Comprendo qué es un algoritmo
- [ ] Puedo descomponer problemas
- [ ] Reconozco patrones
- [ ] Escribo pseudocódigo básico
- [ ] Aplico metodología de debug

---

*Pensamiento Computacional - Fundamento para Programación*