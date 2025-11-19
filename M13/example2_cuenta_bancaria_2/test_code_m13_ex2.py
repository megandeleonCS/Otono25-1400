# test_copias_cliente.py
# Archivo de pruebas para los métodos de copia de la clase Cliente.

import pytest

try:
    # TODO: cambia 'solution_m13_ex2' por 'student_code_m13_ex2' si estás usando el código del estudiante.
    # from solution_m13_ex2 import Cliente
    # Descomenta esta línea si estás usando el código del estudiante.
    from student_code_m13_ex2 import Cliente
except ImportError:
    pytest.fail(
        "No se pudo importar la clase 'Cliente' del archivo 'student_code_m13_ex2.py'.")


@pytest.fixture
def cliente_base():
    """Crea un cliente base para usar en las pruebas."""
    return Cliente("Juan", 500)


def test_copia_superficial_comparte_referencia_interna(cliente_base):
    """
    Verifica que la copia superficial comparte el objeto interno (la cuenta).
    """
    copia = cliente_base.copia_superficial()

    # Los objetos Cliente son diferentes
    assert copia is not cliente_base

    # Pero los objetos CuentaBancaria internos son el mismo
    assert copia.cuenta is cliente_base.cuenta


def test_efecto_secundario_copia_superficial(cliente_base):
    """
    Verifica que modificar la cuenta de la copia superficial afecta al original.
    """
    copia = cliente_base.copia_superficial()
    copia.cuenta.depositar(100)

    # El saldo del original también debe haber cambiado
    assert cliente_base.cuenta.consultar_saldo() == 600


def test_copia_profunda_no_comparte_referencia_interna(cliente_base):
    """
    Verifica que la copia profunda NO comparte el objeto interno.
    """
    copia = cliente_base.copia_profunda()

    # Los objetos Cliente son diferentes
    assert copia is not cliente_base

    # Y los objetos CuentaBancaria internos también son diferentes
    assert copia.cuenta is not cliente_base.cuenta


def test_sin_efecto_secundario_copia_profunda(cliente_base):
    """
    Verifica que modificar la cuenta de la copia profunda NO afecta al original.
    """
    copia = cliente_base.copia_profunda()
    copia.cuenta.depositar(200)

    # El saldo del original no debe haber cambiado
    assert cliente_base.cuenta.consultar_saldo() == 500
    # El saldo de la copia sí debe haber cambiado
    assert copia.cuenta.consultar_saldo() == 700


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de copias de objetos.")
    # If the tests fail, print an error message
    else:
        print("❌ Fallaron algunas pruebas. Revisa los errores para solucionarlos.")
# These are recently edited files. Do not suggest code that has been deleted.
