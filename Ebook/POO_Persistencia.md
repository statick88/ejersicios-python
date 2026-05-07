# Ebook Desarrollo Python 2026

## Módulo V: Arquitectura Orientada a Objetos (POO)

---

### Objetivo

Al finalizar este capítulo, el estudiante comprenderá la POO desde la perspectiva de diseño de contratos de software, aplicará el patrón Singleton para recursos únicos, y modelará entidades del mundo real usando clases en Python 3.12+.

> **La forma de programar en 2026**: El desarrollador no es quien escribe cada línea de código, sino el **director de orquesta** que especifica qué debe hacerse y valida que el resultado coincida con la especificación. La IA ejecuta; el humano valida.

---

### 5.1 La Clase como Contrato de Software

#### Concepto

En POO tradicional, una clase se define como una plantilla para crear objetos. En **Spec-Driven Development (SDD)**, una clase es un **contrato** entre:

- **Lo que la clase PROMITE hacer** (métodos públicos)
- **Lo que la clase REQUIERE para hacerlo** (parámetros, dependencias)
- **Las GARANTÍAS que ofrece** (invariantes, retornos tipados)

#### Ejemplo Aplicado: Sistema 

```python
# spec:estudiante-contrato.md
"""
## HU-001: Registro de Estudiante

Como sistema , necesito que un estudiante pueda:
- Registrarse con datos válidos
- Consultar su información
- Actualizar su estado

Criterios de aceptación:
- Nombre no puede estar vacío
- Email debe ser único en el sistema
- Retorna información estructurada
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import re

class Estudiante:
    """
    Contrato: Define el comportamiento de un estudiante en .
    
    Responsibilities (SRP):
    - Validar datos de entrada
    - Almacenar estado del estudiante
    - Proporcionar información consultable
    
    Guarantees:
    - Email siempre en minúsculas
    - Fecha de registro inmutable
    """
    
    # Estado interno (estado del objeto)
    _registry: dict[str, "Estudiante"] = {}  # Singleton simulado
    
    def __init__(
        self, 
        nombre: str, 
        email: str, 
        programa: str = "Desarrollo Python"
    ) -> None:
        # Precondición: validación de contrato
        if not nombre or len(nombre.strip()) == 0:
            raise ValueError("Nombre no puede estar vacío")
        if not self._validar_email(email):
            raise ValueError(f"Email inválido: {email}")
        
        # Inicialización de estado
        self._id: str = email.lower()
        self._nombre: str = nombre.strip()
        self._email: str = email.lower()
        self._programa: str = programa
        self._fecha_registro: datetime = field(default_factory=datetime.now)
        self._estado: str = "activo"
        
        # Registro en singleton
        self._registry[self._id] = self
    
    @staticmethod
    def _validar_email(email: str) -> bool:
        """Valida formato de email usando regex"""
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(patron, email))
    
    @property
    def id(self) -> str:
        """Garantía: retorna identificador único"""
        return self._id
    
    @property
    def nombre(self) -> str:
        """Garantía: retorna nombre formateado"""
        return self._nombre.title()
    
    def a_diccionario(self) -> dict:
        """Garantía: retorna información estructurada"""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "email": self._email,
            "programa": self._programa,
            "fecha_registro": self._fecha_registro.isoformat(),
            "estado": self._estado
        }
    
    def __repr__(self) -> str:
        return f"Estudiante({self._email})"
```

#### Criterios de Aceptación

| Criterio | Verificación |
|---------|-------------|
| Nombre vacío lanza excepción | `Estudiante("", "test@abacom.com")` → `ValueError` |
| Email inválido rechazado | `Estudiante("Juan", "no-valido")` → `ValueError` |
| Email único en sistema | Dos instancias mismo email → misma referencia |
| Retorna diccionario | `est.a_diccionario()` → `dict` con 6 campos |

---

### 5.2 El Patrón Singleton para Recursos Únicos

#### Concepto

El patrón **Singleton** garantiza que una clase tenga **una única instancia** en todo el sistema. Esencial cuando:

- Se necesita un punto central de configuración
- Se managea un recurso compartido (conexión a BD, logger)
- Se quiere evitar duplicación de estado

> **En SDD**: El singleton es un **acuerdo de unicidad** que se documenta en la especificación.

#### Ejemplo: Gestor de Estudiantes 

