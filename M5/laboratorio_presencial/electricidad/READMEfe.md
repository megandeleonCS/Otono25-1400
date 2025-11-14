Este ejercicio te desafía a entender y completar una función en Python que simula el cálculo de una factura de electricidad.  Pongale enfasis a este ejemplo, una operacion similar viene en el examen.

¿Qué Hace el Código?
El programa que vas a analizar y completar se llama factura_electricidad(). Su objetivo es calcular el costo de la electricidad basándose en un sistema de tarifas por niveles o "escalones". Esto significa que el precio que pagas por cada kilovatio-hora (kWh) cambia según tu consumo total.

Tu tarea es analizar el código, entender cómo funciona cada nivel de consumo y asegurarte de que los cálculos y la presentación final de la factura sean correctos.

Análisis del Código
El código utiliza una estructura condicional if/elif/else para determinar la tarifa aplicable:

Nivel 1: Si el consumo es de 100 kWh o menos, se aplica una tarifa fija.

Nivel 2: Si el consumo es mayor a 100 kWh pero no excede los 300 kWh, se paga una tarifa diferente por los kWh que exceden el Nivel 1.

Nivel 3: Si el consumo es mayor a 300 kWh, se aplica una tarifa aún más alta para los kWh que exceden los niveles anteriores.

Presta especial atención a cómo se calculan los cargos en cada nivel. Necesitas asegurarte de que solo se apliquen las tarifas correctas a la cantidad de kWh que corresponde a cada nivel.

def factura_electricidad():
    # Tu código y las explicaciones van aquí
    pass

if __name__ == '__main__':
    factura_electricidad()


Tarea
El código que te han proporcionado está casi completo. 
1. Entender la Lógica: Analiza la lógica detrás de los bloques if, elif, y else para ver cómo se calculan los costos. 

2. Agregar los TRES niveles de consumo utilizando un bloque if, elif, y else. Por ejemplo para el primer if, si el consumo es menor o igual a 100, algo asi:

     consumo_kwh <= 100:
        kwh_nivel1 = consumo_kwh
        cargo_nivel1 = 20.00  # tarifa fija
        kwh_nivel2 = 0
        cargo_nivel2 = 0.00
        kwh_nivel3 = 0
        cargo_nivel3 = 0.00

3. Añadir Comentarios donde sea necesario: Agrega comentarios detallados a lo largo del código para explicar cada paso, especialmente en las secciones de cálculo. Esto te ayudará a solidificar tu comprensión y a documentar tu trabajo para otros.