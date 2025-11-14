# Programa para calcular el promedio de una lista de calificaciones

"""
Si ves un error como NameError, verifica que las variables estén bien nombradas.

Si ves un TypeError, revisa los tipos de datos (por ejemplo, no puedes sumar texto y número directamente).

Usa print() para ver qué valores tienen las variables en diferentes puntos del programa.
"""

def calcular_promedio(calificaciones):
    suma = 0
    notas = len(calificaciones)

    for nota in calificaciones:
        suma = suma + nota

    promedio = suma / len(calificaciones)
    return promedio

def main():
    calificacion = [8.5, 9.0, 7.5, 10, 6.0]
    promedio = calcular_promedio(calificacion)
    print(f"El promedio de las calificaciones es: {promedio}")

main()
