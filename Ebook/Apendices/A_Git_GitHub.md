# Apéndice A: Git y GitHub con Python

---

## A.1 Conceptos Fundamentales

### ¿Qué es Git?
Git es un sistema de control de versiones distribuido. Permite rastrear cambios en código fuente durante el desarrollo de software.

### ¿Qué es GitHub?
GitHub es una plataforma de hosting para repositorios Git. Permite colaboración entre desarrolladores.

---

## A.2 Comandos Esenciales

### Configuración Inicial
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Verificar configuración
git config --list
```

### Iniciar Repositorio
```bash
# Crear nuevo repositorio
git init

# Clonar repositorio existente
git clone https://github.com/usuario/repositorio.git
```

### Estados de Archivo
```
 Working    →    Staging    →    Repository
 (editado)      (git add)      (git commit)
```

### Comandos Básicos
```bash
# Ver estado
git status

# Ver cambios
git diff

# Agregar archivos
git add archivo.py      # archivo específico
git add .              # todos los archivos
git add *.py            # todos los .py

# Confirmar cambios
git commit -m "Mensaje descriptivo"

# Historial
git log
git log --oneline      # formato compacto
git log -n 5           # últimos 5 commits

# Ver diferencias
git diff               # sin staged
git diff --staged       # en staging
```

---

## A.3 Ramas (Branches)

```bash
# Crear rama
git checkout -b feature/nueva

# Listar ramas
git branch

# Cambiar rama
git checkout main
git checkout develop

# Eliminar rama
git branch -d nombre_rama

# Fusionar rama
git merge feature/nueva
```

---

## A.4 Trabajo Remoto

```bash
# Añadir remoto
git remote add origin https://github.com/user/repo.git

# Ver remotos
git remote -v

# Empujar (primera vez)
git push -u origin main

# Empujar (actualizar)
git push

# Traer
git pull

# Fetch + Merge
git fetch origin
git merge origin/main
```

---

## A.5 .gitignore

```bash
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
.venv/

# Virtual environments
venv/
ENV/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/

# Secrets
.env
*.key
credenciales.json
```

---

## A.6 gitflow Simple para Python

```
main ─────●─────●─────●─────●──
          ↑
   hotfix/patch
   
develop ──●───●───●───●─────►
          ↑   ↑   ↑
     feature/1 feature/2
```

### Convenciones de Commits

```
feat: Mensaje    → Nueva funcionalidad
fix: Mensaje    → Corrección de bug
docs: Mensaje   → Documentación
style: Mensaje → Formateo (sin cambio de código)
refactor: Mensaje → Refactorización
test: Mensaje   → Tests
chore: Mensaje  → Mantenimiento
```

### Ejemplo
```bash
git add .
git commit -m "feat: agregar función promedio

- Nueva función calcular_promedio()
- Añadidos type hints
- Añadido test básico"
```

---

## A.7 GitHub Actions para Python

```yaml
# .github/workflows/python.yml
name: Python Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest ruff
    
    - name: Lint
      run: ruff check .
    
    - name: Test
      run: pytest
```

---

## A.8 Common Issues

| Problema | Solución |
|---------|----------|
| "detached HEAD" | `git checkout main` |
| Merge conflicts | Editar archivos conflicted, luego `git add .` + `git commit` |
| Commit errado | `git commit --amend` (si no hecho push) |
|git add errado | `git reset HEAD archivo` |
|Olvidar commit | `git stash` para guardar cambios temporales |

---

*Desarrollo Python 2026*
*Licencia Creative Commons CC BY-NC-SA 4.0*