"""
Desafío 3: FizzBuzz clásico
Situación
FizzBuzz es el desafío clásico de entrevistas técnicas. Parece simple, pero revela si entiendes condiciones, bucles y el orden de evaluación.

El orden de las condiciones importa: verifica FizzBuzz primero (múltiplo de 15)
Un número es múltiplo de X si numero % X == 0
Si verificas Fizz y Buzz por separado antes que FizzBuzz, nunca llegarás a FizzBuzz

Tu misión
"""

# Crea un programa que imprima los números del 1 al 50, pero con estas reglas:
for i in range(1, 51):
    #Si el número es múltiplo de 3 Y 5, imprime "FizzBuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
#Si el número es múltiplo de 3, imprime "Fizz"
    elif i % 3 == 0:
        print("Fizz")
#Si el número es múltiplo de 5, imprime "Buzz"
    elif i % 5 == 0:
        print("Buzz")
#En cualquier otro caso, imprime el número
    else:
        print(i)
