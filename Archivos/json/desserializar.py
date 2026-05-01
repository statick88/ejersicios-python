import json

# JSON como cadena de texto
datos_json = '''
{
    "nombre": "Carlos",
    "edad": 35,
    "activo": true,
    "hobbies": ["fútbol", "música"]
}
'''

# Convertir JSON a diccionario de Python
datos = json.loads(datos_json)
print(type(datos))
print(datos["nombre"])
print(datos["hobbies"][0])