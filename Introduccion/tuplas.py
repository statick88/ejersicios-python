# Tuplas
tupla = (1, 2, 3, 4, 5)
print(tupla)

#tupla[4] = 10 # ❌ Error: las tuplas son inmutables y no se pueden modificar
#print(tupla) # La tupla original no se ha modificado y sigue conteniendo
lista = list(tupla) # Convertimos la tupla a una lista para modificarla
print(lista) # La nueva lista contiene los mismos elementos que la tupla original
lista[4] = 10 # Modificamos la lista
print(lista) # La lista se ha modificado y ahora contiene el nuevo elemento
tupla_modificada = tuple(lista) # Convertimos la lista de nuevo a una tupla
print(tupla_modificada) # La nueva tupla contiene los mismos elementos que la lista