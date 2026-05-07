# Módulo 10: Proyecto Integrador

---

## Objetivo

Integrar todos los conocimientos adquiridos en un proyecto funcional de gestión usando Python, aplicando metodologías profesionales como SDD.

---

## 10.1 Planificar el Proyecto

### Del Problema a la Solución

Antes de programar, responde:

1. **¿Qué problema resuelvo?**
2. **¿Quién usará el sistema?**
3. **¿Qué funciones necesito?**
4. **¿Cómo almacenaré datos?**

### Estructura Profesional de Proyecto

```
proyecto/
├── src/
│   ├── __init__.py
│   ├── modelos.py          # Clases y estructuras
│   ├── vistas.py           # Interfaz de usuario
│   └── controladores.py    # Lógica de negocio
├── datos/                  # Archivos de datos
├── pruebas/               # Tests
├── docs/                  # Documentación
└── main.py               # Punto de entrada
```

---

## 10.2 Proyecto Guiado: Gestor de Tareas

### Sistema de Gestión de Tareas (To-Do)

**Funcionalidades:**
- Crear tarea
- Listar tareas
- Completar tarea
- Eliminar tarea
- Persistir en archivo JSON

### Paso 1: Modelo (Clase Tarea)

```python
# src/modelos.py

class Tarea:
    """Modelo para representar una tarea"""
    
    def __init__(self, titulo: str, descripcion: str = ""):
        self.id = None  # Se asignará automáticamente
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
    
    def marcar_completada(self):
        self.completada = True
    
    def __dict__(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "completada": self.completada
        }
    
    def __repr__(self):
        estado = "✓" if self.completada else "○"
        return f"{estado} {self.titulo}"
```

### Paso 2: Controlador (Lógica)

```python
# src/controladores.py

import json
from pathlib import Path
from typing import Optional
from src.modelos import Tarea

class GestorTareas:
    """Controlador para gestionar tareas"""
    
    def __init__(self, archivo_datos: str = "datos/tareas.json"):
        self.archivo = Path(archivo_datos)
        self.tareas: list[Tarea] = []
        self.cargar()
    
    def cargar(self):
        """Carga tareas desde archivo"""
        if self.archivo.exists():
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for d in datos:
                    tarea = Tarea(d["titulo"], d["descripcion"])
                    tarea.id = d["id"]
                    tarea.completada = d["completada"]
                    self.tareas.append(tarea)
    
    def guardar(self):
        """Guarda tareas en archivo"""
        self.archivo.parent.mkdir(parents=True, exist_ok=True)
        datos = [t.__dict__() for t in self.tareas]
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
    
    def crear(self, titulo: str, descripcion: str = "") -> Tarea:
        """Crea una nueva tarea"""
        tarea = Tarea(titulo, descripcion)
        tarea.id = len(self.tareas) + 1
        self.tareas.append(tarea)
        self.guardar()
        return tarea
    
    def listar(self) -> list[Tarea]:
        """Lista todas las tareas"""
        return self.tareas
    
    def completar(self, tarea_id: int) -> Optional[Tarea]:
        """Marca tarea como completada"""
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.marcar_completada()
                self.guardar()
                return tarea
        return None
    
    def eliminar(self, tarea_id: int) -> bool:
        """Elimina una tarea"""
        inicial = len(self.tareas)
        self.tareas = [t for t in self.tareas if t.id != tarea_id]
        if len(self.tareas) < inicial:
            self.guardar()
            return True
        return False
```

### Paso 3: Vista (Interfaz CLI)

```python
# src/vistas.py

from src.controladores import GestorTareas

class InterfazTareas:
    """Interfaz de línea de comandos"""
    
    def __init__(self):
        self.gestor = GestorTareas()
    
    def mostrar_menu(self):
        print("""
╔══════════════════════════╗
║   GESTOR DE TAREAS v1.0   ║
╠══════════════════════════╣
║ 1. Crear tarea           ║
║ 2. Listar tareas         ║
║ 3. Completar tarea        ║
║ 4. Eliminar tarea        ║
║ 5. Salir                 ║
╚══════════════════════════╝
""")
    
    def crear_tarea(self):
        titulo = input("Título: ").strip()
        desc = input("Descripción: ").strip()
        tarea = self.gestor.crear(titulo, desc)
        print(f"✓ Tarea creada: {tarea}")
    
    def listar_tareas(self):
        tareas = self.gestor.listar()
        if not tareas:
            print("No hay tareas")
            return
        print("\n--- TAREAS ---")
        for t in tareas:
            print(f"  {t}")
    
    def completar_tarea(self):
        try:
            tarea_id = int(input("ID de tarea: "))
            tarea = self.gestor.completar(tarea_id)
            if tarea:
                print(f"✓ Completada: {tarea}")
            else:
                print("Tarea no encontrada")
        except ValueError:
            print("ID inválido")
    
    def eliminar_tarea(self):
        try:
            tarea_id = int(input("ID de tarea: "))
            if self.gestor.eliminar(tarea_id):
                print("✓ Tarea eliminada")
            else:
                print("Tarea no encontrada")
        except ValueError:
            print("ID inválido")
    
    def ejecutar(self):
        opciones = {
            "1": self.crear_tarea,
            "2": self.listar_tareas,
            "3": self.completar_tarea,
            "4": self.eliminar_tarea
        }
        
        while True:
            self.mostrar_menu()
            opcion = input("Opción: ").strip()
            
            if opcion == "5":
                print("¡Hasta luego!")
                break
            elif opcion in opciones:
                opciones[opcion]()
            else:
                print("Opción inválida")
```

