#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
import calculadora
from Constants import Constants as cons
import sys


class ScientificCalculatorWindow(calculadora.CalculatorWindow):

    def __init__(self ):
        super(ScientificCalculatorWindow, self).__init__()
        self.initUIC()


    def initUIC(self):
        self.mod_button = QtGui.QPushButton('%')
        self.mod_button.clicked.connect(lambda: self.pressmod(self.display_widget))
        self.pow_button = QtGui.QPushButton('^')
        self.pow_button.clicked.connect(lambda: self.presspow(self.display_widget))
        self.product_button = QtGui.QPushButton('*')
        self.product_button.clicked.connect(lambda: self.pressproduct(self.display_widget))
        self.division_button = QtGui.QPushButton('/')
        self.division_button.clicked.connect(lambda: self.pressdiv(self.display_widget))
        self.grid.addWidget(self.mod_button, cons.ROW2,cons.COLUMN4)
        self.grid.addWidget(self.pow_button, cons.ROW3,cons.COLUMN4)
        self.grid.addWidget(self.product_button,cons.ROW4,cons.COLUMN3)
        self.grid.addWidget(self.division_button,cons.ROW5,cons.COLUMN3)
        self.setLayout(self.grid)
        self.setGeometry(cons.DEFAULT_POSTION_X, cons.DEFAULT_POSTION_Y, cons.WIDTH, cons.HEIGTH)
        self.setWindowTitle('Calculadora')


    '''
       metodos para conectar los botones para que escriba en el display de la calculadora 
    '''

    def pressmod(self,display_widget):
        c = display_widget.text() + "%"
        display_widget.setText(c)

    def presspow(self,display_widget):
        c = display_widget.text() + "^"
        display_widget.setText(c)

    def pressminus(self,display_widget):
        c = display_widget.text() + "-"
        display_widget.setText(c)

    def pressproduct(self,display_widget):
        c = display_widget.text() + "*"
        display_widget.setText(c)
  
    def pressdiv(self,display_widget):
        c = display_widget.text() + "/"
        display_widget.setText(c)


