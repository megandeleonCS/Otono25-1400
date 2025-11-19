# --------------------------------------------------------------------------
#          COPIAS SUPERFICIALES Y PROFUNDAS DE OBJETOS
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es entender la diferencia entre una copia superficial y una
# profunda al trabajar con objetos que contienen otros objetos (composición).
# Modificaremos la clase `Cliente` para que pueda crear copias de sí misma.
#
# Instrucciones para el estudiante:
# 1. Importa el módulo `copy`.
# 2. La clase `Cliente` ahora tiene dos nuevos métodos: `copia_superficial`
#    y `copia_profunda`.
# 3. En `copia_superficial`, usa `copy.copy(self)` para crear y devolver
#    una copia superficial del cliente.
# 4. En `copia_profunda`, usa `copy.deepcopy(self)` para crear y devolver
#    una copia profunda.
# 5. Analiza el bloque de prueba para ver cómo un cambio en la cuenta
#    bancaria de una copia superficial afecta al original, mientras que
#    en una copia profunda no lo hace.
# --------------------------------------------------------------------------

# TODO: Paso 1. Importa el módulo `copy`.
import copy


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def consultar_saldo(self):
        return self.saldo


class Cliente:
    def __init__(self, nombre, saldo_inicial_cuenta=0):
        self.nombre = nombre
        self.cuenta = CuentaBancaria(nombre, saldo_inicial_cuenta)

    # TODO: Paso 2. Implementa el método de copia superficial.
    def copia_superficial(self):
        """Devuelve una copia superficial del cliente."""
        return copy.copy(self)
        

    # TODO: Paso 3. Implementa el método de copia profunda.
    def copia_profunda(self):
        """Devuelve una copia profunda del cliente."""
        return copy.deepcopy(self)
        


# --- Bloque para probar tu clase ---
if __name__ == "__main__":
    cliente_original = Cliente("Ana", 1000)

    print("--- Probando Copia Superficial ---")
    cliente_superficial = cliente_original.copia_superficial()
    # Modificamos la cuenta de la copia
    cliente_superficial.cuenta.depositar(500)

    print(
        f"Saldo del original después de modificar la copia superficial: {cliente_original.cuenta.consultar_saldo()}")
    print("Observa: ¡El saldo del original cambió! Ambos clientes comparten la misma cuenta.")

    print("\n--- Probando Copia Profunda ---")
    cliente_profundo = cliente_original.copia_profunda()
    # Modificamos la cuenta de la copia profunda
    cliente_profundo.cuenta.depositar(1000)

    print(
        f"Saldo del original después de modificar la copia profunda: {cliente_original.cuenta.consultar_saldo()}")
    print("Observa: El saldo del original no cambió. La copia profunda tiene su propia cuenta.")
