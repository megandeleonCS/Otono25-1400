import turtle


def configurar_tortuga():
    """Set up the turtle with initial settings."""
    t = turtle.Turtle()
    t.speed(10)
    turtle.bgcolor("black")
    return t

def dibujar_cuadro(t, size, color):
    """Draw a square of given size and color."""
    t.color(color)
    for _ in range(4):
        t.forward(size)
        t.right(90)

def dibujar_espiral(t, num_squares):
    """Draw a spiral made of squares with increasing size and changing colors."""
    colors = ["red", "yellow", "blue", "green", "orange", "purple"]
    size = 20
    for i in range(num_squares):
        dibujar_cuadro(t, size, colors[i % len(colors)])
        t.right(15)
        size += 10

def main():
    screen = turtle.Screen()
    t = configurar_tortuga()
    dibujar_espiral(t, 20)
    screen.mainloop()

if __name__ == "__main__":
    main()