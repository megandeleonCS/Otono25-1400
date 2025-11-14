# --------------------------------------------------------------------------
#          FUNCIÓN PARA LEER Y PROMEDIAR PUNTAJES DESDE UN ARCHIVO
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que lea una lista de puntajes desde un
# archivo de texto, calcule el promedio y maneje posibles errores, como
# que el archivo no exista o que contenga datos no numéricos.
#
# Instrucciones para el estudiante:
# 1. Completa la función `promedio_de_archivo`.
# 2. Usa un bloque `try...except` para manejar la apertura del archivo.
#    - Si el archivo no se encuentra, debe capturar `FileNotFoundError` y
#      devolver un mensaje de error.
# 3. Dentro del bloque `try`, lee todas las líneas del archivo.
# 4. Itera sobre cada línea, conviértela a un número entero y súmala
#    a un total. Aquí puede ocurrir un `ValueError` si la línea no es un
#    número. Debes manejar este caso, pero por ahora nos enfocaremos
#    en el archivo no encontrado.
# 5. Si no hay puntajes en el archivo, devuelve 0.0 para evitar una
#    división por cero.
# 6. Calcula y devuelve el promedio.
# --------------------------------------------------------------------------

def promedio_de_archivo(nombre_archivo):
    """
    Lee puntajes de un archivo, los promedia y maneja errores.

    Args:
      nombre_archivo (str): La ruta al archivo de texto.

    Returns:
      float or str: El promedio de los puntajes o un mensaje de error.
    """
    # TODO: Paso 1. Inicia un bloque try para manejar errores.
    try:
        # TODO: Paso 2. Abre el archivo en modo lectura ('r').
        # with open(...) as archivo:
        # TODO: Paso 3. Lee todas las líneas del archivo.
        # lineas = archivo.readlines()

        puntajes = []
        # TODO: Paso 4. Itera sobre cada línea, conviértela a entero
        # y añádela a la lista `puntajes`.
        # for linea in lineas:
        #     puntajes.append(int(linea.strip()))

        # TODO: Paso 5. Si la lista de puntajes está vacía, devuelve 0.0.
        # if not puntajes:
        #     return 0.0

        # TODO: Paso 6. Calcula la suma y el promedio.
        # promedio = sum(puntajes) / len(puntajes)
        # return promedio
        pass  # Borra este pass

    # TODO: Paso 7. Captura la excepción si el archivo no se encuentra.
    except FileNotFoundError:
        return "Error: el archivo no fue encontrado."
    # Opcional: Captura errores de datos inválidos.
    except ValueError:
        return "Error: el archivo contiene datos no numéricos."


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    # Para probar, primero crea un archivo llamado 'puntajes.txt'
    # y escribe algunos números, uno por línea.
    # Ejemplo de contenido para 'puntajes.txt':
    # 100
    # 85
    # 90

    # Crear un archivo de prueba
    try:
        with open("puntajes.txt", "w") as f:
            f.write("100\n")
            f.write("85\n")
            f.write("90\n")
        print("Archivo 'puntajes.txt' creado para la prueba.")
    except Exception as e:
        print(f"No se pudo crear el archivo de prueba: {e}")

    print(f"Promedio de 'puntajes.txt': {promedio_de_archivo('puntajes.txt')}")
    print(
        f"Promedio de 'archivo_inexistente.txt': {promedio_de_archivo('archivo_inexistente.txt')}")


## TODO: Analizando
"""
1. Propósito del Bloque with y Cierre de Archivos:
¿Cuál es la ventaja clave de usar la sintaxis with open(...) as archivo:
en lugar de simplemente archivo = open(...)? ¿Qué acción de "limpieza" o
manejo de recursos realiza esta estructura automáticamente, incluso si ocurre
un error dentro del bloque try?

2. Manejo de Errores Específicos vs. Generales:
En el código, estamos capturando FileNotFoundError y ValueError por separado.
¿Por qué es más informativo y mejor práctica capturar errores tan específicos
en lugar de usar un except genérico (como except Exception:)? Explica cómo el
lugar donde ocurre cada uno de esos dos errores impacta la ejecución del
programa.

3. Lógica Condicional y Evitar Fallos:
La línea if not puntajes: return 0.0 es crucial después de la lectura del
Archivo. ¿Qué tipo de error exacto de Python (por ejemplo, IndexError,
TypeError, etc.) ocurriría en la línea promedio = suma_puntajes / len(puntajes)
si esta verificación se eliminara y el archivo de entrada estuviera vacío?
"""