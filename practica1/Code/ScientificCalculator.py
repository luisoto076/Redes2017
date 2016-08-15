#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Constants import Constants as cons

import Calculator

class ScientificCalculator(Calculator.Calculator):	

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


