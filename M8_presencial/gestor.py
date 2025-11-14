# Programa para gestionar las notas de los estudiantes

def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Agregar estudiante")
    print("2. Mostrar todos")
    print("3. Salir")

def calcular_promedio(lista_notas):
    if len(lista_notas) == 0:
        return None
    suma = 0
    for nota in lista_notas:
        suma += nota
    return suma / len(lista_notas)

def main():
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            notas = []
            for i in range(3):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota {i+1} (0-10): "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("Error: ingresa un número válido entre 0 y 10.")
                    except ValueError:
                        print("Ingresa un número válido.")

            promedio = calcular_promedio(notas)
            aprobado = False
            if promedio is not None and promedio >= 6 and all(n >= 4 for n in notas[:3]):
                aprobado = True

            estudiante = {
                "nombre": nombre,
                "notas": notas,
                "promedio": promedio,
                "aprobado": aprobado
            }
            estudiantes.append(estudiante)
            print(f"\nEstudiante {nombre} agregado correctamente.")

        elif opcion == "2":
            print("\n=== LISTA DE ESTUDIANTES ===")
            for est in estudiantes:
                estado = "Aprobado" if est["aprobado"] else "Reprobado"
                print(f"{est['nombre']} - Promedio: {est['promedio']:.2f} - {estado}")
                print(f"  Primeras dos notas: {est['notas'][:2]}")  
        elif opcion == "3":
                        # Eliminar estudiante por nombre
            nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
            encontrado = False
            for est in estudiantes:
                if est["nombre"].lower() == nombre_eliminar.lower():
                    estudiantes.remove(est)
                    print(f"Estudiante {nombre_eliminar} eliminado correctamente.")
                    encontrado = True
                    break
            if not encontrado:
                print("Estudiante no encontrado.")
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

main()
