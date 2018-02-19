#coding: utf-8

x=input("Cuantos numeros vas a introducir?:")
salir = False
a=0
b=0
import os

while salir == False:
	
	for aux in range (1,x+1):
		y=input("Introduzca el numero "+str(aux)+" :")
		
		if y%2==0:
			a=a+1
		else:
			b=b+1
				
	print "Hay ",a," pares, y hay",b," impares."
	exit()
			
