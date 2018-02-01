#coding: utf-8

import os

x=input("Introduzca un numero:")

while x%2==0:
	
	condicion=raw_input("Quiere escribir otro par S/N?: ")
	
	if condicion=="N":
		exit()
		
	if condicion=="S":
		x=input("Introduzca un numero:")

		
		
