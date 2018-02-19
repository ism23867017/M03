#coding: utf-8
import os
x=input("Cuantas vueltas quieres hacer?:")
contador=0
b=0
salir = False
if x < 0:
	print "Almenos tienes que hacer una:"
	x=input("Cuantas vueltas quieres hacer?:")
else:
	
	y=input("Escriba un numero:")
	while contador<x:
		
		b=input("Escriba un numero superior: :")
		if y>b:
			contador=contador+1
			print "Escriba un numero mayor a",y," :" 
			b=input("Escriba un numero superior: :")
		else:
			print "Un numero mayor!!"
	else:
		exit()			
