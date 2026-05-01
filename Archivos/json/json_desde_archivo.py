import json

with open("/Users/statick/dev/apps/ejersicios-python/Archivos/json/config.json", "r") as archivo:
    configuracion = json.load(archivo)
    print(f"App: {configuracion['app']}")
    print(f"Versión: {configuracion['version']}")
    print(f"Puerto: {configuracion['puerto']}")