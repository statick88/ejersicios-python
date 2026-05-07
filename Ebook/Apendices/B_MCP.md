# Apéndice B: Model Context Protocol (MCP)

---

## B.1 ¿Qué es MCP?

**Model Context Protocol (MCP)** es un estándar que permite conectar agentes IA con herramientas externas de forma estructurada.

```
Agente IA ←→ MCP ←→ Herramientas (DB, Files, HTTP, etc.)
```

---

## B.2 Arquitectura MCP

### Componentes

| Componente | Descripción |
|-----------|-------------|
| **Host** | Aplicación que ejecuta el agente (OpenCode) |
| **Client** | Conexión al servidor MCP |
| **Server** | Proveedor de herramientas |
| **Tools** | Funciones que el agente puede llamar |

### Tipos de MCP

| Tipo | Función | Ejemplo |
|------|--------|--------|
| **Database** | Consultas SQL | SQLite, PostgreSQL |
| **FileSystem** | Lectura/escritura | Archivos locales |
| **HTTP** | Requests HTTP | APIs externas |
| **Playwright** | Automatización browser | E2E testing |
| **Git** | Version control | Operaciones Git |
| **Brave Search** | Búsqueda web | Investigación |

---

## B.3 MCP de Base de Datos

### Conexión SQLite

```python
from mcp import DatabaseMCPServer

# Crear servidor
db_server = DatabaseMCPServer("mi_db.db")

# Herramientas disponibles
server.add_tool("consultar_estudiantes", db_server.query)
server.add_tool("registrar_estudiante", db_server.execute)
```

### Query desde el Agente

```
Usuario: "¿Cuántos estudiantes hay en el curso?"
Agente: [_llama herramienta consultar_estudiantes_]
→ SELECT COUNT(*) FROM estudiantes
→ Resultado: 25 estudiantes
```

---

## B.4 MCP de Sistema de Archivos

```python
from mcp import FileSystemMCPServer

# Server para operaciones de archivo
fs_server = FileSystemMCPServer("./proyecto")

server.add_tool("leer_archivo", fs_server.read)
server.add_tool("escribir_archivo", fs_server.write)
server.add_tool("buscar", fs_server.search)
```

---

## B.5 MCP de Búsqueda Web

```python
from mcp import BraveSearchMCPServer

search_server = BraveSearchMCPServer(api_key="TU_API_KEY")

server.add_tool("buscar", search_server.search)

# Uso: "Buscar información sobre Python 3.12"
```

---

## B.6 Configurar MCP en OpenCode

### En AGENTS.md

```markdown
## MCP Configuration

### base-de-datos
- type: database
- connection: sqlite:./abacom.db
- tools:
  - query
  - execute
  - transaction

### filesystem
- type: filesystem
- path: ./proyecto
- permissions:
  - read: ["*.py", "*.md"]
  - write: [".py"]

### brave-search
- type: search
- api_key: env.BRAVE_API_KEY
```

---

## B.7 Ejemplo: Agente con MCP

```python
# El agente puede usar tools directamente
resultado = db.query("SELECT * FROM estudiantes WHERE programa = ?", ("Python",))
contenido = fs.read("README.md")
busqueda = search.search("mejores prácticas Python 2026")
```

---

## B.8 MCPs Disponibles por Rol

| Rol | MCPs Recomendados |
|-----|-----------------|
| **developer** | Database, FileSystem, Git |
| **qa** | Database, FileSystem, Playwright |
| **security** | Database, HTTP |
| **researcher** | Brave Search, Notion |

---

*Desarrollo Python 2026*
*Licencia Creative Commons CC BY-NC-SA 4.0*