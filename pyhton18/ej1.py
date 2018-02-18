#coding: utf-8
import os
x=input("Introduzca un valor:")
y=input("Introduzca un valor superior:")

salir = False

while salir == False:

	for aux in range (x,y+1):
	
		if aux %2==0:
			print "El numero", aux, "es par."
		
		else:
			print "El numero", aux, "es impar."

	exit()


