#coding: utf-8

y=input("Numero de vueltas deseado:")
x=0
var_total=0
while x<y:
	num=input("Introduzca un numero:")
	
	if num>0:
		x=x+1
	var_total=var_total+num

print var_total
