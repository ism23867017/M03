#coding: utf-8

entero=input("Introduzca un numero: ") 
divisor=2
salir = False

while salir == False:
	
	if entero%divisor==0:
		contador=divisor
		entero=entero/divisor
		print "Dividiendo," ,entero,"/",divisor
	else:
		divisor=divisor+1
			
		if entero==divisor:
			salir = True
			print "Dividiendo," ,entero,"/",divisor

			print "Saliendo"

