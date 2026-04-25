# ❌ Error común: esperar que range(5) incluya el 5
"""for i in range(5):
    print(i)  # Imprime 0, 1, 2, 3, 4 — NO imprime 5"""

# ✅ Si necesitas incluir el 5, usa range(6)
for i in range(6):
    print(i)  # Imprime 0, 1, 2, 3, 4, 5