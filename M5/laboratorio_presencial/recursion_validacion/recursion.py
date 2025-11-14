

## Una funcion que se lla a si mismo para resolver un pedazo pequeno del problema

# Si queremos calcular el factorial de un numero. La funcion devuelve un valor se llama hasta llegar a 1. 
# Return nos sirve si queremos usar eso de nuevo.

def factorial(n):
    if n == 1:
        return 1  # Caso base: cuando n es 1, regresamos 1
    return n * factorial(n - 1)  # Llamada recursiva

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")


## No todas las funciones tienen que devolver algo como por ejemplo este, solo imprime un saludo.

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")


## Si no pones un return y lo tratas de imprimir, que pasa?
def no_hace_nada():
    pass

resultado = no_hace_nada()
print(resultado)  


## Una funcion para revisar que tenemos un dato adecuado. Primero miramos si lo ingresado es correcto antes de correr el codigo. En este caso queremos que la entrada sea positiva.

def obtener_entero_positivo():
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo: "))
            if numero > 0:
                return numero
            else:
                print("Por favor, ingresa un número mayor que 0.")
        except ValueError:
            print("Eso no es un número válido.")

# Ejemplo de uso
numero_valido = obtener_entero_positivo()
print(f"Ingresaste el número {numero_valido}")


## Ahora combinamos recursion con return y validacion de entrada o input. 


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def obtener_entero_positivo():
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo: "))
            if numero > 0:
                return numero
            else:
                print("Debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

# Programa principal
numero = obtener_entero_positivo()
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")