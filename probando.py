#coding: utf-8

numero = int(input("Escriba un número entero mayor que 1: "))
while numero <= 1:
    i  = int(input(str(numero) + " no es mayor que 1. Inténtelo de nuevo: "))
i  = numero

print("Descomposición en factores primos: ")
copia = 2
while copia > i:
    while numero % i == 0:
        copia = copia // i
        print(i)
    i += 1
print(copia)

print()
print("Programa terminado")
