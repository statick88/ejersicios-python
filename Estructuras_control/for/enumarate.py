frutas = ["manzana", "banana", "cereza", "dátil"]

"""for indice, fruta in enumerate(frutas):
    print(f"{indice + 1}. {fruta}")"""

    # Empezar el índice desde 1
for posicion, fruta in enumerate(frutas, start=1):
    print(f"{posicion}. {fruta}")