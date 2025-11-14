#1Pidiendo saludo
#def saludo(nombre):
 #   print(f"Hola, {nombre}!")

#saludo("Megan")
#saludo("Ana")

#2Calculando el área de un rectángulo

def area_rectangulo(largo, ancho):
    return largo * ancho
largo = int(input("Ingrese el largo del rectángulo: "))
ancho = int(input("Ingrese el ancho del rectángulo: "))
resultado = area_rectangulo(largo, ancho)
print(f"El área del rectángulo es: {resultado}")

#3 Class
class Gato:
    #Funcion requerida
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def maullar(self):
        return"Miau!"
#Crear objectos
tu_gato = Gato("Luna",2)
mi_gato = Gato("Simba",3)

print(tu_gato.maullar())

#4 Clase propia
class coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        return "El coche ha arrancado."
mi_coche = coche("Toyota", "Corolla", 2020)
print(mi_coche.arrancar())        

#5 Tiempo
#TODO1 y 3Crear la clase Tiempo con atributos horas, minutos y segundos
class Tiempo:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self._normalize()

    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
    
    def _normalize(self):
        self.minutos += self.segundos // 60
        self.segundos = self.segundos % 60
        self.horas += self.minutos // 60
        self.minutos = self.minutos % 60
        self.horas = self.horas % 24 

    def incrementar(self, horas=0, minutos=0, segundos=0):
        self.segundos += segundos
        self.minutos += minutos
        self.horas += horas
        self._normalize()
        return self

#TODO2 Crear una funcion para sumar horas minutos y segundos
#convirtiendo tiempo origianal a los segundos
#convertir el total de segundos a un objecto Tiempo
def tiempo_a_int(tiempo):
        return tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos

def int_a_tiempo(segundos):
        minutos, segundos = divmod(segundos, 60)
        horas, minutos = divmod(minutos, 60)
        return Tiempo(horas, minutos, segundos)

def sumar_tiempo(tiempo, horas, minutos, segundos):
        total_segundos = tiempo_a_int(tiempo) + horas * 3600 + minutos * 60 + segundos
        return int_a_tiempo(total_segundos)

mi_hora = Tiempo(14, 30, 15)
print("Hora original:", mi_hora)

#TODO3 Nueva hora despues de sumar
nueva_hora = sumar_tiempo(mi_hora, 2, 45, 50)
print("Nueva hora:", nueva_hora)
hora_incrementada = mi_hora.incrementar(2, 45, 50)
print("Hora incrementada:", hora_incrementada)
mi_hora.incrementar(1, 20, 30)
print("Hora despues del overflow:", mi_hora)

