#coding: utf-8

v1=input("Introduzca un numero entero :")

v2=input("Introduzca un numero entero mayor que el anterior: ") ##Como poner v1 envez de le texto

	
for x in xrange (v1, v2+1):

	if x%2==0:
		
		print "El numero", x , "es par."
		
	else:
		
		print "El numero", x , "es impar"

