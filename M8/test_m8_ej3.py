# test_ordenar_lista.py
# Archivo de pruebas para la función ordenar_de_mayor_a_menor.

import pytest

try:
    from m8_ordenar_ej3 import ordenar_de_mayor_a_menor
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'ordenar_de_mayor_a_menor' del archivo 'student_code_m9_ex3.py'.")


def test_ordena_correctamente():
    """Prueba que la lista se ordena de mayor a menor."""
    lista = [3, 1, 4, 1, 5, 9, 2]
    ordenar_de_mayor_a_menor(lista)
    assert lista == [9, 5, 4, 3, 2, 1, 1]


def test_con_numeros_negativos():
    """Prueba con una lista que incluye números negativos."""
    lista = [-5, 10, -2, 0, 3]
    ordenar_de_mayor_a_menor(lista)
    assert lista == [10, 3, 0, -2, -5]


def test_lista_ya_ordenada():
    """Prueba con una lista que ya está ordenada de mayor a menor."""
    lista = [10, 8, 6, 4, 2]
    ordenar_de_mayor_a_menor(lista)
    assert lista == [10, 8, 6, 4, 2]


def test_modifica_lista_en_lugar():
    """
    Verifica que la función modifica la lista original en lugar de crear una nueva.
    Compara el 'id' del objeto antes y después de llamar a la función.
    """
    lista = [1, 2, 3]
    id_antes = id(lista)
    ordenar_de_mayor_a_menor(lista)
    id_despues = id(lista)
    assert id_antes == id_despues, "La función debe modificar la lista en el lugar, no crear una nueva."


def test_retorna_none():
    """Verifica que la función no devuelve ningún valor (retorna None)."""
    lista = [1, 2, 3]
    resultado = ordenar_de_mayor_a_menor(lista)
    assert resultado is None, "La función no debe devolver ningún valor."


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de variables.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
