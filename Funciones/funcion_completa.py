def funcion_completa(obligatorio, opcional="default", *args, **kwargs):
    print(f"Obligatorio: {obligatorio}")
    print(f"Opcional: {opcional}")
    print(f"Args extra: {args}")
    print(f"Kwargs extra: {kwargs}")

funcion_completa("hola", "mundo", 1, 2, 3, clave="valor")
funcion_completa("solo obligatorio")
funcion_completa("obligatorio", clave1="valor1", clave2="valor2")