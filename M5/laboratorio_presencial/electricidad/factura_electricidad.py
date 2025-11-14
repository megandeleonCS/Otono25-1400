

def factura_electricidad():
    """Calcula la factura de electricidad según niveles de consumo."""

    consumo_kwh = int(input("¿Cuántos kWh consumiste este mes? "))

    # TODO 1: Agrega una estructura condicional if/elif/else para determinar la tarifa aplicable:
    # Nivel 1: Si el consumo es de 100 kWh o menos, se aplica una tarifa fija.
    # Nivel 2: Si el consumo es mayor a 100 kWh pero no excede los 300 kWh, se paga una tarifa diferente por los kWh que exceden el Nivel 1. *.15
    # Nivel 3: Si el consumo es mayor a 300 kWh, se aplica una tarifa aún más alta para los kWh que exceden los niveles anteriores. * .25
    # # If logica va aqui
    if consumo_kwh <= 100:
        kwh_nivel1 = consumo_kwh
        cargo_nivel1 = 20.00  # tarifa fija
        kwh_nivel2 = 0
        cargo_nivel2 = 0.00
        kwh_nivel3 = 0
        cargo_nivel3 = 0.00
        
    elif consumo_kwh <= 300:
        kwh_nivel1 = 100
        cargo_nivel1 = 20.00  # tarifa fija
        kwh_nivel2 = consumo_kwh - 100
        cargo_nivel2 = kwh_nivel2 *.15
        kwh_nivel3 = 0
        cargo_nivel3 = 0.00
    
    else:
        kwh_nivel1 = 100
        cargo_nivel1 = 20.00  # tarifa fija
        kwh_nivel2 = 200
        cargo_nivel2 = kwh_nivel2 *.15
        kwh_nivel3 = consumo_kwh - 300
        cargo_nivel3 = kwh_nivel3 *.25

    # Total de la factura
    cargo_total = cargo_nivel1 + cargo_nivel2 + cargo_nivel3

    def pluralizar(kwh):
        return "kWh"  # No cambia en plural, pero se mantiene por consistencia

    # Mostrar resumen
    print("\nResumen de tu factura de electricidad:")
    print(f"Consumo total: {consumo_kwh} {pluralizar(consumo_kwh)}")
    print(f"Nivel 1 (0-100): {kwh_nivel1} {pluralizar(kwh_nivel1)}, ${cargo_nivel1:.2f}")
    print(f"Nivel 2 (101-300): {kwh_nivel2} {pluralizar(kwh_nivel2)}, ${cargo_nivel2:.2f}")
    print(f"Nivel 3 (más de 300): {kwh_nivel3} {pluralizar(kwh_nivel3)}, ${cargo_nivel3:.2f}")
    print(f"\nTotal a pagar: ${cargo_total:.2f}")

if __name__ == '__main__':
    factura_electricidad()
