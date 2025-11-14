"""
PROYECTO DE PROGRAMACIÓN: Cadenas, tuplas, diccionarios y anagramas

Instrucciones:
Lee con atención cada ejercicio. Completa el código en las secciones marcadas como TODO.
Puedes probar tus funciones en la sección "if __name__ == '__main__'".
"""

# ============================
# EJERCICIO 1: Tuplas no hashables
# ============================

from diccionario import value_counts


def tupla_no_hashable():
    """
    Crea una tupla que contiene listas como elementos. Intenta usarla como clave en un diccionario.
    """
    list0 = [1, 2, 3]
    list1 = [4, 5]
    t = (list0, list1)

    # TODO: Añade el número 6 al final de la segunda lista (list1) usando t
    # Resultado esperado: ([1, 2, 3], [4, 5, 6])
    t[1].append(6)
    print(t)

    # TODO: Intenta usar la tupla t como clave en un diccionario y captura el error con try-except
    # Debes imprimir un mensaje que diga que no se puede usar como clave si ocurre un TypeError
    try:
        d = {t: "valor"}
    except TypeError:
        print("No se puede usar una tupla con listas como clave en un diccionario.")


# ============================
# EJERCICIO 2: Cifrado César
# ============================

def shift_word(word, shift):
    """
    Aplica un cifrado César a la palabra dada, desplazando cada letra por 'shift' posiciones.
    Se espera que la palabra esté en minúsculas y sin caracteres especiales.

    Ejemplo:
    shift_word("alegria", 7) -> "alegre"
    shift_word("melon", 16) -> "al cubo"
    """
    # TODO: Implementa el cifrado César aquí
    # Tip: Usa letter_map y operador % para hacer el desplazamiento circular
    letters = 'abcdefghijklmnopqrstuvwxyzáéíóúñ '
    letter_map = dict(zip(letters, range(len(letters))))
    reverse_map = dict(zip(range(len(letters)), letters))
    result = []

    # Recorre cada letra y aplícale el desplazamiento
    for letter in word:
        # TODO: Maneja letras no reconocidas (espacios, tildes, etc.)
        if letter in letter_map:
            original_index = letter_map[letter]
            shifted_index = (original_index + shift) % len(letters)
            result.append(reverse_map[shifted_index])
        else:
            result.append(letter)  # Si la letra no está en el mapa, la dejamos igual

    # Une la lista resultante en una cadena
    return ''.join(result)


# ============================
# EJERCICIO 3: Letras más frecuentes
# ============================

def most_frequent_letters(texto):
    """
    Recibe una cadena y muestra las letras ordenadas por frecuencia (de mayor a menor).
    """
    # TODO: Cuenta las letras ignorando espacios y ordena por frecuencia
    # Tip: Usa value_counts() del ejercicio anterior si lo tienes
    value_count = value_counts(texto.replace(" ", "").lower())
    sorted_letters = sorted(value_count.items(), key=lambda item: item[1], reverse=True)
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")


# ============================
# EJERCICIO 4: Anagramas en lista
# ============================

def encontrar_anagramas(lista_palabras):
    """
    Dada una lista de palabras, imprime todos los grupos de palabras que son anagramas.

    Ejemplo de salida:
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    """
    # TODO: Crea un diccionario que relacione la palabra ordenada con sus anagramas
    anagram_dict = {}
    for palabra in lista_palabras:
        clave = ''.join(sorted(palabra))
        if clave in anagram_dict:
            anagram_dict[clave].append(palabra)
        else:
            anagram_dict[clave] = [palabra]

    # Imprime los grupos de anagramas
    for grupo in anagram_dict.values():
        if len(grupo) > 1:
            print(grupo)


# ============================
# EJERCICIO 5: Distancia entre palabras
# ============================

def word_distance(word1, word2):
    """
    Devuelve el número de letras distintas entre dos palabras de igual longitud.

    Ejemplo:
    word_distance("casa", "cata") -> 1
    """
    # TODO: Usa zip para comparar letra por letra y contar diferencias
    if len(word1) != len(word2):
        raise ValueError("Las palabras deben tener la misma longitud.")

    return sum(1 for a, b in zip(word1, word2) if a != b)


# ============================
# EJERCICIO 6: Pares de metátesis
# ============================

def encontrar_metatesis(lista_palabras):
    """
    Imprime todos los pares de palabras que son anagramas y difieren solo por una transposición (intercambio de dos letras).

    Ejemplo:
    ('converse', 'conserve')
    """
    # TODO:
    # 1. Encuentra anagramas usando el mismo enfoque del ejercicio anterior
    # 2. Para cada par en cada grupo de anagramas, verifica si son pares de metátesis
    #    (solo deben diferir en exactamente dos letras y ser del mismo largo)
    anagram_dict = {}
    for palabra in lista_palabras:
        clave = ''.join(sorted(palabra))
        if clave in anagram_dict:
            anagram_dict[clave].append(palabra)
        else:
            anagram_dict[clave] = [palabra]

    # Imprime los pares de metátesis
    for grupo in anagram_dict.values():
        if len(grupo) > 1:
            for i in range(len(grupo)):
                for j in range(i + 1, len(grupo)):
                    w1, w2 = grupo[i], grupo[j]
                    if word_distance(w1, w2) == 2:
                        print((w1, w2))


# ============================
# PRUEBAS
# ============================

if __name__ == '__main__':
    print("EJERCICIO 1: Tupla no hashable")
    tupla_no_hashable()

    print("\nEJERCICIO 2: Cifrado César")
    print(shift_word("murcielago", 5))    # Esperado: "alegre"
    print(shift_word("program", 10))     # Esperado: "al cubo"

    print("\nEJERCICIO 3: Letras más frecuentes")
    most_frequent_letters("este es un texto de prueba para contar la frecuencia de letras")

    print("\nEJERCICIO 4: Anagramas en lista")
    palabras = ['amor', 'roma', 'ramo', 'python', 'typhon', 'hola', 'aloh', 'test', 'sett']
    encontrar_anagramas(palabras)

    print("\nEJERCICIO 5: Distancia entre palabras")
    print(word_distance("casa", "cata"))  # Esperado: 1
    print(word_distance("perro", "gorro"))    # Esperado: 2
    print(word_distance("python", "typhon"))  # Esperado: 6
    try:
        print(word_distance("casa", "casita"))  # Debería lanzar error
    except ValueError as e:
        print("Error esperado:", e)

    print("\nEJERCICIO 6: Pares de metátesis")
    palabras = ['listen', 'silent', 'enlist', 'rescue', 'secure', 'recuse', 'converse', 'conserve']
    encontrar_metatesis(palabras)
