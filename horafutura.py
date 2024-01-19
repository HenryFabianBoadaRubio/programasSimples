# Ejercicio 7
# Escriba un programa que pregunte al usuario la hora 
# actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

from os import system
system("clear")

actualH=float(input("Ingrese la hora actual\n"))
futuraH=int(input("ingrese el numero de horas a sumar\n"))
hfinal=0

for i in range(24):
    hfinal=(actualH+futuraH)%24
print("la hora que sera dentro de =",futuraH, "H sera =",round(hfinal,2))