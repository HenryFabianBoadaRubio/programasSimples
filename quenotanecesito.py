#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
#El promedio del ramo se calcula con la siguiente formula.
#Donde NC
 #es el promedio de certámenes, NL
 #el promedio de laboratorio y NF
 #la nota final.

#Escriba un programa que pregunte al usuario las notas
#de los dos primeros certamen y la nota de laboratorio, y
#muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

C1= int(input("ingrese la nota del primer certamen\n"))
C2=int(input("ingrese la nota del segundo certamen\n"))
NL=int(input("ingrese la nota del laboratorio\n"))
NF=59.5
NC=(NF-(NL*0.3))/0.7
C3 =(3*NC)-(C1-C2)
print("la nota que necesita para el tercer certamen es ",C3)