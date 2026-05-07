# Ebook: Desarrollo Python 2026

## Módulo 11: 🤖 Inteligencia Artificial para Desarrolladores

---

### Objetivo

Al finalizar este capítulo, el estudiante comprenderá el ecosistema de IA en 2026, configurará OpenCode con perfiles personalizados, integrará agentes especializados, y aplicará Spec-Driven Development (SDD) con asistencia de IA.

> **La forma de programar en 2026**: El desarrollador no es el que escribe cada línea de código, sino el **director de orquesta** que especifica qué debe hacerse y valida que el resultado coincida con la especificación. La IA ejecuta; el humano valida.

---

## 11.1 El Ecosistema de IA en 2026

### Modelos de Lenguaje (LLMs)

| Modelo | Proveedor | Características | Mejor para |
|--------|----------|---------------|-----------|
| **Opus 4** | Anthropic | Reasoning avanzado, código | Desarrollo complejo |
| **Sonnet 4** | Anthropic | Balance velocidad/costo | Uso diario |
| **Haiku** | Anthropic | Rápido, económico | Tareas simples |
| **GPT-4o** | OpenAI | Multimodal, código | Desarrollo general |
| **GPT-4o Mini** | OpenAI | Rápido, barato | Prototipado |
| **Gemini 2.5 Pro** | Google | Long context, reasoning | Proyectos grandes |
| **Gemini 2.5 Flash** | Google | Velocidad | Respuestas rápidas |
| **Minimax** | Minimax | Código abierto | Privacidad |
| **Kimi** | Kimi | Contexto largo | Documentación |
| **GLM-4** | Zhipu | Código chino | Mercados asiáticos |
| **Llama 4** | Meta | Código abierto | Autohospedaje |
| **Qwen 2.5** | Alibaba | Código abierto | Desarrollo local |

### Modelos de Escritura de Código

| Herramienta | Proveedor | Especialidad |
|------------|----------|-------------|
| **Claude Code** | Anthropic | Desarrollo agente |
| **Gemini Code** | Google | Código + context |
| **Copilot** | Microsoft/GitHub | Autocompletado IDE |
| **Codex** | OpenAI | Generación código |
| **Kiro Code** | Kiro | Código alternativo |
| **Kilo Code** | Kiro | Código ligero |
| **AMP Code** | Various | Código mobile |
| **Pi Code** | Various | Código Python |

---

## 11.2 OpenCode: El Director de Orquestas

### ¿Qué es OpenCode?

OpenCode es un CLI agentic que asiste en desarrollo de software. A diferencia de completar código, OpenCode **ejecuta tareas** siguiendo especificaciones.

```
Usuario (Director) → OpenCode (Orquesta) → Agentes (Músicos) → Código (Sinfonía)
```

### Perfiles de Usuario

En `~/.config/opencode/AGENTS.md`:

```markdown
# Perfil: Diego Saavedra

## Metodología
Spec-Driven Development (SDD)

## Preferencias
- TypeScript strict mode
- pytest para Python
- Tailwind CSS 4
- React Native para mobile

## Restricciones
- NO generar código sin especificación
- ALWAYS verificar con tests
- NO hacer commit sin code review

## Skills por Rol
- developer: FullStack + React Native + SDD
- security: Pentesting + vulnerabilidades
- qa: Testing + linting + typecheck
- design: UI/UX + Apple HIG
```

### Estructura de Comandos

```bash
# Iniciar sesión
opencode

# Ejecutar tarea específica
opencode implement " HU-001: Login"

# Generar especificación
opencode spec "registro de usuarios"

# Verificar implementación
opencode verify

# Revisión de código
opencode review
```

---

## 11.3 Agentes y Subagentes

### Agentes Principales

| Agente | Descripción | Especialidad |
|--------|-------------|--------------|
| **developer** | FullStack Developer | React, Flutter, Python, SDD |
| **explore** | Explorador de código | Búsqueda de patrones |
| **sdd-apply** | Implementador | Código desde specs |
| **sdd-verify** | Verificador | Validación línea a línea |
| **qa-engineer** | QA Engineer | Tests, linting |
| **security** | Security Review | OWASP, vulnerabilidades |
| **design** | Design Review | UI/UX, Apple HIG |

### Subagentes de Soporte

