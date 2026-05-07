# Curso Python 2026 - Ejercicios Prácticos

---

## 📚 Acerca del Curso

Este repositorio contiene ejercicios prácticos para aprender Python desde cero hasta nivel intermedio. El curso está diseñado para ser循序渐进 (progresivo), donde cada rama contiene el código de una unidad específica.

**Licencia:** Creative Commons CC BY-NC-SA 4.0

---

## 📋 Estructura del Curso

### 11 Módulos

| Módulo | Tema | Rama Git |
|--------|------|----------|
| M0 | Introducción | `m0-intro` |
| M1 | Variables y Tipos | `m1-vars` |
| M2 | Operadores | `m2-ops` |
| M3 | Control de Flujo | `m3-flow` |
| M4 | Funciones | `m4-func` |
| M5 | POO | `m5-poo` |
| M6 | Colecciones | `m6-coll` |
| M7 | Archivos | `m7-file` |
| M8 | Errores | `m8-err` |
| M9 | Testing | `m9-test` |
| M10 | Proyecto Final | `m10-proj` |
| M11 | IA para Desarrolladores | `m11-ia` |

---

## 🚀 Cómo Usar Este Repositorio

### Opción 1: Por Rama (Recomendado para estudiantes)

Cada rama contiene el código de esa unidad Y las anteriores:

```bash
# Clonar el repositorio
git clone https://github.com/statick88/ejersicios-python.git
cd ejersicios-python

# Cambiar a la rama de tu unidad
git checkout m0-intro   # Para M0
git checkout m1-vars    # Para M1 (incluye M0)
git checkout m2-ops      # Para M2 (incluye M0+M1)
# ... y así sucesivamente
```

### Opción 2: Ver Código por Archivo

Explora los archivos directamente:

```
Introduccion/
├── m0_introduccion.py    # Teoría M0
├── m1_variables_tipos.py # Teoría M1
├── m2_operadores.py      # Teoría M2
├── m3_control_flujo.py  # Teoría M3
├── m6_colecciones.py     # Teoría M6
└── ejercicio_01.py        # Ejercicio M0.1
    ├── ejercicio_02.py   # Ejercicio M0.2
    └── ejercicio_03.py   # Ejercicio M1.1

Funciones/
├── m4_funciones.py       # Teoría M4
├── ejercicio_06.py       # Ejercicio M4.1
└── ejercicio_10.py      # Ejercicio M8.1

POO/
├── m5_poo.py           # Teoría M5
└── ejercicio_07.py      # Ejercicio M5.1

Archivos/
├── m7_archivos.py       # Teoría M7
└── ejercicio_09.py      # Ejercicio M7.1
```

---

## 📖 Contenido del Ebook

El curso incluye un ebook completo en la carpeta `Ebook/`:

```
Ebook/
├── 00_Índice.md           # Índice general
├── M0_Pensamiento_Computacional.md
├── M1_Variables_Tipos.md
├── M2_Operadores.md
├── M3_Control_Flujo.md
├── M4_Funciones.md
├── POO_Persistencia.md    # M5 + M7
├── M10_Proyecto_Integrador.md
└── M11_IA_Desarrolladores.md
```

---

## 💻 Ejecutar los Ejercicios

```bash
# Verificar Python instalado
python --version

# Ejecutar ejercicio específico
python Introduccion/ejercicio_01.py

# Ejecutar todos los de una carpeta
python -m pytest tests/  # Para tests
```

---

## 🎯 Objetivos por Módulo

### M0 - Introducción
- Ejecutar tu primer programa
- Usar print() e input()
- Comprender variables básicas

### M1 - Variables y Tipos
- Trabajar con str, int, float, bool
- Convertir entre tipos (casting)
- Usar f-strings

### M2 - Operadores
- Aritméticos (+, -, *, /)
- Comparación (==, !=, <, >)
- Lógicos (and, or, not)

### M3 - Control de Flujo
- if/elif/else
- for y while
- break y continue

### M4 - Funciones
- Crear funciones
- Parámetros y return
- *args y **kwargs
- Lambda

### M5 - POO
- Clases y objetos
- Herencia
- Encapsulación

### M6 - Colecciones
- Listas, tuplas
- Diccionarios
- Sets

### M7 - Archivos
- Leer y escribir archivos
- JSON y CSV

### M8 - Errores
- try/except
- Excepciones personalizadas

### M9 - Testing
- pytest básico
- Assertions
- Fixtures

### M10 - Proyecto
- Integrar todos los conceptos

### M11 - IA
- Herramientas de IA para desarrolladores
- OpenCode, SDD, Engram

---

## 🤝 Contribuir

1. Fork del repositorio
2. Crear rama: `git checkout -b mi-mejora`
3. Hacer cambios
4. Commit: `git commit -m "feat: mi mejora"`
5. Push: `git push origin mi-mejora`
6. Pull Request

---

## 📞 Contacto

- **GitHub:** github.com/statick88/ejersicios-python
- **Curso:** Python 2026

---

## 📄 Licencia

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Licencia Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>

Este curso está bajo licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons BY-NC-SA 4.0</a>.

---

*Python 2026 - Curso Práctico*