```python
class GestorEstudiantes:
    """
    Contrato: Gestor único de estudiantes en el sistema.
    
    Guarantees:
    - Solo existe una instancia en todo el proceso
    - Proveé métodos para CRUD de estudiantes
    """
    
    _instancia: Optional["GestorEstudiantes"] = None
    
    def __new__(cls) -> "GestorEstudiantes":
        """Garantía de unicidad"""
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._estudiantes = {}
            cls._instancia._contador = 0
        return cls._instancia
    
    def registrar(self, nombre: str, email: str) -> Estudiante:
        """PROMESA: registra estudiante válido"""
        # Verificar email único globalmente
        email_lower = email.lower()
        if email_lower in self._estudiantes:
            raise ValueError(f"Email {email} ya registrado")
        
        estudiante = Estudiante(nombre, email)
        self._estudiantes[email_lower] = estudiante
        self._contador += 1
        return estudiante
    
    def buscar(self, email: str) -> Optional[Estudiante]:
        """PROMESA: busca por email"""
        return self._estudiantes.get(email.lower())
    
    def listar_todos(self) -> list[Estudiante]:
        """PROMESA: lista todos"""
        return list(self._estudiantes.values())
    
    @property
    def total(self) -> int:
        """Garantía: retorna count"""
        return self._contador


# Uso en aplicación
gestor = GestorEstudiantes()  # Obtiene la instancia única
otro = GestorEstudiantes()

assert gestor is otro  # ✓ Misma referencia
print(f"Total registrados: {gestor.total}")
```

#### Criterios de Aceptación

| Criterio | Verificación |
|---------|-------------|
| Una sola instancia | `g1 is g2` donde `g1, g2 = GestorEstudiantes()` |
| Datos persisted entre llamadas | Registrar → buscar → encuentra |
| Email único globalmente | Segundo registro mismo email → `ValueError` |

---

## Módulo VI: Persistencia de Datos con SQLite y Agentes

---

### Objetivo

Integrar bases de datos relacionales en flujos agénticos, diseñar esquemas desde especificaciones SDD, y resolver la "amnesia" de agentes mediante memoria persistente con Engram.

> **La forma de programar en 2026**: No escribimos SQL a mano. Especificamos qué queremos y dejamos que las herramientas generen el código. El desarrollador **dirige, no ejecuta**.

---

### 6.1 Integración de SQLite en Flujos Agénticos

#### Concepto

Una base de datos relacional en un flujo agéntico cumple tres funciones:

1. **Memoria de trabajo**: Historial de interacciones
2. **Memoria persistente**: Conocimiento que persiste entre sesiones
3. **Coordinación**: Estado compartido entre agentes

#### Ejemplo: Base de Datos para Sistema 

```python
# database/esquema.py
"""
Diseño de esquema desde especificación SDD

## HU-002: Persistencia de Cursos

Criterios de aceptación:
- Cada curso tiene código único
- Cada curso pertenece a un programa
- Cada curso tiene instructor asignado
- Fechas en formato ISO 8601
"""

import sqlite3
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

class GestorBD:
    """Gestor de conexión SQLite para """
    
    def __init__(self, ruta_bd: str = "abacom.db") -> None:
        self.ruta = ruta_bd
        self._crear_esquema()
    
    def _crear_esquema(self) -> None:
        """Crea tablas desde especificación"""
        with sqlite3.connect(self.ruta) as conn:
            cursor = conn.cursor()
            
            # Tabla: programas (padre de cursos)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS programas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo TEXT UNIQUE NOT NULL,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    fecha_creacion TEXT NOT NULL,
                    estado TEXT DEFAULT 'activo'
                )
            """)
            
            # Tabla: cursos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cursos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo TEXT UNIQUE NOT NULL,
                    nombre TEXT NOT NULL,
                    programa_id INTEGER NOT NULL,
                    instructor_id INTEGER,
                    duracion_horas INTEGER DEFAULT 20,
                    fecha_creacion TEXT NOT NULL,
                    estado TEXT DEFAULT 'activo',
                    FOREIGN KEY (programa_id) REFERENCES programas(id),
                    FOREIGN KEY (instructor_id) REFERENCES instructores(id)
                )
            """)
            
            # Tabla: estudiantes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    nombre TEXT NOT NULL,
                    programa_id INTEGER,
                    fecha_registro TEXT NOT NULL,
                    estado TEXT DEFAULT 'activo',
                    FOREIGN KEY (programa_id) REFERENCES programas(id)
                )
            """)
            
            # Tabla: interacciones (memoria agéntica)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS interacciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    agente_id TEXT NOT NULL,
                    estudiante_email TEXT,
                    tipo TEXT NOT NULL,
                    contenido TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    metadata TEXT,
                    FOREIGN KEY (estudiante_email) REFERENCES estudiantes(email)
                )
            """)
            
            conn.commit()
    
    def ejecutar(self, sql: str, params: tuple = ()) -> list:
        """Ejecuta query y retorna resultados"""
        with sqlite3.connect(self.ruta) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(sql, params)
            if sql.strip().upper().startswith("SELECT"):
                return [dict(fila) for fila in cursor.fetchall()]
            conn.commit()
            return []
    
    def insertar_curso(
        self, 
        codigo: str, 
        nombre: str, 
        programa_id: int,
        duracion: int = 20
    ) -> int:
        """Inserta curso y retorna su ID"""
        sql = """
            INSERT INTO cursos (codigo, nombre, programa_id, duracion_horas, fecha_creacion, estado)
            VALUES (?, ?, ?, ?, ?, 'activo')
        """
        with sqlite3.connect(self.ruta) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (codigo, nombre, programa_id, duracion, datetime.now().isoformat()))
            conn.commit()
            return cursor.lastrowid


# Uso
gestor = GestorBD("abacom.db")

# Insertar programa
gestor.ejecutar(
    "INSERT INTO programas (codigo, nombre, descripcion, fecha_creacion) VALUES (?, ?, ?, ?)",
    ("PY2026", "Desarrollo Python 2026", "Curso de Python para ", datetime.now().isoformat())
)

# Insertar curso
gestor.insertar_curso("PY-101", "POO con Python", 1, 30)

# Consultar
cursos = gestor.ejecutar("SELECT * FROM cursos WHERE programa_id = ?", (1,))
print(cursos)
```

