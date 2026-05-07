# Python 2026 - Ejercicios Prácticos

**[ebook: python-2026-ebook](https://github.com/statick88/python-2026-ebook)** | **[curso web](https://abacom.dev/python)**

> 🐍 **Aprende Python desde cero hasta IA** — 12 módulos progresivos con ejercicios prácticos

## 📚 Contenido del Curso

Este repositorio contiene **ejercicios prácticos** complementarios al ebook. Cada rama tiene el contenido de una unidad específica.

### Estructura por Módulos

| Módulo | Rama | Tema | Archivos |
|--------|------|------|---------|
| M0 | `m0-intro` | Introducción y conceptos básicos | 3 |
| M1 | `m1-vars` | Variables y tipos de datos | 3 |
| M2 | `m2-ops` | Operadores | 3 |
| M3 | `m3-flow` | Control de flujo (if, for, while) | 2 |
| M4 | `m4-func` | Funciones | Funciones/ |
| M5 | `m5-poo` | Programación Orientada a Objetos | POO/ |
| M6 | `m6-coll` | Colecciones (listas, diccionarios, etc.) | - |
| M7 | `m7-file` | Archivos y persistencia | - |
| M8 | `m8-err` | Manejo de errores | - |
| M9 | `m9-test` | Testing y QA | - |
| M10 | `m10-proj` | Proyecto integrador | - |
| M11 | `m11-ia` | Introducción a IA | - |

## 🚀 Cómo Usar Este Repositorio

### Opción 1: Por Ramas (Contenido Específico por Unidad)

```bash
# Ver todas las ramas disponibles
git branch -a

# Cambiar a una rama específica (ej: M1 - Variables)
git checkout m1-vars

# Ver contenido
ls -la Introduccion/
```

### Opción 2: Clonar Todo (Todas las Ramas)

```bash
# Clonar con todas las ramas
git clone --branch main --single-branch https://github.com/statick88/ejercicios-python.git

# Ver ramas remotas
git fetch origin

# Explorar cada rama
for branch in m0-intro m1-vars m2-ops m3-flow m4-func m5-poo; do
  git checkout $branch
  echo "=== $branch ==="
  ls -la
done
```

## 📖 Relacionado con el Ebook

El **contenido teórico** vive en el ebook separado:

👉 **[python-2026-ebook](https://github.com/statick88/python-2026-ebook)**

```
ebook/
├── M0_Pensamiento_Computacional.md
├── M1_Variables_Tipos.md
├── M2_Operadores.md
├── M3_Control_Flujo.md
├── M4_Funciones.md
├── M5_POO_Persistencia.md
├── M10_Proyecto_Integrador.md
├── M11_IA_Desarrolladores.md
└── Lab/
```

## 🎯 Objetivos de Aprendizaje

Al completar este curso podrás:

- ✅ Escribir programas en Python desde cero
- ✅ Entender tipos de datos y operadores
- ✅ Controlar el flujo de ejecución
- ✅ Crear funciones reutilizables
- ✅ Aplicar POO (Programación Orientada a Objetos)
- ✅ Trabajar con archivos y datos persistentes
- ✅ Escribir tests básicos
- ✅ Construir un proyecto completo

## 🛠️ Requisitos

- Python 3.10+ (verificado en 3.14)
- Editor de código (VS Code recomendado)

## 📝 Ejecutar los Ejercicios

```bash
# Ejecutar un ejercicio
python Introduccion/m0_introduccion.py

# Ejecutar con argumentos
python Introduccion/ejercicio_01.py arg1 arg2

# Ver estructura de un módulo
python -c "import Introduccion.m0_introduccion"
```

## 🔄 Contributing

¿Encontraste un error o tienes sugerencias?

1. Fork del repo
2. Crea una rama: `git checkout -b fix/descripcion`
3. Commitea tus cambios: `git commit -m 'fix: descripción'`
4. Push: `git push origin fix/descripcion`
5. Abre un Pull Request

## 📄 Licencia

MIT License - Feel free to use and modify.

---

**Edgar Cifuentes** | [ABACOM](https://abacom.dev/python) | 2026
