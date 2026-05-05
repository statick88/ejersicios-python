

"""
=== Módulo de Conversiones ===

100°C = 212.0°F
32°F = 0.0°C
10 km = 6.21 millas
5 millas = 8.05 km
"""

"""
Pista
Cada función debe recibir un parámetro numérico y devolver el resultado
El bloque if __name__ == "__main__" solo se ejecuta cuando corres python conversiones.py directamente
Usa f-strings para formatear la salida con 2 decimales: {valor:.2f}
"""

"""
Criterios de éxito
Las 4 funciones están definidas correctamente
Cada función tiene un docstring que explica qué hace
El bloque if __name__ == "__main__" prueba las funciones
Los resultados son numéricamente correctos
El archivo puede ser importado sin ejecutar las pruebas
"""

#from conversiones import celsius_a_fahrenheit, fahrenheit_a_celsius, kilometros_a_millas, millas_a_kilometros
import conversiones
while True:
    print("=== Módulo de Conversiones ===")

    print("Elije una opcion del 1 al 4")
    print("1: Celcius a Farenheit")
    print("2: Fahrenheit a Celsius")
    print("3: Kilometros a Millas")
    print("4: Millas a Kilometros")


    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        valor = float(input("Ingrese los grados en Celcius: "))
        resultado = celsius_a_fahrenheit(valor)
        print(f"El valor en Farenheit es:  {resultado}")
        break
    else:
        print("Ingrese un valor valido")

    if opcion == 2:
        valor = float(input("Ingrese los grados en Farenheit: "))
        resultado = fahrenheit_a_celsius(valor)
        print(f"El valor en Celcius es: {resultado}")
        break
    else:
        print("Ingrese un valor valido")

    if opcion == 3:
        valor = float(input("Ingrese un valor en Kilometros: "))
        resultado = kilometros_a_millas(valor)
        print(f"El valor en millas es: {resultado}")
        break
    else:
        print("Ingrese un valor valido")

    if opcion == 4:
        valor = float(input("Ingrese un valor en Millas: "))
        resultado = millas_a_kilometros(valor)
        print(f"El valor en kilometros es: {resultado}")
        break
    else:
        print("Ingrese un valor valido")


if __name__ == "__main__":
    print()