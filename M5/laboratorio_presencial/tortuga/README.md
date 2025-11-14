Explicacion del codigo:

# import turtle
Permite usar la biblioteca turtle para dibujar gráficos con la tortuga.

# configurar_tortuga()
Crea un objeto tortuga llamado t, configura la velocidad de movimiento, cambia el color de fondo a negro y devuelve el objeto t para que otras funciones puedan usarlo.

# dibujar_cuadro()
Recibe tres argumentos: la tortuga t, el tamaño de un lado del cuadrado (size) y el color del dibujo (color). Cambia el color del lápiz y usa un bucle para dibujar un cuadrado con cuatro lados.

# dibujar_espiral()
Recibe la tortuga t y el número de cuadrados que se dibujarán (num_squares). Define una lista de colores para usar en secuencia. Empieza con un tamaño inicial de 20. Luego, en un bucle, dibuja cuadrados con tamaños crecientes y colores alternados, gira la tortuga 15 grados para crear el efecto espiral y aumenta el tamaño del cuadrado en 10 píxeles en cada iteración.

# main()
Aquí comienza el programa. Crea la ventana de dibujo, configura la tortuga, llama a las funciones para dibujar la espiral y mantiene la ventana abierta hasta que el usuario la cierre.

# if __name__ == "__main__":
Esta línea le dice a Python que ejecute la función main() solo si el archivo se está ejecutando directamente, y no si se importa desde otro archivo.

Intenta uno de estos cambios:
- Modifica los colores a rosa, cyan, morado, y naranja.
- Cambia el angulo de giro a 30 grados. 
- Modifica la variable size para que crezca mas rapida.
- Cambia el numero de cuadros que se dibujan a 30.