### Paso 4: Punto de Entrada

```python
# main.py

from src.vistas import InterfazTareas

def main():
    interfaz = InterfazTareas()
    interfaz.ejecutar()

if __name__ == "__main__":
    main()
```

---

## 10.3 Proyecto Guiado: Calculadora de Notas

### Calculadora con Persistencia

```python
from dataclasses import dataclass
from typing import Optional
import json

@dataclass
class Estudiante:
    nombre: str
    nota: float

class RegistroNotas:
    def __init__(self, archivo="notas.json"):
        self.archivo = archivo
        self.estudiantes: list[Estudiante] = []
        self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.estudiantes = [Estudiante(d["nombre"], d["nota"]) for d in data]
        except FileNotFoundError:
            pass
    
    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump([{"nombre": e.nombre, "nota": e.nota} for e in self.estudiantes], f, indent=2)
    
    def agregar(self, nombre: str, nota: float):
        self.estudiantes.append(Estudiante(nombre, nota))
        self.guardar()
    
    def promedio(self) -> float:
        if not self.estudiantes:
            return 0
        return sum(e.nota for e in self.estudiantes) / len(self.estudiantes)
    
    def arriba_promedio(self) -> list[str]:
        prom = self.promedio()
        return [e.nombre for e in self.estudiantes if e.nota >= prom]
    
    def mostrar(self):
        print("\n=== REGISTRO DE NOTAS ===")
        for e in self.estudiantes:
            print(f"{e.nombre}: {e.nota:.1f}")
        print(f"\nPromedio: {self.promedio():.1f}")
        print(f"Encima del promedio: {', '.join(self.arriba_promedio())}")

# Uso
registro = RegistroNotas()
registro.agregar("Juan", 8.5)
registro.agregar("María", 9.0)
registro.agregar("Carlos", 7.0)
registro.mostrar()
```

---

## 10.4 Proyecto Guiado: Juego del Ahorcado

```python
import random

class Ahorcado:
    def __init__(self):
        self.palabras = ["PYTHON", "ALGORITMO", "PROGRAMA", "DATOS", "FUNCION"]
        self.palabra = random.choice(self.palabras)
        self.letras_adivinadas = set()
        self.intentos = 6
    
    def mostrar(self):
        resultado = ""
        for letra in self.palabra:
            resultado += letra + " " if letra in self.letras_adivinadas else "_ "
        print(f"\n{resultado.strip()}")
        print(f"Intentos restantes: {self.intentos}")
        print(f"Letras intentadas: {', '.join(sorted(self.letras_adivinadas))}")
    
    def jugar(self):
        while self.intentos > 0:
            self.mostrar()
            letra = input("Letra: ").strip().upper()
            
            if not letra or len(letra) != 1:
                print("Ingresa una letra")
                continue
            
            if letra in self.letras_adivinadas:
                print("Ya laIntentaste")
                continue
            
            self.letras_adivinadas.add(letra)
            
            if letra not in self.palabra:
                self.intentos -= 1
                print(f"✗ No está. Intentos: {self.intentos}")
            
            if all(l in self.letras_adivinadas for l in self.palabra):
                print(f"\n¡Ganaste! La palabra era: {self.palabra}")
                return
        
        print(f"\nPerdiste. La palabra era: {self.palabra}")

# Ejecutar
juego = Ahorcado()
juego.jugar()
```

---

## 10.5 Presentación del Proyecto

### Cómo Presentar

| Aspecto | Qué Mostrar |
|---------|--------------|
| **Funcionalidad** | Demo en vivo |
| **Código** | Partes clave explicadas |
| **Decisiones** | Por qué lo hice así |
| **Lecciones** | Qué aprendí |
| **Próximos pasos** | Mejoras futuras |

### Pitch de 5 minutos

```
1. Problema (30 seg):   "¿Alguna vez olvidaron una tarea..."
2. Solución (1 min):   "Creé este gestor que..."
3. Demo (2 min):       Muestra las 4 funciones
4. Código (1 min):    Explica la claseGestorTareas
5. Cierre (30 seg):    "Esto fue lo que aprendí..."
```

---

## Checklist de Proyecto

- [ ] Proyecto con estructura limpia
- [ ] Programa funcional
- [ ] Datos persisten entre ejecuciones
- [ ] Mínimo CRUD completo
- [ ] Código documentado
- [ ] Tests incluidos (opcional)

---

*Proyecto Integrador - Desarrollo Python 2026*