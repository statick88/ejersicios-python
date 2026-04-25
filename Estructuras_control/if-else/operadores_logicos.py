# Sistema de acceso a una película
edad = 16
tiene_permiso = True

# Con 'and': AMBAS condiciones deben cumplirse
if edad >= 18 and tiene_permiso:
    print("Puedes entrar")
else:
    print("No puedes entrar")

# Con 'or': BASTA con que una se cumpla
es_vip = False
if edad >= 18 or es_vip:
    print("Puedes entrar")

# Con 'not': invertir la lógica
esta_prohibido = False
if not esta_prohibido:
    print("La entrada está permitida")