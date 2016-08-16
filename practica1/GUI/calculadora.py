#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
from PyQt4.QtCore import Qt
from Constants import Constants as cons

import sys

'''
Clase para implementar la interfaz grafica de una calculadora que suma y resta
'''
class CalculatorWindow(QtGui.QWidget):

    '''
	    Constructor
    '''
    def __init__(self ):
        super(CalculatorWindow, self).__init__()
        self.initUI()

    '''
	   auxiliar del constructor que agrega los elementos que componen la ventana
    '''
    def initUI(self):
        self.display_widget = QtGui.QLineEdit()
        self.display_widget.setReadOnly(True)
        self.display_widget.setAlignment(Qt.AlignRight)
        self.registra_button = QtGui.QPushButton('registrar')
        self.button1 = QtGui.QPushButton('1')
        self.button1.clicked.connect(lambda: self.press1(self.display_widget))
        self.button2 = QtGui.QPushButton('2')
        self.button2.clicked.connect(lambda: self.press2(self.display_widget))
        self.button3 = QtGui.QPushButton('3')
        self.button3.clicked.connect(lambda: self.press3(self.display_widget))
        self.button4 = QtGui.QPushButton('4')
        self.button4.clicked.connect(lambda: self.press4(self.display_widget))
        self.button5 = QtGui.QPushButton('5')
        self.button5.clicked.connect(lambda: self.press5(self.display_widget))
        self.button6 = QtGui.QPushButton('6')
        self.button6.clicked.connect(lambda: self.press6(self.display_widget))
        self.button7 = QtGui.QPushButton('7')
        self.button7.clicked.connect(lambda: self.press7(self.display_widget))
        self.button8 = QtGui.QPushButton('8')
        self.button8.clicked.connect(lambda: self.press8(self.display_widget))
        self.button9 = QtGui.QPushButton('9')
        self.button9.clicked.connect(lambda: self.press9(self.display_widget))
        self.button0 = QtGui.QPushButton('0')
        self.button0.clicked.connect(lambda: self.press0(self.display_widget))
        self.point_button = QtGui.QPushButton('.')
        self.point_button.clicked.connect(lambda: self.presspoint(self.display_widget))
        self.equal_button = QtGui.QPushButton('=')
        self.plus_button = QtGui.QPushButton('+')
        self.plus_button.clicked.connect(lambda: self.pressplus(self.display_widget))
        self.minus_button = QtGui.QPushButton('-')
        self.minus_button.clicked.connect(lambda: self.pressminus(self.display_widget))
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.display_widget,cons.ROW1,cons.ROW0,cons.ROW1,cons.COLUMN5)
        self.grid.addWidget(self.registra_button,cons.ROW0,cons.COLUMN0)
        self.grid.addWidget(self.button1,cons.ROW4,cons.COLUMN0)
        self.grid.addWidget(self.button2,cons.ROW4,cons.COLUMN1)
        self.grid.addWidget(self.button3,cons.ROW4,cons.COLUMN2)
        self.grid.addWidget(self.button4,cons.ROW3,cons.COLUMN0)
        self.grid.addWidget(self.button5,cons.ROW3,cons.COLUMN1)
        self.grid.addWidget(self.button6,cons.ROW3,cons.COLUMN2)
        self.grid.addWidget(self.button7,cons.ROW2,cons.COLUMN0)
        self.grid.addWidget(self.button8,cons.ROW2,cons.COLUMN1)
        self.grid.addWidget(self.button9,cons.ROW2,cons.COLUMN2)
        self.grid.addWidget(self.button0,cons.ROW5,cons.COLUMN0)
        self.grid.addWidget(self.point_button,cons.ROW5,cons.COLUMN1)
        self.grid.addWidget(self.equal_button,cons.ROW5,cons.COLUMN2)
        self.grid.addWidget(self.plus_button,cons.ROW2,cons.COLUMN3)
        self.grid.addWidget(self.minus_button,cons.ROW3,cons.COLUMN3)
        self.setLayout(self.grid)
        self.setGeometry(cons.DEFAULT_POSTION_X, cons.DEFAULT_POSTION_Y, cons.WIDTH, cons.HEIGTH)
        self.setWindowTitle('Calculadora')
		
    '''
      metodos para conectar los botones para que escriba en el display de la calculadora 
    '''
    def press1(self,display_widget):
        c = display_widget.text() + '1'
        display_widget.setText(c)

    def press2(self,display_widget):
        c = display_widget.text() + '2'
        display_widget.setText(c)

    def press3(self,display_widget):
        c = display_widget.text() + '3'
        display_widget.setText(c)

    def press4(self,display_widget):
        c = display_widget.text() + '4'
        display_widget.setText(c)

    def press5(self,display_widget):
        c = display_widget.text() + '5'
        display_widget.setText(c)

    def press6(self,display_widget):
        c = display_widget.text() + '6'
        display_widget.setText(c)

    def press7(self,display_widget):
        c = display_widget.text() + '7'
        display_widget.setText(c)

    def press8(self,display_widget):
        c = display_widget.text() + '8'
        display_widget.setText(c)

    def press9(self,display_widget):
        c = display_widget.text() + '9'
        display_widget.setText(c)

    def press0(self,display_widget):
        c = display_widget.text() + '0'
        display_widget.setText(c)

    def presspoint(self,display_widget):
        c = display_widget.text() + '.'
        display_widget.setText(c)

    def pressplus(self,display_widget):
        c = display_widget.text() + '+'
        display_widget.setText(c)

    def pressminus(self,display_widget):
        c = display_widget.text() + '-'
        display_widget.setText(c)

