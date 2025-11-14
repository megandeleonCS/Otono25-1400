# test_cuenta_bancaria.py
# Archivo de pruebas para la clase CuentaBancaria.

import pytest

try:
    from m11_cuenta_ej2 import CuentaBancaria  # Descomenta
except ImportError:
    pytest.fail(
        "No se pudo importar la clase 'CuentaBancaria' del archivo 'student_code_m12_ex2.py'.")


def test_inicializacion():
    """Verifica que la cuenta se inicializa con los valores correctos."""
    cuenta = CuentaBancaria("Ana", 500)
    assert cuenta.titular == "Ana"
    assert cuenta.saldo == 500


def test_inicializacion_saldo_defecto():
    """Verifica que el saldo por defecto es 0 si no se especifica."""
    cuenta = CuentaBancaria("Pedro")
    assert cuenta.saldo == 0


def test_deposito():
    """Prueba el método de depósito."""
    cuenta = CuentaBancaria("Luisa", 100)
    cuenta.depositar(50)
    assert cuenta.consultar_saldo() == 150


def test_retiro_exitoso():
    """Prueba un retiro exitoso."""
    cuenta = CuentaBancaria("Carlos", 200)
    cuenta.retirar(50)
    assert cuenta.consultar_saldo() == 150


def test_retiro_fondos_insuficientes():
    """Prueba un intento de retiro sin fondos suficientes. El saldo no debe cambiar."""
    cuenta = CuentaBancaria("Marta", 100)
    cuenta.retirar(150)
    assert cuenta.consultar_saldo() == 100


def test_operaciones_multiples():
    """Prueba una secuencia de depósitos y retiros."""
    cuenta = CuentaBancaria("Jorge", 1000)
    cuenta.depositar(200)  # Saldo: 1200
    cuenta.retirar(500)   # Saldo: 700
    cuenta.depositar(300)  # Saldo: 1000
    cuenta.retirar(1000)  # Saldo: 0
    assert cuenta.consultar_saldo() == 0


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de clases y objetos.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
# This module is not meant to be run directly. Use pytest to run the tests.
