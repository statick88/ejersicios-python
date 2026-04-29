"""
Desafío 4: Contador de vocales
Situación
Un profesor de lingüística necesita una herramienta que cuente las vocales en cualquier texto para analizar patrones fonéticos en sus investigaciones.

Tu misión
Crea una función llamada contar_vocales que:


Ejemplo de ejecución
PYTHON
resultado = contar_vocales("Hola Mundo, ¿cómo estás?")
print(resultado)

{
    'a': 2,
    'e': 1,
    'i': 0,
    'o': 4,
    'u': 1,
    'total': 8
}
Pista
- Convierte el texto a minúsculas con .lower()
- Puedes usar un diccionario para llevar el conteo
- Itera sobre cada carácter del texto
- Verifica si el carácter está en "aeiou"

Criterios de éxito
- La función se llama contar_vocales
- No distingue entre mayúsculas y minúsculas
- Devuelve un diccionario con cada vocal y el total
- Funciona con textos vacíos (devuelve todo en 0)
"""



#Crea una función llamada contar_vocales que:
def contar_vocales(texto):
    #Convierte el texto a minúsculas con .lower()
    texto = texto.lower()
    #Puedes usar un diccionario para llevar el conteo
    conteo = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'á': 0, 'é': 0, 'í': 0, 'ó': 0, 'ú': 0, 'total': 0}
    #Itera sobre cada carácter del texto
    for char in texto:
        #Verifica si el carácter está en "aeiou"
        if char in conteo:
            conteo[char] += 1
            conteo['total'] += 1
    return conteo

# Reciba un texto como parámetro
texto1 = "Hola Mundo, ¿cómo estás?"
# Cuente cuántas vocales (a, e, i, o, u) hay en el texto
resultado1 = contar_vocales(texto1)
# Debe funcionar sin importar mayúsculas o minúsculas
texto2 = "PYTHON es GENIAL"
resultado2 = contar_vocales(texto2)
# Devuelva un diccionario con el conteo de cada vocal y el total
print(resultado1)
print(resultado2) 
#Cuente cuántas vocales (a, e, i, o, u) hay en el texto
#Debe funcionar sin importar mayúsculas o minúsculas
#Devuelva un diccionario con el conteo de cada vocal y el total