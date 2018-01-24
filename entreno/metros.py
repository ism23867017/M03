#coding: utf-8

var=input("Introduzca x metros:")
demanda=raw_input("Introduzca el tipo de conversor:")

if demanda == 'mm':
	cent=var*1000
	print "Son", cent , "milimetros"

if demanda == 'cm':
	cent=var*100
	print "Son", cent , "centimetros"

if demanda == 'Km':
	cent=var/1000
	print "Son", cent , "kilometros"

