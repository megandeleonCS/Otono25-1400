# --------------------------------------------------------------------------
#          CLASE PARA REPRESENTAR UNA CUENTA BANCARIA
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una clase `CuentaBancaria` que modele una cuenta
# simple. La clase almacenará el nombre del titular y el saldo, y tendrá
# métodos para depositar, retirar y consultar el saldo.
#
# Instrucciones para el estudiante:
# 1. Completa el método `__init__`. Debe aceptar `titular` y un
#    `saldo_inicial` opcional que por defecto será 0.
# 2. Completa el método `depositar`. Debe aceptar una `cantidad` y sumarla
#    al saldo actual.
# 3. Completa el método `retirar`. Debe aceptar una `cantidad` y restarla
#    del saldo, pero solo si hay fondos suficientes. Si no hay fondos,
#    no debe cambiar el saldo y debe devolver un mensaje de error.
# 4. Completa el método `consultar_saldo`, que simplemente debe devolver
#    el saldo actual.
# --------------------------------------------------------------------------

class CuentaBancaria:
    """
    Una clase para simular una cuenta bancaria simple.
    """

    def __init__(self, titular, saldo_inicial=0):
        """
        Inicializa una nueva cuenta bancaria.

        Args:
          titular (str): El nombre del titular de la cuenta.
          saldo_inicial (float, opcional): El saldo con el que empieza la cuenta. Por defecto es 0.
        """
        # TODO: Paso 1. Almacena el titular y el saldo como atributos.
        self.titular = titular  # Asigna aquí el titular.
        self.saldo = saldo_inicial  # Asigna aquí el saldo inicial.

    def depositar(self, cantidad):
        """
        Añade una cantidad al saldo de la cuenta.
        """
        # TODO: Paso 2. Incrementa el saldo con la cantidad depositada.
        # self.saldo += ...
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        """
        Retira una cantidad del saldo, si es posible.
        """
        # TODO: Paso 3. Comprueba si la cantidad a retirar es menor o igual al saldo.
        # if cantidad <= ...:
        # Si hay fondos, resta la cantidad del saldo.
        # self.saldo -= ...
        # print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        # else:
        # Si no hay fondos, imprime un mensaje de error.
        # print("Error: fondos insuficientes.")
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Error: fondos insuficientes.")

    def consultar_saldo(self):
        """
        Devuelve el saldo actual de la cuenta.
        """
        # TODO: Paso 4. Devuelve el atributo de saldo.
        return self.saldo
        


# --- Bloque para probar tu clase ---
if __name__ == "__main__":
    mi_cuenta = CuentaBancaria("Juan Pérez", 1000)

    print(f"Saldo inicial: {mi_cuenta.consultar_saldo()}")

    mi_cuenta.depositar(500)
    mi_cuenta.retirar(200)
    mi_cuenta.retirar(1500)  # Intento de retiro mayor al saldo

    print(f"Saldo final: {mi_cuenta.consultar_saldo()}")
