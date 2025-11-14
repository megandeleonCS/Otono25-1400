# test_formatear_usuario.py
# Archivo de pruebas para la función formatear_nombre_usuario.

import pytest

try:
    from M13.m13_codigo_ej1 import formatear_nombre_usuario
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'formatear_nombre_usuario' del archivo 'student_code_m8_ex1.py'.")


def test_nombre_valido():
    """Prueba un nombre válido sin espacios ni mayúsculas."""
    assert formatear_nombre_usuario("usuario") == "usuario"


def test_limpia_espacios():
    """Prueba que la función elimina espacios al principio y al final."""
    assert formatear_nombre_usuario("  pepito  ") == "pepito"


def test_convierte_a_minusculas():
    """Prueba que la función convierte la cadena a minúsculas."""
    assert formatear_nombre_usuario("MARIA") == "maria"


def test_limpia_y_convierte():
    """Prueba una combinación de espacios y mayúsculas."""
    assert formatear_nombre_usuario("  CARLOS  ") == "carlos"


def test_invalido_con_numeros():
    """Prueba que un nombre con números devuelve un error."""
    assert formatear_nombre_usuario(
        "usuario123") == "Error: el nombre de usuario solo puede contener letras."


def test_invalido_con_simbolos():
    """Prueba que un nombre con símbolos devuelve un error."""
    assert formatear_nombre_usuario(
        "user-name") == "Error: el nombre de usuario solo puede contener letras."
    assert formatear_nombre_usuario(
        "test@test") == "Error: el nombre de usuario solo puede contener letras."


def test_cadena_vacia_despues_de_limpiar():
    """Prueba que una cadena de solo espacios devuelve un error."""
    assert formatear_nombre_usuario(
        "   ") == "Error: el nombre de usuario solo puede contener letras."


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de variables.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
