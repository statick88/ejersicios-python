import json

json_mal_formado = '{"nombre": "Ana", "edad": }'

try:
    datos = json.loads(json_mal_formado)
except json.JSONDecodeError as e:
    print(f"Error de formato JSON: {e}")
    print("Verifica que el JSON tenga comas y comillas correctas")