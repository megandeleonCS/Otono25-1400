# test_encontrar_emails.py
# Archivo de pruebas para la función encontrar_emails.

import pytest

try:
    from M13.m13_codigo_ej3 import encontrar_emails
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'encontrar_emails' del archivo 'student_code_m8_ex3.py'.")


def test_encontrar_multiples_emails():
    """Prueba un texto que contiene varias direcciones de correo electrónico."""
    texto = "Contacta a juan@test.com o a maria.lopez@web.es para más info."
    esperado = ["juan@test.com", "maria.lopez@web.es"]
    assert sorted(encontrar_emails(texto)) == sorted(esperado)


def test_texto_sin_emails():
    """Prueba un texto que no contiene ninguna dirección de correo."""
    texto = "Esta es una frase normal sin direcciones."
    assert encontrar_emails(texto) == []


def test_email_con_guiones_y_puntos():
    """Prueba emails que contienen caracteres especiales como guiones y puntos."""
    texto = "El correo es mi-nombre.apellido@un-dominio.largo.net"
    esperado = ["mi-nombre.apellido@un-dominio.largo.net"]
    assert encontrar_emails(texto) == esperado


def test_texto_vacio():
    """Prueba con una cadena de entrada vacía."""
    assert encontrar_emails("") == []


def test_emails_mezclados_con_texto():
    """Prueba que los emails se extraen correctamente cuando están pegados a otros caracteres."""
    texto = "Mi email es:info@sitio.com, por favor escribe."
    esperado = ["info@sitio.com"]
    assert encontrar_emails(texto) == esperado


def test_retorno_es_lista():
    """Verifica que la función siempre devuelve una lista."""
    assert isinstance(encontrar_emails("un texto de prueba"), list)


# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de variables.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
