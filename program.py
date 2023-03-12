#program.py

sum = 1 + 2
print (sum)
print ("Muestra esto en la consola")


#Variables 
sumvar = 1 + 2
product = sumvar * 2
print (product)

#Tipos de datos 
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #String

type(can_liftoff)

#Operadores
left_side = 10
right_side = 5
division = int(left_side / right_side) # 2
print(division)
print(type(division))
 
 #Operadores aritméticos
#  Tipo	Descripción	Ejemplo
# +	Operador de suma que agrega dos valores juntos	1 + 1
# -	Operador de resta que quita el valor del lado derecho del lado izquierdo	1 - 2
# /	Operador de división que divide el lado izquierdo tantas veces como el lado derecho especifica	10 / 2
# *	Operador de multiplicación	2 * 2
 
 
#operadores de asignación
# =	x = 2
# x ahora contiene 2.
# +=	x += 2
# x incrementado en 2. Si contenía 2 antes, ahora tiene un valor de 4.
# -=	x -= 2
# x reducido en 2. Si contenía 2 antes, ahora tiene un valor de 0.
# /=	x /= 2
# x dividido por 2. Si contenía 2 antes, ahora tiene un valor de 1.
# *=	x *= 2
# x multiplicado por 2. Si contenía 2 antes, ahora tiene un valor de 4.

#Para trabajar fechas en python se importa el módulo datetime
from datetime import date
print(date.today()) #Función today perteneciente a date 


#Conversión de los datos
#Solo se puede concatenar datos del mismo tipo
print("La fecha de hoy es: " + str(date.today()))