import json

# Datos en Python
configuracion = {
    "app": "Mi Aplicación",
    "version": "2.0",
    "debug": True,
    "puerto": 8080,
    "base_datos": {
        "host": "localhost",
        "nombre": "mi_db",
    },
}

# Convertir diccionario a cadena JSON
json_texto = json.dumps(configuracion)
print(json_texto)

# JSON formateado con indentación
json_bonito = json.dumps(configuracion, indent=4)
print(json_bonito)