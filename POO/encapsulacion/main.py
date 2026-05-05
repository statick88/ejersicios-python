from transacciones import CuentaBancaria
    
# Ejemplo de uso
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500)  # Depósito exitoso. Nuevo saldo: 1500
cuenta.retirar(200)    # Retiro exitoso. Nuevo saldo: 1300
print(f"Saldo actual: {cuenta.obtener_saldo()}")  # Saldo actual: 1300
# Intentando acceder a un atributo privado (esto no es recomendable)
try:
    print(cuenta.__saldo)  # Esto generará un error porque __saldo es privado
except AttributeError as e:
    print("Error al acceder a atributo privado:", e)
print(cuenta._CuentaBancaria__conocer_garantias())  # Acceso al método privado (no recomendado)