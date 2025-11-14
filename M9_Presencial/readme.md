Tu trabajo es completar la lógica de las siguientes tres secciones dentro del archivo de código:

📝 TODO 1: Añadir o Actualizar Producto
Implementa la lógica en la función agregar_producto(nombre, precio, stock):
Crea una nueva tupla con el precio y el stock proporcionados.
Usa el nombre del producto como clave para añadir o actualizar la entrada en el diccionario inventario.

📝 TODO 2: Buscar Precio
Implementa la lógica en la función buscar_precio(nombre):
Busca la clave nombre en el diccionario inventario.
Si el producto existe, desempaqueta la tupla de detalles y retorna solo el primer elemento (el precio).
Si el producto no se encuentra, la función debe retornar el valor None.

📝 TODO 3: Calcular Valor Total
Implementa la lógica en el bucle dentro de la función valor_total_inventario():
Itera sobre los valores (las tuplas) del diccionario inventario.
Dentro del bucle, desempaqueta cada tupla en sus variables precio y stock.
Calcula el valor del stock actual (precio * stock) y súmalo a la variable valor_total.

🔎 Preguntas de Investigación y Experimentación

# 1. Mutabilidad vs. Inmutabilidad: 
En el código, el valor de cada producto en el diccionario inventario es una tupla (por ejemplo, (1200.00, 15)). Si quisieras cambiar solo la cantidad en stock de un producto (el segundo elemento de la tupla) sin cambiar su precio, ¿por qué no podrías hacerlo directamente (como inventario["Laptop"][1] = 20)? ¿Qué modificación al código de la función agregar_producto tendrías que hacer para lograr actualizar el stock de un producto? Agregar una nueva tupla ya que las tuplas son inmutables osea que no se pueden editar

# 2. Claves Únicas del Diccionario:
¿Qué sucede si llamas a la función agregar_producto con un producto que ya existe en el diccionario (por ejemplo, agregar_producto("Laptop", 1250.00, 5))? Explica cómo se comporta el diccionario en este caso, y cómo esta propiedad de las claves únicas es útil para garantizar que solo haya una entrada por producto en el inventario. Se actualiza la nueva entrada que se puso no se puede poner doble solo se actualiza.

# 3. Tuplas en Acceso: 
En la función valor_total_inventario, se utiliza la línea for detalles in inventario.values():. ¿Cómo aprovecha el código la naturaleza ordenada de la tupla detalles para acceder al precio y al stock dentro del bucle sin usar un índice numérico ([0], [1])? ¿Por qué fue una buena decisión de diseño usar una tupla en lugar de una lista para almacenar los detalles fijos del producto? Porque la tupla es inmutable y aguarda los datos y en este ejercicio los datos son precisos y en orden y esto representa una estructura fija y mejora la claridad del codigo