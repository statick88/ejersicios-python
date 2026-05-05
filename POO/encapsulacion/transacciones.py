"""
Ejemplo basico de encapsulación en Python. La clase 
`CuentaBancaria` tiene atributos privados y 
métodos públicos para acceder a ellos.
"""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad a retirar debe ser positiva y menor o igual al saldo actual.")

    def obtener_saldo(self):
        return self.__saldo
    
    def __conocer_garantias(self):
        return "Garantías disponibles: Seguro de depósito hasta $250,000."