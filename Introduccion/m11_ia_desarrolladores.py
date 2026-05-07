#!/usr/bin/env python3
"""
Módulo 11: Introducción a la IA para Desarrolladores
===================================================

Este módulo introduce conceptos básicos de IA/ML
aplicados al desarrollo de software.

Libro: M11_IA_Desarrolladores.md
"""

# ==========================================
# 1. ¿Qué es IA?
# ==========================================

print("=== Introducción a la IA ===")
print("""
IA (Inteligencia Artificial):
- Rama de la computación que crea sistemas capaces de aprender
- ML (Machine Learning): La máquina aprende de los datos
- DL (Deep Learning): Redes neuronales profundas
- GenAI: IA Generativa (GPT, Claude, etc.)
""")

# ==========================================
# 2. EJEMPLO BÁSICO: Clasificación
# ==========================================

# Datos de entrenamiento
datos_entrenamiento = [
    [25, 50000],   # persona joven, bajo salario
    [35, 80000],   # persona mayor, alto salario
    [28, 60000],   # persona joven, salario medio
    [45, 90000],   # persona mayor, alto salario
    [30, 55500],   # persona joven, salario medio
]

# Etiquetas (0: clase baja, 1: clase alta)
etiquetas = [0, 1, 0, 1, 0]

# Predicción simple (sin ML real)
def predecir_clase(edad, salario):
    """Predicción simple basada en reglas."""
    if edad > 35 and salario > 70000:
        return 1  # Clase alta
    return 0  # Clase baja

# Probar predicción
prueba_edad = 40
prueba_salario = 85000
prediccion = predecir_clase(prueba_edad, prueba_salario)
print(f"Predicción para edad={prueba_edad}, salario={prueba_salario}")
print(f"Clase predicha: {'Alta' if prediccion == 1 else 'Baja'}")

# ==========================================
# 3. IA GENERATIVA
# ==========================================

print("\n=== IA Generativa ===")
print("""
Herramientas de IA Generativa para desarrolladores:
- GitHub Copilot: Código assist
- Claude/ChatGPT: Asistente de código
- NotebookLM: Investigación y aprendizaje

Aplicaciones:
- Generación de código
- Debugging y refactoring
- Documentación automática
- Revisión de código
""")

# ==========================================
# 4. HERRAMIENTAS PARA PYTHON
# ==========================================

print("=== Herramientas de IA en Python ===")
print("""
# Instalar bibliotecas de IA
pip install scikit-learn  # ML básico
pip install tensorflow   # Deep Learning
pip install openai       # API de OpenAI
pip install anthropic   # API de Claude

# Uso básico de sklearn
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
""")

# ==========================================
# RESUMEN DEL MÓDULO 11
# ==========================================
"""
Conceptos aprendidos:
✓ Qué es IA y diferencia con ML/DL
✓ Clasificación básica
✓ IA Generativa y sus aplicaciones
✓ Herramientas para Python

Siguiente paso:
- Explorar más en: scikit-learn, TensorFlow
- Practicar con datasets de Kaggle
- Experimentar con APIs de OpenAI/Claude
"""

# Fin del Módulo 11