Tarea 1: Descifrando la Calculadora de Descuento

Objetivo
Analizarás una función en Python que calcula el precio final de un artículo después de aplicar un descuento. Tu objetivo es añadir comentarios detallados que expliquen exactamente lo que sucede en cada línea del código.

Instrucciones
Lee y Comprende el Código: Lee atentamente toda la función calcular_descuento(). Tómate un momento para entender su propósito general: pide el precio original y el porcentaje de descuento, y luego calcula el precio final.

1. Añade un Comentario a Nivel de Función: Comienza agregando un docstring justo debajo de la definición de la función (def calcular_descuento():). Este docstring debe ser un resumen breve y de alto nivel de lo que hace la función completa. Piensa en él como un manual de usuario para la función.

Ejemplo: """Esta función... """

2. Añade Comentarios Línea por Línea: Ahora, revisa cada línea de código dentro de la función y añade un comentario que explique su acción específica. Usa el símbolo #. Para cada línea, pregúntate:

¿Qué está haciendo esta línea? 
¿Con qué tipo de dato está trabajando?
¿Por qué es necesario este paso?

3. Analiza la Matemática: Presta especial atención a la línea donde se calcula precio_final. ¡Esta es la parte más importante! Desglosa la expresión.

Explica qué hace descuento / 100.

Explica qué logra 1 - (descuento / 100).

4. Da un ejemplo concreto, como: "Si el descuento es del 20%..."

Explica la Salida: Observa la instrucción print(). Esta línea es un poco más compleja. Explica qué significa la f antes de la cadena de texto y qué hace la parte :.2f. ¿Por qué es útil para mostrar precios?

Ejemplo de un Buen Comentario: 

# Esta línea obtiene el precio original del usuario y convierte la
# cadena de texto de entrada a un número flotante para poder realizar operaciones matemáticas.
precio_original = float(input('¿Cuál es el precio original del artículo? $'))