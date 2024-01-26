Algoritmo sin_titulo
	Definir num, invertir Como cadena 
	Escribir "ingrese el valor de 3 digitos que desea invertir"
	leer num
	
	Escribir "el valor ingresado fue = ",num
	invertir= ""
	para x<-3 hasta 1 con paso -1 Hacer
		
		invertir = invertir+ Subcadena(num, x ,x)
	FinPara
	
	Escribir "el resultado del numero invertido es ",invertir
FinAlgoritmo
