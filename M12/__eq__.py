#Todo1 Metodo __eq__
#Escribe un método __eq__ para la clase Line que devuelva
#True si los objetos Line se refieren a objetos Point equivalentes,
#en cualquier orden.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        return (self.p1 == other.p1 and self.p2 == other.p2) or \
               (self.p1 == other.p2 and self.p2 == other.p1)
# Ejemplo de uso:
p1 = Point(0, 0)
p2 = Point(1, 1)
line1 = Line(p1, p2)
line2 = Line(p2, p1)        
print(line1 == line2)  # Debería imprimir True

if __name__ == "__main__":
    # Pruebas adicionales
    p3 = Point(2, 2)
    line3 = Line(p1, p3)
    print(line1 == line3)  # Debería imprimir False


