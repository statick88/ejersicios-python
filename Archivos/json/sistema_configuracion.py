import json
import os

CONFIG_FILE = "app_config.json"

# Configuración por defecto
CONFIG_DEFAULT = {
    "app_name": "Mi App",
    "version": "1.0.0",
    "theme": "dark",
    "language": "es",
    "notifications": True,
}

def cargar_configuracion():
    """Carga la configuración desde un archivo JSON."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                print("✅ Configuración cargada desde archivo")
                return config
        except json.JSONDecodeError:
            print("⚠️ Archivo corrupto, usando configuración por defecto")
    
    print("📝 Creando configuración por defecto")
    return CONFIG_DEFAULT.copy()

def guardar_configuracion(config):
    """Guarda la configuración actual en un archivo JSON."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
    print("✅ Configuración guardada")

# Uso del sistema
config = cargar_configuracion()
config["theme"] = "light"  # Cambiar configuración
config["language"] = "en"  # Cambiar idioma
guardar_configuracion(config)