#TODO2Escribe un método Line llamado midpoint 
#que calcule el punto mediode un segmento de recta y devuelva el resultado como un objeto Point.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2
        return Point(mid_x, mid_y) 
# Ejemplo de uso:
p1 = Point(0, 0)
p2 = Point(2, 2)
line = Line(p1, p2)
midpoint = line.midpoint()
print(f"Midpoint: ({midpoint.x}, {midpoint.y})")  

if __name__ == "__main__":
    # Pruebas adicionales
    p3 = Point(1, 3)
    p4 = Point(5, 7)
    line2 = Line(p3, p4)
    midpoint2 = line2.midpoint()
    print(f"Midpoint: ({midpoint2.x}, {midpoint2.y})")  # Debería imprimir Midpoint: (3.0, 5.0) # Debería imprimir Midpoint: (1.0, 1.0)