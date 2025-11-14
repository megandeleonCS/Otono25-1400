# --- Base de datos de Inventario ---
# El diccionario principal: la clave es el nombre del producto (string),
# y el valor es una tupla (precio_unitario, cantidad_en_stock).
inventario = {
    "Laptop": (1200.00, 15),
    "Mouse Inalámbrico": (25.50, 40),
    "Teclado Mecánico": (85.00, 22),
    "Monitor 27in": (350.00, 10)
}

def mostrar_inventario():
    """Imprime el inventario actual de forma legible."""
    print("\n--- INVENTARIO ACTUAL ---")
    print(f"{'PRODUCTO':<20}{'PRECIO':>10}{'STOCK':>10}")
    print("-" * 40)
    for nombre, detalles in inventario.items():
        precio, stock = detalles  # Desempaquetado de la tupla
        print(f"{nombre:<20}${precio:>9.2f}{stock:>10}")
    print("-------------------------")

def agregar_producto(nombre, precio, stock):
    """Agrega un nuevo producto o actualiza el stock/precio de uno existente."""
    # TODO 1: Añadir o Actualizar Producto
    # Crea una NUEVA TUPLA con el precio y stock, y úsala para actualizar
    # el diccionario 'inventario' con el nombre del producto como CLAVE.
    
    inventario[nombre] = (precio, stock)
    print(f"\n✅ Producto '{nombre}' agregado/actualizado.")

def buscar_precio(nombre):
    """Busca y retorna el precio unitario de un producto."""
    # TODO 2: Buscar Precio
    # Intenta obtener el valor asociado a la clave 'nombre' del diccionario.
    # Si la clave existe, desempaqueta la tupla para obtener el precio
    # (el primer elemento) y lo retorna. Si no existe, retorna None.
    
    detalles = inventario.get(nombre)
    if detalles:
        precio, _ = detalles
        return precio
    else:
        return None

def valor_total_inventario():
    """Calcula el valor monetario total de todos los productos en stock."""
    valor_total = 0.0
    for detalles in inventario.values():
        # TODO 3: Calcular Valor Total
        # Desempaqueta la tupla 'detalles' para obtener el precio y el stock.
        # Multiplica el precio por el stock y suma el resultado a 'valor_total'.
        
        precio, stock = detalles
        valor_total += precio * stock
        
        return valor_total

# --- Pruebas del Programa ---

# 1. Mostrar el inventario inicial
mostrar_inventario()

# 2. Agregar un nuevo producto (llamada a TODO 1)
agregar_producto("Webcam HD", 49.99, 30)

# 3. Mostrar inventario después de la adición
mostrar_inventario()

# 4. Buscar el precio de un producto (llamada a TODO 2)
precio_mouse = buscar_precio("Mouse Inalámbrico")
print(f"\n🔍 Precio del Mouse Inalámbrico: ${precio_mouse:.2f}")

# 5. Calcular el valor total (llamada a TODO 3)
total = valor_total_inventario()
print(f"\n💰 Valor total estimado de todo el inventario: ${total:,.2f}")