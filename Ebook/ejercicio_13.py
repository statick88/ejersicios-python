#!/usr/bin/env python3
"""
Ejercicio M11.1: IA para Desarrolladores
=======================================

练习: Herramientas de IA para desarrolladores

Libro: M11_IA_Desarrolladores.md

Este ejercicio explica herramientas de IA útiles para programadores.
"""

# ==========================================
# 1. OPENCODE - Desarrollo Guiado por Specs
# ==========================================

"""
OpenCode es un entorno de desarrollo donde:
- El humano especifica qué quiere (SPEC)
- La IA ejecuta el código
- El humano valida el resultado

SDD = Spec-Driven Development
→ HU (Historia de Usuario) → Spec → Code → Verify
"""

print("=" * 50)
print("MÓDULO 11: IA PARA DESARROLLADORES")
print("=" * 50)

# ==========================================
# 2. CONCEPTOS CLAVE
# ==========================================

conceptos = {
    "SDD": "Spec-Driven Development - desarrollo guiado por especificaciones",
    "AGENTS": "Agentes IA especializados (QA, Security, Design)",
    "ENGRAM": "Memoria persistente para agentes IA",
    "SKILLS": "Habilidades configurables para agentes"
}

print("\n2. Conceptos clave de IA para desarrolladores:")
for concepto, significado in conceptos.items():
    print(f"  {concepto}: {significado}")

# ==========================================
# 3. HABILIDADES (SKILLS) DE AGENTES
# ==========================================

skills = {
    "qa_engineer": " QA, testing, linting, typecheck",
    "security_reviewer": " OWASP, vulnerabilidades",
    "design_reviewer": " UI/UX, Apple HIG",
    "sdd_spec": " Especificaciones detallada",
    "sdd_verify": " Verificación contra specs"
}

print("\n3. Skills de agentes especializados:")
for skill, desc in skills.items():
    print(f"  • {skill}: {desc}")

# ==========================================
# 4. HERRAMIENTAS DE IA
# ==========================================

herramientas = [
    ("Context7", "Documentación actualizada"),
    ("NotebookLM", " investigación y resúmenes"),
    ("OpenCode", "Desarrollo con agentes"),
    ("ChatGPT/Claude", "Asistencia general")
]

print("\n4. Herramientas de IA útiles:")
for h, d in herramientas:
    print(f"  {h}: {d}")

# ==========================================
# 5. WORKFLOW DE DESARROLLO CON IA
# ==========================================

print("""
5. Workflow de desarrollo con IA:
   
   ┌─────────────┐
   │    USER    │  ← Pide algo
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │  EXPLORE    │  ← Analiza Requirements
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │    SPEC     │  ← Especificación detallada
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │    CODE    │  ← IA escribe código
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │  VERIFY    │  ← Verificar contra spec
   └───────────┘
""")

# ==========================================
# 6. ENGRAM - MEMORIA DE AGENTES
# ==========================================

print("""
6. Engram - Memoria persistente:
   
   - Solve problema de "amnesia" de agentes
   - Persiste contexto entre sesiones
   -Guarda decisiones y patrones
   - Historial de trabajo

   Uso: mem_save() después de completar trabajo
""")

# ==========================================
# 7. RECURSOS ADICIONALES
# ==========================================

print("""
7. Recursos adicionales:
   
   • Documentación: Context7 (librería/docs)
   • Investigación: NotebookLM
   • Código: GitHub Copilot, Cursor
   • Documentación: Readme, SPEC.md
   
   Links útiles:
   - github.com/statick88/ejersicios-python
   - Ebook/ (contenido del curso)
""")

print("\n" + "=" * 50)
print("¡EJERCICIO COMPLETADO!")
print("Continúa aprendiendo Python y explora herramientas de IA")
print("=" * 50)