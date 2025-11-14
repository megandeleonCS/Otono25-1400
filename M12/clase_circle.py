#TODO5Escribe una definición para una clase llamada Circle con atributos center y radius,
#donde center es un objeto Point y radius es un número. Incluye los métodos especiales
#__init__ y a __str__, y un método llamado draw que utilice las funciones jupyturtle
#para dibujar el círculo.

import turtle
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
class Circle:
    def __init__(self, center, radius):
        self.center = center  # center is a Point object
        self.radius = radius  # radius is a number

    def __str__(self):
        return f"Circle with center at ({self.center.x}, {self.center.y}) and radius {self.radius}"

    def draw(self):
        turtle.penup()
        turtle.goto(self.center.x, self.center.y - self.radius)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.done()


# Ejemplo de uso:
center_point = Point(0, 0)
circle = Circle(center_point, 50)
print(circle)  # Debería imprimir: Circle with center at (0, 0) and radius 50
circle.draw()  # Dibuja el círculo usando turtle    

if __name__ == "__main__":
    # Pruebas adicionales
    center_point2 = Point(100, 100)
    circle2 = Circle(center_point2, 75)
    print(circle2)  # Debería imprimir: Circle with center at (100, 100) and radius 75
    circle2.draw()  # Dibuja el círculo usando turtle