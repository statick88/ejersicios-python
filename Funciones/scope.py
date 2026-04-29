# Variable global: todos los apartamentos la ven
edificio = "Torre Python"

def apartamento_3a():
    # Variable local: solo este apartamento la ve
    mueble = "Sofá rojo"
    print(f"En el {edificio} hay un {mueble}")

def apartamento_5b():
    mueble = "Sofá azul"
    print(f"En el {edificio} hay un {mueble}")

apartamento_3a()  # En el Torre Python hay un Sofá rojo
apartamento_5b()  # En el Torre Python hay un Sofá azul
# print(mueble)  # ❌ NameError: ¿cuál mueble? ¿el rojo o el azul?