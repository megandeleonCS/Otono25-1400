# test_cliente_banco.py
# Archivo de pruebas para la clase Cliente.

import pytest

try:
    from m11_usuario_ej3 import Cliente, CuentaBancaria
except ImportError:
    pytest.fail(
        "No se pudo importar la clase 'Cliente' o 'CuentaBancaria' del archivo 'student_code_m12_ex3.py'.")


def test_cliente_inicializacion():
    """Verifica que el cliente y su cuenta se inicializan correctamente."""
    cliente = Cliente("Carlos", 100)
    assert cliente.nombre == "Carlos"
    # Comprueba que el atributo `cuenta` es una instancia de CuentaBancaria
    assert isinstance(cliente.cuenta, CuentaBancaria)
    # Comprueba que la cuenta interna tiene los datos correctos
    assert cliente.cuenta.titular == "Carlos"
    assert cliente.cuenta.saldo == 100


def test_deposito_cliente():
    """Prueba que el depósito a través del cliente funciona."""
    cliente = Cliente("Ana", 200)
    cliente.hacer_deposito(50)
    assert cliente.ver_saldo() == 250


def test_retiro_cliente():
    """Prueba que el retiro a través del cliente funciona."""
    cliente = Cliente("Pedro", 300)
    cliente.hacer_retiro(100)
    assert cliente.ver_saldo() == 200


def test_operaciones_multiples_cliente():
    """Prueba una secuencia de operaciones a través del cliente."""
    cliente = Cliente("Luisa", 1000)
    cliente.hacer_deposito(500)  # Saldo: 1500
    cliente.hacer_retiro(200)  # Saldo: 1300
    assert cliente.ver_saldo() == 1300


def test_dos_clientes_independientes():
    """Verifica que dos clientes tienen cuentas separadas e independientes."""
    cliente1 = Cliente("Jorge", 500)
    cliente2 = Cliente("Sofia", 1000)

    cliente1.hacer_deposito(100)  # Saldo Jorge: 600
    cliente2.hacer_retiro(200)   # Saldo Sofia: 800

    assert cliente1.ver_saldo() == 600
    assert cliente2.ver_saldo() == 800


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de clases y objetos.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
