def saludo (nombre)
 print(f"Hola, {nombre}!")
 
 saludo("Ana")
 saludo('Laura')
 

def area_rectangulo(largo, ancho):
    return largo*ancho
class gato:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        def maullar(self):
            return "Miai!"
        
tu_gato = gato ("Luna",2)
print (tu_gato.maullar())

tu_comida = comida("Ensalda", 2)
print (tu_comida,favorita ())

class Tiempo:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self._normalize()
        
    def __str__ (self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
    def _normalize(self):
        self.minutos += self.segundos //60
        self.segundos %=60
        self.horas += self.minutos // 60
        self.minutos %=60
        self.horas %=24
    def incrementar (self, horas, minutos, segundos):
        self.segundos += segundos
        self.minutos += minutos
        self.horas += horas
        self._normalize()
        return self
        
    #Todo 2
def sumar_tiempo(tiempo, horas, minutos, segundos):
        total_segundos = tiempo_a_int(tiempo) + horas + 3600+ minutos *60 + segundos
        return int_a_tiempo(total_segundos)
def tiempo_a_int(tiempo):
         return tiempo.horas*3600 + tiempo.minutos * 60 + tiempo.segundos
def int_a_tiempo(segundos):
         minutos, segundos = divmod (segundos,60 )
         horas, minutos = divmod(minutos,60)
         return Tiempo (horas, minutos, segundos)
     
mi_hora = Tiempo(14, 30, 15)
print ("Hora Inicial:", mi_hora)

nueva_hora = sumar_tiempo(mi_hora, 2, 45, 30)
print ("Nueva Hora:", nueva_hora)

mi_hora.incrementar(1, 45, 30)
print ("Hora incrementada:", mi_hora)

#mi_hora.incrementar_tiempo(3, 0, 0)
#print ("Hora despues del overflow:", mi_hora)


