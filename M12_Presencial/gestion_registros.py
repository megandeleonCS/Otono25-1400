"""Juntos: w = write/escribir o escribir, r = read/leer, A = appenda/anadir.
1. Reemplazar 'Megan,38,desayuno' con su nombre, edad, y su preferencia entre desayuno almuerzo, o cena.
2. Correr este codigo en su maquina local (que no tenga errores)
3. Verificar que se crea el archivo salida.txt, en el directorio actual, con sus datos.
"""
"""import os
print(os.getcwd())
# w Funcion para escribir en el archivo
def escribirDocumento(data):
    with open("salida.txt", "a", encoding="utf-8") as fileToWriteTo:
       fileToWriteTo.write(data + "\n")


# TODO 1:
# Reemplazar 'Megan,38,desayuno' con su nombre, edad, y su preferencia entre desayuno almuerzo, o cena.
miEntrada = 'Megan,38,desayuno'
escribirDocumento(miEntrada)

# TODO 2:
# a Despues de verificar el documento salida.txt, agregar 3 lineas con datos de companeros. 
def agregarAlDocumento(data):
    with open("salida.txt", "a") as fileToWriteTo:
        fileToWriteTo.write(data + "\n") 
usuario1 = "Enrique,35,almuerzo"
usuario2 = "Brandy,18,cena"
usuario3 = "Angelica,32,desayuno"
agregarAlDocumento(usuario1)
agregarAlDocumento(usuario2)
agregarAlDocumento(usuario3)

#agregarAlDocumento("Angelica,21,almuerzo")"""

# TODO 3: 
# r 

"""def leerDocumento():
    with open("salida.txt", "r") as fileToReadFrom:
        contenido = fileToReadFrom.read()
        print(contenido)
# leerDocumento()"""

import csv

with open("M12_Presencial/informacion.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        print(linea["cantante"])