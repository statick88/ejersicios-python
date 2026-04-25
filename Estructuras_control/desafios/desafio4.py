"""
Desafío 4: Adivina el número
Situación
Vas a crear un juego clásico: la computadora piensa un número aleatorio y el jugador debe 
adivinarlo recibiendo pistas de “más alto” o “más bajo”.

Tu misión
Crea un programa que:

=== ADIVINA EL NÚMERO ===

¡He pensado un número entre 1 y 100!

Intento 1: 50
📉 Más bajo...

Intento 2: 25
📈 Más alto...

Intento 3: 37
🎉 ¡Correcto! El número era 37
Lo lograste en 3 intentos

"""

# Genere un número aleatorio entre 1 y 100
# Usa import random y random.randint(1, 100) para generar el número
import random
numero_secreto = random.randint(1, 100)
# Usa un while True para el bucle principal
intentos = 0
while True:
    # Permita al jugador ingresar su adivinanza usando input()
    adivinanza = int(input("Introduce tu adivinanza: "))
    
    # Compara la adivinanza con el número secreto para dar pistas
    if adivinanza < numero_secreto:
    #Dé pistas: “Más alto” o “Más bajo” después de cada intento
        print("📈 Más alto...")
    elif adivinanza > numero_secreto:
        print("📉 Más bajo...")
    else:  
        print(f"🎉 ¡Correcto! El número era {numero_secreto}")

        break  # Termina el juego cuando se adivina correctamente
        #Permita al jugador intentar adivinarlo

    #Incrementa un contador de intentos en cada iteración
    intentos += 1
    #Cuente cuántos intentos necesitó el jugador para adivinar el número
print(f"Lo lograste en {intentos} intentos")

#Ejemplo de ejecución