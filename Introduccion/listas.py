# Listas
lista = [1, 2, 3, 4, 5]
print(lista)
lista[4]= 10
print(lista)
lista.append(20)
print(lista) # La lista original se ha modificado y ahora contiene el nuevo elemento
lista.pop() # Elimina el último elemento de la lista
print(lista) # La lista original se ha modificado y el último elemento ha sido eliminado
lista.pop(0) # Elimina el primer elemento de la lista
print(lista) # La lista original se ha modificado y el primer elemento ha sido eliminado
lista2 = lista.copy() # Crea una copia de la lista original
print(lista2) # La nueva lista contiene los mismos elementos que la lista original
lista2.remove(3) # Elimina el elemento '3' de la nueva lista
print(lista2) # La nueva lista se ha modificado y el elemento '3' ha sido eliminado
print(lista) # La lista original no se ha modificado y sigue conteniendo el