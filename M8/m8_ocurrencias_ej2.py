# --------------------------------------------------------------------------
#          FUNCIÓN PARA ELIMINAR UN ELEMENTO DE UNA LISTA
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que reciba una lista y un elemento,
# y devuelva una nueva lista sin ninguna de las ocurrencias de ese elemento.
#
# Instrucciones para el estudiante:
# 1. Completa la función `eliminar_elemento`.
# 2. Inicializa una nueva lista vacía para almacenar el resultado.
# 3. Itera sobre cada `item` en la `lista_original`.
# 4. Dentro del bucle, comprueba si el `item` actual NO es igual al
#    `elemento_a_eliminar`.
# 5. Si no son iguales, añade el `item` a tu nueva lista de resultados.
# 6. Después de que el bucle termine, devuelve la nueva lista.
#
# Nota: Este método (crear una lista nueva) es una forma segura de
# "eliminar" elementos sin modificar la lista mientras la recorres,
# lo cual puede causar errores inesperados.
# --------------------------------------------------------------------------

def eliminar_elemento(lista_original, elemento_a_eliminar):
    """
    Crea una nueva lista sin las ocurrencias de un elemento específico.

    Args:
      lista_original (list): La lista de la que se eliminarán elementos.
      elemento_a_eliminar: El elemento que se desea eliminar.

    Returns:
      list: Una nueva lista sin el elemento especificado.
    """
    # TODO: Paso 1. Inicializa una lista vacía para el resultado llamado nueva_lista.
    nueva_lista = []
    # TODO: Paso 2. Itera sobre cada elemento en la lista original.
    # for item in ...:
    for item in lista_original:
    # TODO: Paso 3. Comprueba si el elemento actual NO es el que se debe eliminar.
    # if item != ...:
     if item != elemento_a_eliminar:
    # TODO: Paso 4. Si no lo es, añádelo a la nueva lista.
    # nueva_lista.append(...)
      nueva_lista.append(item)
    # TODO: Paso 5. Devuelve la nueva lista.
    return nueva_lista
    


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    colores = ["rojo", "verde", "azul", "rojo", "amarillo", "rojo"]
    elemento = "rojo"

    lista_filtrada = eliminar_elemento(colores, elemento)

    print(f"Lista original: {colores}")
    print(f"Elemento a eliminar: '{elemento}'")
    print(f"Lista resultante: {lista_filtrada}")
