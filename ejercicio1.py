# -*- coding: utf8 -*-
# Sumar una colleccion de numeros de tres formas diferentes. 

x = int(raw_input("Cuantos numeros vas a sumar?: "))

def primeraSuma(x):
	numero = 0
	for y in range(x):
		numero2 = int(raw_input("Inserta numero para sumar:"))
		numero = numero + numero2
	print numero
	pass


primeraSuma(x)