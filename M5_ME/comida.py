"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""

# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print("Bienvenidos al programa de comidas de Latinoamerica")
# TODO #2:
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.
print("\nEstas son las opciones que tenemos hoy")
print("- tacos")
print("- pupusas")
print("- arepas")
print("- ceviche")
print("- empanadas")
# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
comida = input("\nPor favor escribe el nombre de la comida de la lista que quieres saber")

# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.
comida = comida.lower()

# TODO #5:
# Usa una estructura if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.
if comida =="tacos":
    print(f"Excelente! Los {comida} son de Mexico y son muy ricos")
elif comida =="pupusas":
    print(f"Las {comida} son muy deliciosas y son de El Salvador")
elif comida =="arepas":
    print(f"Me gustan mucho las {comida} y son de Venezuela y Colombia")
elif comida =="ceviche":
    print(f"Muy buena eleccion {comida} es de Peru muy delicioso") 
elif comida =="empanadas":
    print(f"Muy ricas las {comida} que son de Espana")
else:
    print("Lo sentimos esa comida no esta disponible")               


## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""
