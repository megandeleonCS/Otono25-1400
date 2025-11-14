# --------------------------------------------------------------------------
#          FUNCIÓN PARA VALIDAR Y FORMATEAR UN NOMBRE DE USUARIO
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que "limpie" y valide una cadena de texto
# para que sirva como un nombre de usuario simple. Las reglas son:
# 1. No debe tener espacios en blanco al principio ni al final.
# 2. Debe estar completamente en minúsculas.
# 3. Debe contener únicamente caracteres alfabéticos (sin números ni símbolos).
#
# Instrucciones para el estudiante:
# 1. Completa la función `formatear_nombre_usuario`.
# 2. Usa el método `.strip()` para eliminar espacios en blanco de los extremos.
# 3. Usa el método `.lower()` para convertir la cadena a minúsculas.
# 4. Usa el método `.isalpha()` para comprobar si la cadena resultante
#    contiene solo letras.
# 5. Si `.isalpha()` devuelve True, la función debe retornar la cadena limpia.
# 6. Si devuelve False, la función debe retornar un mensaje de error específico.
# --------------------------------------------------------------------------

def formatear_nombre_usuario(nombre):
    """
    Limpia y valida una cadena para ser un nombre de usuario simple.

    Args:
      nombre (str): La cadena de entrada.

    Returns:
      str: El nombre de usuario limpio y en minúsculas, o un mensaje de error.
    """
    # TODO: Paso 1. Elimina espacios en blanco de los extremos.
    nombre_limpio = nombre.strip()

    # TODO: Paso 2. Convierte la cadena a minúsculas.
    nombre_final =  # Usa .lower() en la cadena ya limpia.

    # TODO: Paso 3. Comprueba si la cadena final contiene solo letras.
    # if nombre_final.isalpha() ...:
    # TODO: Paso 4. Si es válido, devuelve el nombre_final.
    # return ...
    # else:
    # TODO: Paso 5. Si no es válido, devuelve un mensaje de error.
    return "Error: el nombre de usuario solo puede contener letras."


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    test1 = "  UsuarioUno  "
    test2 = "Usuario2"
    test3 = "  VALIDO  "

    print(f"Entrada: '{test1}' -> Salida: '{formatear_nombre_usuario(test1)}'")
    print(f"Entrada: '{test2}' -> Salida: '{formatear_nombre_usuario(test2)}'")
    print(f"Entrada: '{test3}' -> Salida: '{formatear_nombre_usuario(test3)}'")


"""
Ejemplo de salida esperada:
Entrada: '   UsuarioUno  ' -> Salida: 'usuariouno'
Entrada: 'Usuario2' -> Salida: 'Error: el nombre de usuario solo puede contener letras.'
Entrada: '  VALIDO  ' -> Salida: 'valido'
Entrada: 'Usario Con Espacio' -> Salida: 'Error: el nombre de usuario solo puede contener letras.'
Entrada: '!' -> Salida: 'Error: el nombre de usuario solo puede contener letras.'
"""

"""
# TODO

1. Porque es importante usar .strip() antes que .lower(). Que pasaria si los
 pones al reves?
2. La función actual devuelve un mensaje de error general: "Error: el
 nombre de usuario solo puede contener letras." Si quisiéramos expandir
 la función para permitir números pero seguir previniendo símbolos
 (como !, @, #), ¿cómo modificarías el paso de validación actual
 (que usa .isalpha()), y cómo se vería un mensaje de error más específico
 en este caso?
3. ¿Por qué falla el control de validación (.isalpha() devuelve False)
 una entrada como "Usario Con Espacio"?
"""