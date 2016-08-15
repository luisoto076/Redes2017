#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from GUI import loggin,calculadora,calculadora_cientifica
from Code import Calculator, ScientificCalculator
from Constants import *
import sys

cal = ScientificCalculator.ScientificCalculator()

def access(lw,cw):
	usr = lw.usr_widget.text()
	pasword = lw.pasword_widget.text()
	if(cal.valida(usr,pasword)):
		cw.show()
		lw.close()
	
	else:
		aviso = loggin.ErrorWindow("No tienes Acceso al sistema").exec_()

def pressequal(display_widget):
	try:
		c = cal.procesa(str(display_widget.text()))
		display_widget.setText(str(c))   
	except ZeroDivisionError as detail:
		display_widget.setText('')
		aviso = loggin.ErrorWindow("No puedes dividir entre cero").exec_()
		


# **************************************************
#  Definicion de la funcion principal
#**************************************************
def main():
    app = QtGui.QApplication(sys.argv)
    lw = loggin.LoginWindow()
    cw = calculadora_cientifica.ScientificCalculatorWindow()   
    cw.equal_button.clicked.connect(lambda: pressequal(cw.display_widget))
    lw.login_button.clicked.connect(lambda: access(lw,cw))
    mainWindow = lw
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

