#coding: utf-8

limite=input("Introduzca un limite:")

x=input("Numero de juego:")

while x < limite:
	
	num=input("Numero de juego:")
	x=num+x

print "Ha llegado al limite", x