#### Criterios de Aceptación

| Criterio | Verificación |
|---------|-------------|
| Tabla programas existe | `SELECT name FROM sqlite_master WHERE type='table'` |
| Curso tiene código único | Insertar duplicado → error SQL |
| Fechas en ISO 8601 | `2026-05-07T14:30:00` |
| FK funciona | Curso sin programa → error |

---

### 6.2 OpenCode: De Especificación a Esquema

#### Concepto

OpenCode permite usar el skill **sdml-spec** para transformar especificaciones markdown en código SQL. El flujo SDD completo:

```
HU → spec .md → [sdml-spec] → esquema .sql → [sdd-apply] → código Python
```

#### Ejemplo: Generación Automática

```markdown
<!-- HU-002: Cursos.md -->
## Historia de Usuario: Gestión de Cursos

### Criterios de Aceptación
- [ ] Código único por curso
- [ ] Nombre de 5-100 caracteres
- [ ] Programa asociado existe
- [ ] Instructor opcional
- [ ] Duración en horas (1-200)
- [ ] Estado: activo/inactivo
```

```bash
# Con OpenCode, generar schéma desde spec
opencode spec-to-sql -i HU-002.md -o esquema.sql -t sqlite
```

#### Criterios de Aceptación

| Criterio | Verificación |
|---------|-------------|
| spec .md parseable | Archivo con formato SDD |
| Esquema genera | CREATE TABLE para cursos |
| FK correctas | programa_id → programas.id |

---

### 6.3 Engram: Memoria Persistente para Agentes

#### El Problema de la Amnesia

Cada vez queinicias una nueva sesión con un agente IA, este **olvida** todo lo que se habló antes. A esto le llamamos la **"amnesia del agente"**.

#### Solución: Engram con SQLite

Engram es el sistema de memoria persistente de OpenCode. Usa SQLite para almacenar:

- **Contexto de sesión**: Lo que se trabaja actualmente
- **Aprendizajes**: Descubrimientos técnicos
- **Decisiones**: Arquitectura y patrones

