# Sistema de registro: acepta números positivos, rechaza negativos, termina con 0
print("=== REGISTRO DE VALORES ===")
print("Números positivos se suman, negativos se ignoran, 0 termina")

total = 0
contador_validos = 0
contador_ignorados = 0

while True:
    entrada = input("Ingresa un número: ")
    
    # Validar que sea un número
    try:
        numero = float(entrada)
    except ValueError:
        print("⚠️ Eso no es un número. Intenta de nuevo.")
        continue
    
    # Verificar señal de parada
    if numero == 0:
        break
    
    # Rechazar negativos
    if numero < 0:
        print(f"⏭️ {numero} ignorado (negativo)")
        contador_ignorados = contador_ignorados + 1
        continue
    
    # Acumular positivos
    total = total + numero
    contador_validos = contador_validos + 1
    print(f"✅ {numero} agregado. Total: {total}")

print(f"\n=== RESUMEN ===")
print(f"Valores válidos: {contador_validos}")
print(f"Valores ignorados: {contador_ignorados}")
print(f"Total acumulado: {total}")