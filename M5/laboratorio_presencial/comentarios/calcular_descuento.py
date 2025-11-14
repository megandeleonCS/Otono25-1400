##TODO 1: Agreguele descripciones/comentarios a cada paso de esta funcion. Que esta pasando?

def calcular_descuento():
    precio_original = float(input('¿Cuál es el precio original del artículo? $'))
    descuento = float(input('¿Cuál es el porcentaje de descuento? (por ejemplo, 20 para 20%) '))
    precio_final = precio_original * (1 - descuento / 100)
    print(f'El precio original es ${precio_original:.2f}, con un descuento del {descuento}%, el precio final es ${precio_final:.2f}')

if __name__ == '__main__':
    calcular_descuento()
