#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Constants import Constants as cons

import Calculator

'''
Clase para la funcionalidad de la calculadora cientifica
Extiende a la clase Calculator
'''
class ScientificCalculator(Calculator.Calculator):	

	'''
		Metodo que obtiene el resultado de la operacion solicitada
	 	op : el codigo de operacion
	 	a : primer operando
	 	b : segundo operando
	'''	
	def operar(self,op,a,b):
		if op == cons.PLUS :
			return a+b
		if op == cons.MINUS :
			return a-b
		if op == cons.PROD :
			return a*b
		if op == cons.DIV :
			return a/b
		if op == cons.MOD :
			return a%b
		if op == cons.POW :
			return pow(a,b)
		return a*b

	'''
		Metodo que obtiene el opcode de una operacion segun el simbolo
		que se encuentra en la posicion i de la cadena
		cadena : la expresion de la que se optendra el operador
		i: posicion del operador a examinar en la cadena
	'''
	def operador(self,cadena,i):		
		if cadena[i] == '+' :
			return cons.PLUS
		if cadena[i] == '-':
			return cons.MINUS
		if cadena[i] == '*':
			return cons.PROD
		if cadena[i] == '/':
			return cons.DIV
		if cadena[i] == '%':
			return cons.MOD
		if cadena[i] == '^':
			return cons.POW
		return cons.ERROR


