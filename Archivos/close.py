# ❌ Peligroso: si hay un error entre open() y close(), el archivo queda abierto
archivo = open("datos.txt", "w")
contenido = archivo.read()
# Imagina que aquí hay un error...
resultado = int("no es un numero")  # ValueError!
archivo.close()