```
Agente Principal
    ├── explore
    │   ├── pm-hu        (Product Manager)
    │   └── sdd-spec     (Spec Writer)
    │
    ├── sdd-design
    │   └── sdd-design-ui    (Design Agent)
    │
    ├── sdd-apply
    │   ├── sdd-tasks      (Task Breakdown)
    │   └── coding        (Code Implementation)
    │
    ├── sdd-verify
    │   ├── code-review   (Code Quality)
    │   └── testing      (Test Validation)
    │
    ├── qa-engineer
    │   ├── linting      (ESLint, Ruff)
    │   ├── typecheck   (TypeScript, mypy)
    │   └── test         (pytest, Jest)
    │
    ├── security-reviewer
    │   ├── vulnerability-scan
    │   ├── dependency-scan (CVE)
    │   └── secret-scan
    │
    └── design-reviewer
        ├── ui-check
        ├── accessibility (WCAG)
        └── apple-hig
```

### Flujo de Trabajo SDD

```
┌─────────────────────────────────────────────────────────────────────┐
│                     SDD WORKFLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│ HU (Historia de Usuario) ──► [Refine] ──► [Close]       │
│         │                      │                   │             │
│         ▼                      ▼                   ▼             │
│ High Level Technical Contract ─► [HITL APPROVAL]              │
│                                      │                    │
│                                      ▼                    │
│ Tasks ──► implement ──► [QA + SECURITY + DESIGN] ──► verify│
│              │                         │                    │
│              ▼                         ▼                    │
│         Emulator Test ──► [Final Score] ─► Archive      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 11.4 MCP: Model Context Protocol

### ¿Qué es MCP?

MCP (Model Context Protocol) es un estándar para conectar agentes IA con herramientas externas.

```python
# Ejemplo: MCP para base de datos
from mcp import DatabaseMCP

db = DatabaseMCP("postgresql://localhost/abacom")

# El agente puede ejecutar SQL directamente
query = "SELECT * FROM estudiantes WHERE programa = 'Python'"
resultados = db.query(query)
```

### MCPs Disponibles

| MCP | Función | Uso |
|-----|---------|-----|
| **Database** | Consultas SQL | SQLite, PostgreSQL, MySQL |
| **FileSystem** | Lectura/escritura | Archivos locales |
| **HTTP** | Requests | APIs externas |
| **Playwright** | Browser automation | Testing E2E |
| **Git** | Version control | Git operations |
| **Notion** | Base de datos | Documentación |
| **Slack** | Mensajería | Notificaciones |
| **Jira** | Project management | Tickets |

---

## 11.5 Skills: Habilidades del Agente

### ¿Qué son los Skills?

Skills son configuraciones que determinan cómo el agente aborda una tarea.

### Instalar un Skill

```bash
# Desde el directorio del skill
opencode skill install ./skills/react-native

# O desde URL
opencode skill install github:statick88/react-skills
```

### Skills por Rol

```python
# En AGENTS.md
## Agent Skills

### security
- software-security
- pentest-methodology
- vulnerability-research

### qa
- pytest
- playwright
- testing-best-practices

### design
- apple-mobile-design
- ui-ux-pro-max
- accessibility

### developer
- react-native
- flutter
- nextjs-15
```

### Estructura de un Skill

```
skills/
└── mi-skill/
    ├── SKILL.md          # Definición del skill
    ├── prompts/         # Plantillas
    ├── tools/          # Scripts auxiliares
    └── examples/        # Casos de uso
```

### Skill ejemplo: Python Developer

```markdown
# SKILL.md
name: python-developer
description: Python development with best practices
triggers:
  - python
  - django
  - flask
  - fastapi
  - pytest

commands:
  lint: ruff check .
  test: pytest
  typecheck: mypy
  format: ruff format

patterns:
  - "*.py"
  - "test_*.py"
  - "*_test.py"
```

---

## 11.6 Engram: Memoria Persistente

### El Problema de la Amnesia

Cada vez queinicias una nueva sesión con un agente IA, este **olvida** todo lo que se habló antes.

### Solución: Engram

Engram persist decisions, aprendizajes y contexto entre sesiones.

```python
from engram import Engram

# Guardar decisión
engram.save(
    title="Arquitectura DB",
    content="Usar SQLite para Engram",
    type="architecture"
)

# Buscar contexto previo
resultados = engram.search("Python")
```

### Tablas de Engram

| Tabla | Contenido |
|-------|-----------|
| `sesiones` | Historial de trabajo |
| `observaciones` | Decisiones, aprendizajes |
| `decisiones` | ARQ, configuración |
| `prompt_history` | Historial de prompts |

---

## 11.7 Spec-Driven Development (SDD)

### Metodología SDD

SDD transforma al programador de "picacódigo" en **arquitecto y director del proceso**.

```
Entrada: Historia de Usuario (HU)
    ↓
