# test_equivalencia_rectangulo.py
# Archivo de pruebas para la clase Rectangulo y su método __eq__.

import pytest

try:
    # TODO: cambia 'solution_m13_ex1' por 'student_code_m13_ex1' si estás usando el código del estudiante.
    # from solution_m13_ex1 import Rectangulo
    from student_code_m13_ex1 import Rectangulo

except ImportError:
    pytest.fail(
        "No se pudo importar la clase 'Rectangulo' del archivo 'student_code_m13_ex1.py'.")


def test_equivalencia_objetos_iguales():
    """Prueba que dos rectángulos con las mismas dimensiones son equivalentes."""
    r1 = Rectangulo(10, 5)
    r2 = Rectangulo(10, 5)
    assert (r1 == r2) is True


def test_no_equivalencia_ancho_diferente():
    """Prueba que dos rectángulos con anchos diferentes no son equivalentes."""
    r1 = Rectangulo(10, 5)
    r2 = Rectangulo(11, 5)
    assert (r1 == r2) is False


def test_no_equivalencia_alto_diferente():
    """Prueba que dos rectángulos con altos diferentes no son equivalentes."""
    r1 = Rectangulo(10, 5)
    r2 = Rectangulo(10, 6)
    assert (r1 == r2) is False


def test_identidad_vs_equivalencia():
    """Verifica explícitamente la diferencia entre `is` y `==`."""
    r1 = Rectangulo(100, 200)
    r2 = Rectangulo(100, 200)
    r3 = r1

    assert r1 == r2  # Equivalentes en valor
    assert r1 is not r2  # No son el mismo objeto
    assert r1 is r3     # Son el mismo objeto


def test_comparacion_con_otro_tipo():
    """Prueba la comparación de un Rectangulo con un objeto de otro tipo."""
    r1 = Rectangulo(10, 5)
    assert (r1 == "un string") is False
    assert (r1 == 123) is False


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
