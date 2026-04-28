# ❌ SyntaxError: el if de filtro va DESPUÉS del for
#cuadrados = [i ** 2 if i % 2 == 0 for i in range(10)]
#print(cuadrados)

# ✅ Correcto: el filtro va al final
cuadrados_pares = [i ** 2 for i in range(10) if i % 2 == 0]
print(cuadrados_pares)
# ✅ Pero si es if/else (ternario), va ANTES del for
cuadrados_o_cero = [i ** 2 if i % 2 == 0 else 0 for i in range(10)]
print(cuadrados_o_cero)