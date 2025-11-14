"""
PROYECTO DE PROGRAMACIÓN: Funciones con cadenas, listas y diccionarios

Instrucciones:
Este archivo contiene varias tareas relacionadas con el uso de cadenas, listas y diccionarios.
Tu objetivo es completar las funciones que aparecen con la etiqueta TODO y seguir las instrucciones.

Puedes probar tus funciones utilizando el bloque "if __name__ == '__main__':" al final del archivo.
"""

# ============================
# TAREA 1: has_duplicates
# ============================

def has_duplicates(seq):
    """
    Devuelve True si hay elementos duplicados en la secuencia (lista o cadena), de lo contrario False.

    seq: lista o cadena

    Ejemplos:
    has_duplicates('hola') -> False
    has_duplicates('llama') -> True
    """
    # TODO: Escribe tu implementación aquí
    has_duplicates = set()
    for element in seq:
        if element in has_duplicates:
            return True
        has_duplicates.add(element)
    return False

    


# ============================
# TAREA 2: find_repeats
# ============================

def find_repeats(counter):
    """
    Devuelve una lista de claves cuyo valor en el diccionario es mayor que 1.

    counter: diccionario que asigna claves a contadores (por ejemplo, {'a': 3, 'b': 1})

    returns: lista de claves repetidas

    Ejemplo:
    find_repeats({'a': 2, 'b': 1, 'c': 3}) -> ['a', 'c']
    """
    # TODO: Escribe tu implementación aquí
    find_repeats = []
    for key, value in counter.items():
        if value > 1:
            find_repeats.append(key)
    return find_repeats


# ============================
# TAREA 3: add_counters
# ============================

def add_counters(dict1, dict2):
    """
    Combina dos diccionarios sumando los valores de las claves que aparecen en ambos.

    dict1, dict2: diccionarios con letras como claves y números como valores

    returns: nuevo diccionario combinado

    Ejemplo:
    dict1 = {'a': 2, 'b': 1}
    dict2 = {'a': 1, 'c': 4}
    add_counters(dict1, dict2) -> {'a': 3, 'b': 1, 'c': 4}
    """
    # TODO: Escribe tu implementación aquí
    add_counters = dict1.copy()
    for key, value in dict2.items():
        if key in add_counters:
            add_counters[key] += value
        else:
            add_counters[key] = value
    return add_counters


# ============================
# TAREA 4: is_interlocking
# ============================

def is_interlocking(word, word_list):
    """
    Devuelve True si la palabra se puede dividir en dos palabras válidas usando letras alternas.

    word: cadena a evaluar
    word_list: lista o conjunto de palabras válidas (por ejemplo, un diccionario en español)

    Ejemplo:
    is_interlocking('escolarizado', {'zapato', 'frío', 'es', 'colar', 'izado'}) -> True
    porque 'zapato' = word[0::2], 'frío' = word[1::2]

    Nota: Puedes asumir que las palabras del word_list están en minúsculas.

    Tip: Usa word[::2] y word[1::2] para obtener las dos mitades entrelazadas.
    """
    # TODO: Escribe tu implementación aquí
    first_half = word[::2]
    second_half = word[1::2]
    return first_half in word_list and second_half in word_list


# ============================
# FUNCIONES DE APOYO (opcional)
# ============================

def value_counts(word):
    """
    Cuenta cuántas veces aparece cada letra en una palabra.

    word: cadena

    returns: diccionario {letra: cantidad}

    Ejemplo:
    value_counts('banana') -> {'b':1, 'a':3, 'n':2}
    """
    counter = {}
    for letter in word:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter


# ============================
# PRUEBAS
# ============================

if __name__ == '__main__':
    # Puedes descomentar estas pruebas y añadir más para verificar tu código

    print("--- Pruebas de has_duplicates ---")
    print(has_duplicates('Hello'))       # False
    print(has_duplicates('Hola'))       # False

    print("\n--- Pruebas de find_repeats ---")
    test_counter = value_counts('platanos')
    print(test_counter)  # {'p': 1, 'l': 1, 'a': 2, 't': 1, 'n': 1, 'o': 1, 's': 1}
    print(find_repeats(test_counter))    # ['a']

    print("\n--- Pruebas de add_counters ---")
    c1 = value_counts('paralelepipedo')
    c2 = value_counts('paranoico')
    print(add_counters(c1, c2))

    print("\n--- Pruebas de is_interlocking ---")
    diccionario = {'hechizo', 'escoba', 'perros', 'pajaro', 'conejo', 'lobo', 'zapato', 'frío', 'es', 'colar', 'izado'}
    print(is_interlocking('escolarizado', diccionario))  # True o False dependiendo del set

    # Agrega más pruebas según necesites
