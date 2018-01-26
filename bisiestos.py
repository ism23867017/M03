#coding: utf-8

year=input("Introduzca un año:")

if (year % 4 == 0 and year % 100 !=0 or year % 400 == 0):
	
	print "El año", year , "Es bisiesto"
	
else:
	
	print "El año", year , "No es bisiesto"
