# --------------------------------------------------------------------------
#          CLASE RECTANGULO CON COMPARACIÓN DE EQUIVALENCIA
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es entender la diferencia entre identidad (`is`) y
# equivalencia (`==`). Modificaremos la clase `Rectangulo` para que
# dos objetos se consideren "iguales" si tienen las mismas dimensiones,
# aunque no sean el mismo objeto en memoria.
#
# Instrucciones para el estudiante:
# 1. La clase `Rectangulo` se proporciona con su `__init__`.
# 2. Implementa el método especial `__eq__(self, otro)`. Este método
#    define cómo funciona el operador `==` para los objetos de esta clase.
# 3. Dentro de `__eq__`, primero comprueba si `otro` es realmente una
#    instancia de `Rectangulo`. Si no, no pueden ser iguales.
# 4. Si es un `Rectangulo`, compara los atributos `ancho` y `alto` de
#    `self` con los de `otro`. Devuelve `True` si ambos son iguales,
#    y `False` en caso contrario.
# 5. Analiza el bloque de prueba para ver las diferencias entre `is` y `==`.
# --------------------------------------------------------------------------

class Rectangulo:
    """Una clase para representar un rectángulo."""

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def __eq__(self, otro):
        """
        Comprueba si este rectángulo es equivalente a otro.

        Args:
          otro: El objeto con el que se compara.

        Returns:
          bool: True si tienen las mismas dimensiones, False en caso contrario.
        """
        # TODO: Paso 1. Comprueba si `otro` es una instancia de `Rectangulo`.
        
        if not isinstance(otro, Rectangulo):
            return False

        # TODO: Paso 2. Compara los atributos y devuelve el resultado.
        
        return self.ancho == otro.ancho and self.alto == otro.alto
        

# --- Bloque para probar tu clase ---
if __name__ == "__main__":
    r1 = Rectangulo(10, 20)
    r2 = Rectangulo(10, 20)  # Otro objeto, pero con los mismos datos
    r3 = r1                 # Misma referencia, mismo objeto

    print("--- Comparando r1 y r2 ---")
    print(f"r1 == r2 (Equivalencia): {r1 == r2}")
    print(f"r1 is r2 (Identidad):    {r1 is r2}")

    print("\n--- Comparando r1 y r3 ---")
    print(f"r1 == r3 (Equivalencia): {r1 == r3}")
    print(f"r1 is r3 (Identidad):    {r1 is r3}")
