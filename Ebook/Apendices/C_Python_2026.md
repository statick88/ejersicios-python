# Apéndice C: Python 3.14 y el Ecosistema 2026

---

## C.1 Python 3.14: Novedades

### Cambios Principales

| Feature | Descripción | Estado |
|---------|-------------|--------|
| **Módulo `fsm`** | Finite State Machine | Nuevo |
| **Type Parameter Syntax** | Generic types simplificados | Preview |
| **Pattern Matching** | Mejoras | Estable |
| **Performance** | Faster startup | Optimizado |

### Instalación

```bash
# Usando pyenv (recomendado)
pyenv install 3.14.0
pyenv global 3.14.0

# O desde python.org
brew install python@3.14
```

### Verificar Versión

```bash
python --version  # Python 3.14.0
python3.14 --version
```

---

## C.2 Entornos Virtuales

### venv (incluido)

```bash
# Crear entorno
python -m venv env

# Activar
source env/bin/activate  # Linux/macOS
env\Scripts\activate    # Windows

# Instalar paquetes
pip install pytest ruff

# Desactivar
deactivate
```

### UV (recomendado 2026)

```bash
# Instalar uv
pip install uv

# Crear entorno
uv venv

# Instalar dependencias
uv pip install pytest ruff fastapi

# Ejecutar con entorno
uv run pytest
uv run python main.py
```

---

## C.3 Gestores de Paquetes

### pip (estándar)

```bash
# Instalar
pip install requests numpy pandas

# requirements.txt
pip freeze > requirements.txt

# Instalar desde requirements
pip install -r requirements.txt

# Instalar específica versión
pip install requests==2.31.0
```

### uv (recomendado)

```bash
# Instalar con uv (más rápido)
uv add requests
uv add "requests==2.31.0"
uv add -r requirements.txt

# Actualizar
uv lock
uv sync
```

### poetry

```bash
# Iniciar proyecto
poetry new mi_proyecto

# Agregar dependencia
poetry add requests

# Instalar
poetry install
```

### pipenv

```bash
# Instalar dependencia
pipenv install requests

# Ejecutar con entorno
pipenv run python main.py

# Shell interactivo
pipenv shell
```

---

## C.4Herramientas Esenciales 2026

### Linting

| Herramienta | Uso | Comando |
|------------|-----|----------|
| **ruff** | Linting rápido | `ruff check .` |
| **flake8** | Linting clásico | `flake8 .` |
| **pylint** | Análisis profundo | `pylint .` |

### Type Checking

| Herramienta | Uso | Comando |
|------------|-----|----------|
| **mypy** | Tipado estático | `mypy .` |
| **pyright** | Microsoft's | `pyright .` |

### Testing

| Herramienta | Uso | Comando |
|------------|-----|----------|
| **pytest** | Testing framework | `pytest` |
| **unittest** | Testing stdlib | `python -m unittest` |
| **coverage** | Coverage | `coverage run -m pytest` |

### Formateo

| Herramienta | Uso | Comando |
|------------|-----|----------|
| **ruff** | Format + Lint | `ruff format .` |
| **black** | Format código | `black .` |
| **isort** | Import sorting | `isort .` |

---

## C.5 Estructura de Proyecto Profesional

```
mi_proyecto/
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       ├── modulo.py
│       └── submodulo/
│           └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_modulo.py
│   └── test_submodulo.py
├── docs/
│   └── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
└── .env
```

### pyproject.toml

```toml
[project]
name = "mi-paquete"
version = "0.1.0"
description = "Descripción del paquete"
requires-python = ">=3.12"
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.4.0",
    "mypy>=1.8.0",
]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.pytest.ini_options]
testpaths = ["tests"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

---

## C.6 Web Frameworks

### FastAPI (recomendado)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola Mundo!"}

# Ejecutar
# uvicorn main:app --reload
```

### Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola Mundo!"

# python app.py
```

### Django

```bash
django-admin startproject miproyecto
cd miproyecto
python manage.py runserver
```

---

## C.7 Data Science

### Bibliotecas Esenciales

| Categoría | Herramientas |
|-----------|-------------|
| **Numeric** | numpy, pandas |
| **Visualization** | matplotlib, seaborn, plotly |
| **ML** | scikit-learn, tensorflow, pytorch |
| **Notebooks** | jupyter |

---

## C.8 Seguridad

### Dependencias Seguras

```bash
# Verificar vulnerabilidades
pip audit

# Actualizar paquetes
pip list --outdated

# Usar pip-audit
pip-audit
```

### Secretos en Código

```python
# ❌ NUNCA hacer esto
API_KEY = "sk-abcdef123456"

# ✅ Usar environment variables
import os
API_KEY = os.getenv("API_KEY")

# ✅ Usar python-dotenv
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
```

---

*Desarrollo Python 2026*
*Licencia Creative Commons CC BY-NC-SA 4.0*