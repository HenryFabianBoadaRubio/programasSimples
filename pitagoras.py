# Ejercicio 6
# Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
#  de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#  del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

import math
a=float(input("Ingrese el valor del cateto A \n"))
b=float(input("Ingrese el valor del cateto B \n"))
c=math.sqrt((a**2)+(b**2))
print("el cateto A es = ",a," y el cateto B es = ",b)
print("La hipotenusa de este triangulo rectangulo es = ",c)