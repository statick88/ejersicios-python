# ❌ No puedes usar múltiples líneas
# lambda x:
#     resultado = x * 2
#     return resultado  # SyntaxError

# ❌ No puedes usar declaraciones (if/for/while como bloque)
# lambda x: if x > 0: return x  # SyntaxError

# ✅ Pero puedes usar expresiones condicionales
absoluto = lambda x: x if x >= 0 else -x
print(absoluto(-5))  # 5
print(absoluto(3))   # 3