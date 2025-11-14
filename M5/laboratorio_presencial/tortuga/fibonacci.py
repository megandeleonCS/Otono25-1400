import turtle

""" Recursion en Fibonacci. Fibonacci en naturaleza (proporciones del cuerpo humano, girasoles, pinas, hojas), en matematica (Golden ratio), en arte (Da Vinci Vitruvian Man), diseno (templos Griegos)"""


# Función recursiva para generar la sucesión de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Inicializar Turtle
pantalla = turtle.Screen()
pantalla.bgcolor("white")

espiral = turtle.Turtle()
espiral.speed(3)  # Velocidad máxima

# Colores opcionales
colores = ["red", "orange", "yellow", "green", "blue", "purple"]

# Número de pasos de Fibonacci a dibujar
pasos = 14

# Dibujar espiral de Fibonacci
longitud = 5
for i in range(pasos):
    espiral.pencolor(colores[i % len(colores)])
    fib = fibonacci(i)
    espiral.forward(fib * longitud)
    espiral.left(90)

# Finalizar
turtle.done()