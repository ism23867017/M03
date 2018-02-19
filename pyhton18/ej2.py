#coding: utf-8

x=input("Introduzca un numero:")

if x < 0:
	print "Introduzca un numero superior a 0...:"
	x=input("Introduzca un numero:")
else:
	
	
	for var in range (1,x/2+1):		###Tengo que poner un 1 para empezar el rango, sino me saldra el error este #ZeroDivisionError: integer division or modulo by zero#

		
		if (x%var==0):
			print var