[Refine] → Spec detallada
    ↓
[Close Decisions] → Decisiones tomadas
    ↓
[Design] → Contrato técnico
    ↓
[HitL Approval] → OK humano
    ↓
[Apply] → Código
    ↓
[Verify] → Validación
    ↓
QA + Security + Design Gates
    ↓
[Emulator Test] → Prueba final
    ↓
[Score] → Puntuación 1-10
```

### Gates de Calidad

| Gate | Verificación |
|------|-------------|
| **QA** | Unit tests, linting, typecheck |
| **Security** | No vulnerabilidades |
| **Design** | UI/UX, Apple HIG |
| **Emulator** | iOS + Android test |

---

## 11.8 Configuración de Agentes Personalizados

### Archivo: agents.md

```markdown
# Agentes Personalizados para 

## Agente: Professor

- role: educator
- expertise: Python, desarrollo móvil
- communication: educativo, motivación
- tools: skill-loader, quiz-generator

## Agente: Security Expert

- role: pentester  
- expertise: OWASP, vulnerabilidades
- tools: vulnerability-scan, dependency-scan
- triggers: security, pentest, CVE

## Agente: FullStack Dev

- role: developer
- expertise: React Native, Flutter, Python
- tools: react-native-skill, flutter-skill
- methodology: SDD
```

### Directorio: agentes/

```
agentes/
├── agente_personalizado_1.md    # Configuración
├── agente_personalizado_2.md    # Configuración
└── prompts/
    ├── system_prompt.md
    └── user_prompt.md
```

### Ejemplo: Agente Profesor

```markdown
# Agente: Professor 

## Rol
Educador y mentor para estudiantes de desarrollo Python

## Especialidad
- Python básico y avanzado
- Desarrollo móvil con React Native
- Metodología SDD

## Comportamiento
- Explicaciones claras y progresivas
- Ejemplos prácticos
- Ejercicios con feedback

## Herramientas
- skill: abacom-cursos
- skill: gentle-teaching

## Restricciones
- NO dar respuestas directas
- SIEMPRE guiar al descubrimiento
- Adaptar al nivel del estudiante
```

---

## 11.9 Instalación y Configuración

### Requisitos

```bash
# Node.js 20+
node --version  # >= 20.0.0

# Python 3.12+
python --version  # >= 3.12

# Git
git --version
```

### Instalación de OpenCode

```bash
# Instalar OpenCode
npm install -g opencode

# Verificar
opencode --version
```

### Configuración Inicial

```bash
# Crear configuración
mkdir -p ~/.config/opencode

# Copiar config base
cp config/opencode.yaml ~/.config/opencode/

# Configurar perfil
opencode configure --profile developer
```

### AGENTS.md Base

```markdown
# Mi Perfil: Desarrollador 

## Metodología
Spec-Driven Development (SDD)

## Preferencias
- python: 3.12+
- typescript: strict
- package-manager: pnpm

## Skills
- python-best-practices
- react-native
- software-security

## Restricciones
- NO generar sin especificación
- ALWAYS verificar tests
- NO secrets en código
```

---

## 11.10 Resumen y Criterios de Aceptación

| Tema | Concepto Clave | Herramienta |
|------|---------------|-----------|
| Modelos IA | LLM para código | Opus, Sonnet, GPT, Gemini |
| OpenCode | CLI agentic | opencode CLI |
| Agentes | Especialistas por rol | developer, qa, security |
| MCPs | Herramientas externas | Database, Git, HTTP |
| Skills | Habilidades | python-dev, react-native |
| Engram | Memoria | SQLite persistente |
| SDD | Metodología | HU → Spec → Code |

### Criterios de Aceptación

| Criterio | Verificación |
|----------|-------------|
| OpenCode instalado | `opencode --version` |
| Perfil configurado | `opencode whoami` |
| Skills cargados | `opencode skills list` |
| Agentes personalizados | Directorio `agentes/` existe |
| Engram funcional | Guardar → buscar → encuentra |
| SDD workflow | HU → spec → code → verify |

---

*Desarrollo Python 2026*
*Licencia Creative Commons CC BY-NC-SA 4.0*
*Spec-Driven Development | QA | Security | Design*