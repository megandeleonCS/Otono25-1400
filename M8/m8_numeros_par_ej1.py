# --------------------------------------------------------------------------
#          FUNCIÓN PARA FILTRAR NÚMEROS PARES DE UNA LISTA
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que reciba una lista de números y
# devuelva una nueva lista que contenga únicamente los números pares
# de la lista original.
#
# Instrucciones para el estudiante:
# 1. Completa la función `filtrar_numeros_pares`.
# 2. Inicializa una nueva lista vacía, por ejemplo `numeros_pares = []`.
#    Esta lista almacenará el resultado.
# 3. Usa un bucle `for` para iterar sobre cada `numero` en la `lista_numeros`.
# 4. Dentro del bucle, usa el operador módulo (%) para comprobar si el
#    `numero` es par.
# 5. Si el número es par, añádelo a tu lista `numeros_pares` usando el
#    método `.append()`.
# 6. Después de que el bucle termine, devuelve la lista `numeros_pares`.
# --------------------------------------------------------------------------

def filtrar_numeros_pares(lista_numeros):
    """
    Filtra una lista de números y devuelve una nueva lista solo con los pares.

    Args:
      lista_numeros (list): Una lista de números enteros.

    Returns:
      list: Una nueva lista que contiene solo los números pares.
    """
    # TODO: Paso 1. Inicializa una lista vacía para guardar los números pares.
    numeros_pares = []
   
    # TODO: Paso 2. Itera sobre cada número en la lista de entrada.
    # for numero in ...:
    for numero in lista_numeros:
    # TODO: Paso 3. Comprueba si el número es par.
    # if ... % 2 == 0:
     if numero % 2 == 0:
    # TODO: Paso 4. Si es par, añádelo a la lista `numeros_pares`.
    # numeros_pares.append(...)
      numeros_pares.append(numero)

    # TODO: Paso 5. Devuelve la nueva lista con los números pares.
    return numeros_pares


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares_filtrados = filtrar_numeros_pares(lista_original)

    print(f"Lista original: {lista_original}")
    print(f"Números pares filtrados: {pares_filtrados}")

    lista2 = [11, 13, 15, 17]
    pares2 = filtrar_numeros_pares(lista2)
    print(f"Lista original: {lista2}")
    print(f"Números pares filtrados: {pares2}")

    lista3 = [11, 13, -8, 0]
    pares3 = filtrar_numeros_pares(lista3)
    print(f"Lista original: {lista3}")
    print(f"Números pares filtrados: {pares3}")
# --- Fin del bloque de prueba ---
