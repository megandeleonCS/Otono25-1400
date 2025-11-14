Funcion de F a C
Este ejercicio te ayudará a entender cómo escribir y usar tus propias funciones para que tu código sea organizado, reutilizable y fácil de leer.

¿Qué es una Función?
Piensa en una función como un mini-programa o una receta. Es un bloque de código que realiza una tarea específica. En lugar de escribir las mismas líneas de código una y otra vez, puedes agruparlas dentro de una función y simplemente "llamarlas" cada vez que necesites realizar esa tarea.

Una función se define usando la palabra clave def, seguida del nombre de la función y paréntesis ().

def mi_funcion():
  print("¡Hola desde una función!")

El if __name__ == '__main__' o "Guardia Principal"

A menudo verás esta línea de código de aspecto extraño en los programas de Python. Se llama el "guardia principal" y es una buena práctica. Verifica si el archivo de Python está siendo ejecutado directamente por el usuario. Si es así, el código dentro del bloque se ejecutará.

¿Por qué es útil? Evita que el código se ejecute automáticamente si el archivo se importa como un módulo en otro programa. Mantiene tu código limpio y predecible.


Aquí está la estructura básica:

def mi_funcion():
  # Tu código va aquí
  pass

if __name__ == '__main__':
  # Llama a tu función aquí
  mi_funcion()


1. Tu tarea es escribir un programa en Python que incluya al menos una función y use el bloque if __name__ == '__main__'.

2. Elige un Objetivo: Decide una tarea sencilla para tu función. Por ejemplo: Una función que convierta la temperatura de Celsius a Fahrenheit.

3. Define tu Función: Escribe tu función usando la palabra clave def. Recuerda darle un nombre descriptivo que te diga lo que hace.

4. Añade tu Código: Dentro de la función, escribe el código que realiza la tarea que elegiste.

5. Añade el Guardia Principal: Al final de tu archivo, agrega el bloque if __name__ == '__main__'.

6. Llama a tu Función: Dentro del bloque if, llama a tu función por su nombre seguido de paréntesis ().

Ejemplo: Una Calculadora Simple
Aquí tienes un ejemplo sencillo para empezar. Estúdialo para entender la estructura.

def sumar_numeros(num1, num2):
  """Esta función suma dos números y muestra el resultado."""
  resultado = num1 + num2
  print(f"La suma es: {resultado}")

if __name__ == '__main__':
  # Podemos llamar a nuestra función aquí con valores específicos
  sumar_numeros(5, 10)
  # También puedes usar variables
  numero_a = 20
  numero_b = 30
  sumar_numeros(numero_a, numero_b)
