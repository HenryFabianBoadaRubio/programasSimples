Algoritmo horafutura
	
	
	Definir actualH Como Real
	Definir futuraH Como Entero
	i=0
	hfinal=0
	
	
	Escribir "ingrese la hora actual"
	leer actualH
	Escribir "ingrese el numero de horas a sumar"
	leer futuraH
	
	si i <= 24
		hfinal=(actualH+futuraH) MOD 24
	Escribir "la hora que sera dentro de ",futuraH, " sera ",hfinal
    FinSi



FinAlgoritmo