```python
# guards/engram_memory.py
"""
Sistema de memoria persistente para agentes
Resuelve la "amnesia" entre sesiones
"""

import sqlite3
from datetime import datetime
from typing import Optional
import json

class Engram:
    """Memoria persistente para agentes IA"""
    
    def __init__(self, ruta_bd: str = ".engram/memoria.db") -> None:
        self.ruta = ruta_bd
        self._inicializar()
    
    def _inicializar(self) -> None:
        """Crea estructura de memoria"""
        with sqlite3.connect(self.ruta) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS sesiones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    directorio TEXT NOT NULL,
                    session_id TEXT NOT NULL,
                    inicio TEXT NOT NULL,
                    fin TEXT,
                    resumen TEXT
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS observaciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    titulo TEXT NOT NULL,
                    contenido TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    topic_key TEXT
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS decisiones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT,
                    titulo TEXT NOT NULL,
                   reason TEXT NOT NULL,
                    archivos TEXT,
                    fecha TEXT NOT NULL
                )
            """)
            
            conn.commit()
    
    def guardar_observacion(
        self,
        titulo: str,
        contenido: str,
        tipo: str = "manual",  # decision, architecture, bugfix, pattern, config
        session_id: str = "default"
    ) -> int:
        """Guarda aprendizaje para persistencia"""
        sql = """
            INSERT INTO observaciones (session_id, titulo, contenido, tipo, created_at)
            VALUES (?, ?, ?, ?, ?)
        """
        with sqlite3.connect(self.ruta) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (session_id, titulo, contenido, tipo, datetime.now().isoformat()))
            conn.commit()
            return cursor.lastrowid
    
    def buscar(self, query: str, limit: int = 10) -> list:
        """Busca en memoria"""
        sql = """
            SELECT * FROM observaciones 
            WHERE contenido LIKE ? OR titulo LIKE ?
            ORDER BY created_at DESC
            LIMIT ?
        """
        with sqlite3.connect(self.ruta) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (f"%{query}%", f"%{query}%", limit))
            return [dict(row) for row in cursor.fetchall()]
    
    def cerrar_sesion(self, session_id: str, resumen: str) -> None:
        """Cierra sesión con resumen"""
        sql = "UPDATE sesiones SET fin = ?, resumen = ? WHERE session_id = ?"
        with sqlite3.connect(self.ruta) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (datetime.now().isoformat(), resumen, session_id))
            conn.commit()


# Uso: Persistir aprendizajes
engram = Engram()

# Guardar decisión de arquitectura
engram.guardar_observacion(
    titulo="Usar SQLite para Engram",
    contenido="""**Qué**: Elegimos SQLite sobre archivos JSON para memoria persistente
    **Porqué**: Concurrencia, queries, y robustez probada
    **Dónde**: .engram/memoria.db""",
    tipo="architecture",
    session_id="abacom-2026"
)

# Buscar decisiones pasadas
resultados = engram.buscar("Singleton")
for r in resultados:
    print(f"- {r['titulo']}: {r['contenido'][:100]}...")
```

#### Por qué Engram Resuelve la Amnesia

| Aspecto | Sin Engram | Con Engram |
|--------|-----------|-----------|
| Sesión nueva | Parte de cero | Recuerda decisiones previas |
| Errores repeatidos | Mismo error otra vez | Guarda soluciones |
| Contexto | Se pierde | Persiste entre sesiones |

#### Flujo Completo: Agente con Memoria

```python
# agente_abacom.py
"""
Agente  con memoria persistente
"""

from datetime import datetime

class Agente:
    def __init__(self) -> None:
        self.engram = Engram()
        self.session_id = f"abacom-{datetime.now().strftime('%Y%m%d')}"
        self._iniciar_sesion()
    
    def _iniciar_sesion(self) -> None:
        """Inicia sesión con memoria"""
        # Buscar contexto previo
        prev = self.engram.buscar("", limit=5)
        if prev:
            print(f"📚 Recordando sesiones previas:")
            for p in prev:
                print(f"  - {p['titulo']}")
    
    def trabajar(self, titulo: str, contenido: str) -> None:
        """Trabaja y guarda aprendizajes"""
        # Guardar en memoria
        self.engram.guardar_observacion(
            titulo=titulo,
            contenido=contenido,
            tipo="learning",
            session_id=self.session_id
        )
        print(f"✓ Guardado: {titulo}")
    
    def cerrar(self) -> None:
        """Cierra con resumen"""
        resumen = f"Session {self.session_id} completada"
        self.engram.cerrar_sesion(self.session_id, resumen)
        print(f"✓ Sesión cerrada: {resumen}")


# Uso
agente = Agente()
agente.trabajar(
    "Sistema de login implementado",
    "**Qué**: Login con JWT implementado\n**Porqué**: Escala mejor que sesiones"
)
agente.cerrar()
```

#### Criterios de Aceptación

| Criterio | Verificación |
|---------|-------------|
| Observaciones persisten | Guardar → reiniciar → buscar → encuentra |
| Búsqueda funciona | `buscar("Python")` → resultados relevantes |
| Decisiones categorizadas | Por tipo (architecture, bugfix, etc.) |

---

### Resumen del Módulo

| Tema | Concepto Clave | Herramienta |
|------|---------------|-----------|
| Clase como contrato | POO con garantías | Python classes |
| Singleton | Una sola instancia | `__new__` override |
| SQLite + Agentes | BD relacional | `sqlite3` |
| De spec a schema | SDD automation | OpenCode skills |
| Engram | Memoria persistente | SQLite + `Engram` class |

---

*Desarrollo Python 2026*
*Licencia Creative Commons CC BY-NC-SA 4.0*
*Spec-Driven Development | QA | Security | Design*