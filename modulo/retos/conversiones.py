"""
Crea un módulo llamado conversiones.py que contenga:

Una función celsius_a_fahrenheit(celsius) que convierta grados Celsius a Fahrenheit
Una función fahrenheit_a_celsius(fahrenheit) que convierta grados Fahrenheit a Celsius
Una función kilometros_a_millas(km) que convierta kilómetros a millas
Una función millas_a_kilometros(millas) que convierta millas a kilómetros
Un bloque if __name__ == "__main__" que pruebe todas las funciones


Formulas
Fahrenheit = Celsius × 9/5 + 32
Celsius = (Fahrenheit - 32) × 5/9
1 kilómetro = 0.621371 millas
1 milla = 1.60934 kilómetros
"""

def celsius_a_fahrenheit(celsius):
    """convierta grados Celsius a Fahrenheit"""
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    """convierta grados Fahrenheit a Celsius"""
    return (fahrenheit - 32) * 5/9

def kilometros_a_millas(km):
    """convierta kilómetros a millas"""
    return  1 * km * 0.621371 

def millas_a_kilometros(millas):
    """convierta millas a kilómetros"""
    return  1 * millas * 1.60934
