import math

# Crear una función para verificar si un número es un cuadrado perfecto
# Completar las 3 tareas especificadas con TODO

def es_cuadrado_perfecto(n):
    # TODO 1: Si el número es negativo, no puede ser un cuadrado perfecto. 
    # Asi que utiliza if para ver si n es menos que 0,
    # si lo es que devuelva un Falso para nuestro Booleano
   if n < 0:

    # Calcular la raíz cuadrada entera del número
    raiz_entera = int(n ** 0.5)  

    # Verificar si la raíz al cuadrado es igual al número original
    #return raiz_entera * raiz_entera == n
    return math.isqrt(n) ** 2 == n

# Entrada del usuario
num_usuario = int(input("¿Qué número te gustaría revisar si es cuadrado perfecto? "))

# Mostrar el resultado
if es_cuadrado_perfecto(num_usuario):
    print(f" El número {num_usuario} es un cuadrado perfecto.")
else:
    #TODO 2: Dar un mensaje al usuario si NO es cuadrado perfecto. 
    print("No es cuadrado perfecto 😢.")    


# TODO 3: Puedes encontrar el error en el siguiente codigo? Quita los simbolos # para probar el codigo linea por linea.

# Este codigo prueba si es cuadrado perfecto de una vez con una lista de valores
import math
def es_cuadrado_perfecto(num):
   if num < 0:
      return False
   raiz = int(math.sqrt(num))
   return raiz * raiz == num
print("\n Pruebas automáticas con varios valores:")
test_valores = [0, 1, 4, 9, 16, 25, 26, 27, 100, 101, -1, -4]
for num in test_valores:   
   resultado = es_cuadrado_perfecto(num)
   estado = "✅" if resultado else "❌"
   print(f"{estado} {num} {'es' if resultado else 'NO es'} un cuadrado perfecto.")