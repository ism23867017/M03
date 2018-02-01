#coding: utf-8
import os

x=input("Escriba un numero:")

y=input("Escriba ahora un numero mucho mas mayor:")

cont=0
while x<y and y>x:
	
	numero=input("Escriba un numero entre el rango:")
	
	if numero >= x and numero <=y:
	
		cont=cont+1
	
		
	
	else:
		
		if numero <x or numero>y:
			print "Has introduzido" ,cont, "numeros correctos."
			exit()
