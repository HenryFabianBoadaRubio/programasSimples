# Ejercicio 5
# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

num=input("ingrese un numero de 3 digitos para invetir su sentido.\n")
invertir=""
print("el valor ingresado es = ",num)
for i in range(len(num)):
 invertir += num[-(i+1)]
print("el numero resultante luego de invertir su sentido es= ",invertir)