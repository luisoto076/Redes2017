#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Constants import Constants as cons

class Calculator:	

	def valida(self,usr,psw):
		archivo = open("Code/Input.txt","r")
		for linea in archivo:
			log = linea.split('|')
			print log[0]+" "+log[1]+usr+" "+psw
			if usr == log[0] and psw+'\n' == log[1] :
				archivo.close()
				return True

		archivo.close()
		return False
	
	def registra(self,usr,psw):
		archivo = open("Code/Input.txt","a")
		archivo.write(usr+'|'+psw)
		archivo.close()

	def operar(self,op,a,b):
		if op == cons.PLUS :
			return a+b
		if op == cons.MINUS :
			return a-b
		return a*b

	def operador(self,cadena,i):		
		if cadena[i] == '+' :
			return cons.PLUS
		elif cadena[i] == '-':
			return cons.MINUS
		return cons.ERROR

	def procesa(self,cadena):
		i = 0
		while (0 <= (ord(cadena[i])-ord('0')) <= 9) or cadena[i] == '.' :
			i = i+1

		num1 = float(cadena[0:i])
		op = 	self.operador(cadena,i)	
		i=i+1
		j=i
		while i < len(cadena) and ( (0 <= (ord(cadena[i])-ord('0')) <= 9) or cadena[i] == '.'):
			i = i+1
		num2 = float(cadena[j:i+1])
		return self.operar(op,num1,num2)

