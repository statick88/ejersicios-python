import json

configuracion = {
    "app": "Mi Aplicacion",
    "version": "2.0",
    "debug": True,
    "puerto": 8080,
}

# Guardar directamente en un archivo
with open("/Users/statick/dev/apps/ejersicios-python/Archivos/json/config.json", "w") as archivo:
    json.dump(configuracion, archivo, indent=4)
    print("Configuración guardada en config.json")