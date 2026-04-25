"""
Desafío 1: Calculadora de propinas
Situación
Estás cenando en un restaurante con amigos. La cuenta llega y necesitan calcular cuánto debe pagar 
cada uno, incluyendo la propina.
"""
"""
Pista
1. Convierte la entrada del usuario a float para la cuenta y a int para las personas
2. Calcula la propina: total * (porcentaje / 100)
3. Usa round(valor, 2) para redondear a 2 decimales
4. Usa f-strings con :.2f para formatear los montos
"""
"""
Tu misión
Crea un programa que:

-Pida el total de la cuenta
-Pregunte el porcentaje de propina deseado (10%, 15%, 20%)
-Pregunte entre cuántas personas se divide

Calcule y muestre:
- Monto de la propina
- Total con propina
- Cuánto paga cada persona
"""


#Ejemplo de ejecución
print("=== CALCULADORA DE PROPINAS ===")
#Total de la cuenta: 85.50
total_cuenta = float(input("Total de la cuenta: "))
#Porcentaje de propina (10, 15, 20): 15
porcentaje_propina = int(input("Porcentaje de propina (10, 15, 20): "))
#Número de personas: 3
numero_personas = int(input("Número de personas: "))


#--- Resultado ---

#Propina (15.0%): $12.83
propina = total_cuenta * (porcentaje_propina / 100)
print(propina)  # 12.825
print(f"Propina ({porcentaje_propina:.1f}%): ${propina:.2f}") 
#Total con propina: $98.33
total_con_propina = total_cuenta + propina
print(f"Total con propina: ${total_con_propina:.2f}")
#Cada persona paga: $32.78
pago_por_persona = total_con_propina / numero_personas
print(f"Cada persona paga: ${pago_por_persona:.2f}")


