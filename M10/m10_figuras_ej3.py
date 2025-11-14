# --------------------------------------------------------------------------
#          DEMOSTRACIÓN DE POLIMORFISMO CON FORMAS GEOMÉTRICAS
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es demostrar el polimorfismo. Crearemos varias clases de formas
# geométricas (`Circulo`, `Rectangulo`, `Triangulo`) que tienen un método
# con el mismo nombre: `dibujar`. Luego, escribiremos una única función que
# pueda dibujar cualquier forma de una lista, sin saber su tipo exacto.
#
# Instrucciones:
# 1. Revisa las clases `Circulo`, `Rectangulo` y `Triangulo`.
# 2. Implementa el método `dibujar()` para cada una de las clases.
#    - Para `Circulo`, debe imprimir "Dibujando un círculo de radio...".
#    - Para `Rectangulo`, debe imprimir "Dibujando un rectángulo de...".
#    - Para `Triangulo`, debe imprimir "Dibujando un triángulo de base...".
# 3. Observa cómo en el bloque de prueba, un solo bucle `for` puede
#    llamar al método `dibujar()` en objetos de diferentes clases.
# --------------------------------------------------------------------------

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def dibujar(self):
        # TODO: Imprime un mensaje describiendo el círculo.
        print(f"Dibujando un círculo de radio {self.radio}.")


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def dibujar(self):
        # TODO: Imprime un mensaje describiendo el rectángulo.
        print(f"Dibujando un rectángulo de {self.ancho}x{self.alto}.")


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def dibujar(self):
        # TODO: Imprime un mensaje describiendo el triángulo.
        print(f"Dibujando un triángulo de base {self.base} y altura {self.altura}.")


# --- Bloque para probar tus clases ---
if __name__ == "__main__":
    # Creamos una lista que contiene objetos de diferentes clases.
    formas = [
        Circulo(10),
        Rectangulo(20, 30),
        Triangulo(15, 25)
    ]

    print("--- Dibujando todas las formas ---")
    # Este bucle demuestra el polimorfismo.
    # La misma llamada `forma.dibujar()` funciona para cualquier objeto
    # que tenga ese método, sin importar si es un Círculo, Rectángulo o Triángulo.
    for forma in formas:
        forma.dibujar()

