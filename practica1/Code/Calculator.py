#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Constants import Constants as cons

'''
Clase para implementar la funcionalidad de una calculadora
que solo realiza sumas y restas
'''
class Calculator:

	'''
		Codifica la cadena que se le pasa como argumento pasando cada caracter a su respectivo
   	en codigo asccii mas 5
		cadena: la cadena a codificar
	'''
	def encode(self,cadena):
		i = cons.INICIO
		s = ''		
		while i < len(cadena):
			if(cadena[i] == '\n'):
				return s+'\n'
			s = s + str(chr(ord(cadena[i]) + 5))
			i = i+1
		return s

	'''
		indica si un usuario y pasword estan en el archivo codificado Input.txt
		usr: la cadena con el usuario
		psw: la cadena con el pasword
	'''
	def valida(self,usr,psw):
		archivo = open("Code/Input.txt","r")
		eusr = self.encode(usr)
		epsw = self.encode(psw)	
		for linea in archivo:
			log = linea.split('|')
			if eusr == log[cons.INDUSUARIO] and epsw+'\n' == log[cons.INDPASWORD] :
				archivo.close()
				return True

		archivo.close()
		return False

	'''
		guarda un usuario y pasword codificados en el archivo Input.txt 
		usr: la cadena con el usuario
		psw: la cadena con el pasword
	'''
	def registra(self,usr,psw):
		archivo = open("Code/Input.txt","a")
		i = cons.INICIO
		eusr = self.encode(usr)
		epsw = self.encode(psw)
		archivo.write(eusr+'|'+epsw+'\n')
		archivo.close()

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
		elif cadena[i] == '-':
			return cons.MINUS
		return cons.ERROR

	'''
		obtiene los elementos que conforman una expresion de la calculadora, los dos operandos, y 
		la evalua. Regresa el valor de la evaluacion
		cadena: la cadena que contiene la expresion
	'''
	def procesa(self,cadena):
		i = cons.INICIO
		while (0 <= (ord(cadena[i])-ord('0')) <= 9) or cadena[i] == '.' :
			i = i+1

		num1 = float(cadena[cons.INICIO:i])
		op = 	self.operador(cadena,i)	
		i=i+1
		j=i
		while i < len(cadena) and ( (0 <= (ord(cadena[i])-ord('0')) <= 9) or cadena[i] == '.'):
			i = i+1
		num2 = float(cadena[j:i+1])
		return self.operar(op,num1,num2)

