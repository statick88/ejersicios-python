# ❌ Demasiado compleja para una sola línea
#resultado = [x * 2 if x > 5 else x * 3 for x in range(20) if x % 2 == 0 if x != 10]
#print(resultado)

"""
# ✅ Mejor como bucle tradicional — más legible
resultado = []
for x in range(20):
    if x % 2 == 0 and x != 10:
        if x > 5:
            resultado.append(x * 2)
        else:
            resultado.append(x * 3)
print(resultado)

"""
# ❌ Con efectos secundarios (no solo crea una lista)
#[print(i) for i in range(10)]  # Usa print() dentro — no es su propósito

# ✅ Bucle tradicional para efectos secundarios
for i in range(10):
    print(i)
