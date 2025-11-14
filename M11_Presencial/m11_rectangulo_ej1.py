# --------------------------------------------------------------------------
#          CLASE PARA REPRESENTAR UN RECTÁNGULO
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una clase `Rectangulo` que modele un rectángulo.
# La clase almacenará las dimensiones del rectángulo (ancho y alto) y
# tendrá un método para calcular su área.
#
# Instrucciones para el estudiante:
# 1. Completa el método `__init__`. Este método especial se llama cuando
#    se crea un nuevo objeto. Debe tomar `ancho` y `alto` como argumentos
#    y almacenarlos como atributos del objeto usando `self`.
# 2. Completa el método `calcular_area`. Este método no necesita argumentos
#    (aparte de `self`) y debe usar los atributos del objeto para calcular
#    y devolver el área.
# 3. Observa cómo se crea un objeto (instancia) de la clase y cómo se
#    llama a su método en el bloque de prueba.
# --------------------------------------------------------------------------

class Rectangulo:
    """
    Una clase para representar un rectángulo y calcular sus propiedades.
    """

    # TODO: TODO 1. Completa el método de inicialización.
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        """
        Inicializa un nuevo objeto Rectangulo.

        Args:
          ancho (int or float): El ancho del rectángulo.
          alto (int or float): El alto del rectángulo.
        """
        # Almacena el ancho y el alto como atributos de la instancia.
        # self.ancho = ...
        # self.alto = ...
        print(f"Rectángulo creado con ancho {ancho} y alto {alto}")

    # TODO: TODO 2. Completa el método para calcular el área.
    def calcular_area(self):
        
        
        """
        Calcula el área del rectángulo usando sus atributos.

        Returns:
          int or float: El área calculada.
        """
        # El área es el producto del ancho y el alto del objeto.
        # return self.ancho * ...
        return self.ancho * self.alto


# --- Bloque para probar tu clase ---
if __name__ == "__main__":
    # Crear una instancia (un objeto) de la clase Rectangulo
    mi_rectangulo = Rectangulo(10, 5)

    # Llamar a un método del objeto
    area = mi_rectangulo.calcular_area()

    print(f"El área del rectángulo es: {area}")
# --- Fin del bloque de prueba ---

""" Tiia Sahrakorpi
Que hacer con la basura?
Tiaa hablo de reciclar y reducir el desperdicio.
Tambien de reutilizar y compostar. Yo no sabia que el basurero mas cerca era Layton.
Tambien que el aluminio es el mas importante de reciclar porque se puede reusar en varias cosas.
En 1986 en Philadelphia cada persona aumento la basura que no reciclaban y ya no habia espacio que querian mandar su basura a otros estados incluyendo paises.Hay que ser mas concientes con el medio ambiente.
cuando queremos actualizar algun dipositivo electronico porque las tiendas solo le sacan lo que se puede reusar y el resto va a la basura.
y luego mandar esa basura a otros paises que no tienen regulaciones ambientales estrictas.
incluyendo a los paises mas pobres del mundo.
"""
