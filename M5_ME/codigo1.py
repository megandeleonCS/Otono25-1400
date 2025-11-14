<<<<<<<< HEAD:M5_Tarea/codigo1.py
# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
(edad <= 18) and (tiene_permiso)

print("¿Puede salir solo?:", tiene_permiso)

# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso
puede_salir_2 = (es_finde) or (tiene_permiso)
print("¿Puede salir por alguna razón?:", puede_salir_2)

# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
no_tiene_permiso = not tiene_permiso
print("¿No tiene permiso?:", no_tiene_permiso)

# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 
edad = 18
puede_conducir = True
no_tiene_permiso = False
#Usando and
(edad <= 18) and (puede_conducir)
print("Puede ir a la tienda solo?:", puede_conducir)
#Usando or
no_licencia = (puede_conducir) or (no_tiene_permiso) 
print("Puede ir en el auto?:", no_tiene_permiso)
#Usando not
========
# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
(edad >= 18) and (tiene_permiso)

print("¿Puede salir solo?:", tiene_permiso)

# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso
puede_salir_2 = (es_finde) or (tiene_permiso)
print("¿Puede salir por alguna razón?:", puede_salir_2)

# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
no_tiene_permiso = not tiene_permiso
print("¿No tiene permiso?:", no_tiene_permiso)

# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 
edad = 18
puede_conducir = True
no_tiene_permiso = False
#Usando and
(edad >= 18) and (puede_conducir)
print("Puede ir a la tienda solo?:", (edad >= 18) and puede_conducir) 
#Usando or
# Cambio
no_licencia = (puede_conducir) or (no_tiene_permiso) 
print("Puede ir en el auto?:", no_tiene_permiso)
#Usando not
>>>>>>>> d513ccd34ac7045a0b4de00f5dd33852b2f043b5:M5_ME/codigo1.py
no_tiene_permiso = not no_tiene_permiso