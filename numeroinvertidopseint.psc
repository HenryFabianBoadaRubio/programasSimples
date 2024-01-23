Algoritmo numeroinvertido
	Definir num, invertir Como cadena 
	Escribir "ingrese el valor de 3 digitos que desea invertir"
	leer num
	
	Escribir "el valor ingresado fue = ",num
	invertir= ""
	para i desde 1 hasta Longitud(num) Con Paso 1
		invertir = invertir+ Subcadena(num,longitud(num)-i+1,1)
	FinPara
	
	Escribir "el resultado del numero invertido es ",invertir
FinAlgoritmo
