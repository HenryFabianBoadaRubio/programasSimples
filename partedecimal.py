
#ejercicio 8
#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

import math 
n1=float(input("escriba por favor el numero del cual desea obtener su parte decimal  "))
decimal=math.modf(n1)
print("los decimales de este numero = ",decimal)