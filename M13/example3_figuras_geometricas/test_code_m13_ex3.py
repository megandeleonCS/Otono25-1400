# test_polimorfismo_formas.py
# Archivo de pruebas para las clases de formas y su comportamiento polimórfico.

import pytest

try:
    # TODO: cambia 'solution_m13_ex3' por 'student_code_m13_ex3' si estás usando el código del estudiante.
    # from solution_m13_ex3 import Circulo, Rectangulo, Triangulo
    from student_code_m13_ex3 import Circulo, Rectangulo, Triangulo
except ImportError:
    pytest.fail(
        "No se pudo importar una o más clases del archivo 'student_code_m13_ex3.py'.")


def test_dibujar_circulo(capsys):
    """Verifica la salida del método dibujar de la clase Circulo."""
    c = Circulo(5)
    c.dibujar()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Dibujando un círculo de radio 5."


def test_dibujar_rectangulo(capsys):
    """Verifica la salida del método dibujar de la clase Rectangulo."""
    r = Rectangulo(10, 20)
    r.dibujar()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Dibujando un rectángulo de 10x20."


def test_dibujar_triangulo(capsys):
    """Verifica la salida del método dibujar de la clase Triangulo."""
    t = Triangulo(8, 12)
    t.dibujar()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Dibujando un triángulo de base 8 y altura 12."


def test_bucle_polimorfico(capsys):
    """
    Prueba el comportamiento polimórfico llamando a dibujar en una lista de formas.
    """
    formas = [
        Circulo(7),
        Rectangulo(5, 10),
        Triangulo(3, 6)
    ]

    for forma in formas:
        forma.dibujar()

    captured = capsys.readouterr()
    salida_esperada = [
        "Dibujando un círculo de radio 7.",
        "Dibujando un rectángulo de 5x10.",
        "Dibujando un triángulo de base 3 y altura 6."
    ]

    # Compara cada línea de la salida capturada con la salida esperada.
    salidas_reales = [line for line in captured.out.strip().split('\n')]
    assert salidas_reales == salida_esperada


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de polimorfismo con formas geométricas.")
    # If the tests fail, print an error message
    else:
        print("❌ Fallaron algunas pruebas. Revisa los mensajes de error.")
#     # Asegúrate de que las clases Circulo, Rectangulo y Triangulo
