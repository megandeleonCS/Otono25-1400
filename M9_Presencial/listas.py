#Parte 1: Creación y acceso a listas
estalista = ["manzana", "banana", "cereza", "durazno", "pera", "durazno", "kiwi", "mango"]
print(estalista)
print(type(estalista))
print(len(estalista))
print(estalista[1])
print(estalista[-2])
print(estalista[2:5])
print(estalista[:4])
print(estalista[3:])
#Parte 2: Modificación de listas
milista = list(("manzana", "banana", "cereza", "durazno"))
for fruta in milista:
    print(fruta)
#Diccionario parte 3
mi_diccionario = {
    "marca": "Ford",
"modelo": "Mustang",
"año": 1964}
print(mi_diccionario)
#Parte 4 : Tuplas
mi_tupla = tuple(("manzana", "banana", "cereza"))
print(mi_tupla)
