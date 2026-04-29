contador = 0  # Global

def incrementar():
    # ❌ Esto da error: Python piensa que 'contador' es local
    # porque hay una asignación (contador += 1)
    #contador += 1  # UnboundLocalError

    # ✅ Con 'global', le dices a Python que uses la variable global
    global contador
    contador += 1

incrementar()
print(contador)  # 1
incrementar()
print(contador)  # 2