#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
from Constants import Constants as cons
import sys

'''
clase para la ventana de longin de la calculadora
'''
class LoginWindow(QtGui.QWidget):

    def __init__(self ):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):
        self.usr_label = QtGui.QLabel('Usuario:', self)
        self.usr_widget = QtGui.QLineEdit()
        self.pasword_label = QtGui.QLabel('Pasword:', self)
        self.pasword_widget = QtGui.QLineEdit()
        self.pasword_widget.setEchoMode(QtGui.QLineEdit.Password)
        #Definimos el boton para llamar
        self.login_button = QtGui.QPushButton('Acceder')
        #login_button.clicked.connect(lambda: self.access(usr_widget,pasword_widget))
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.usr_label, cons.ROW0,cons.COLUMN0)
        self.grid.addWidget(self.usr_widget, cons.ROW0,cons.COLUMN1)
        self.grid.addWidget(self.pasword_label, cons.ROW1,cons.COLUMN0)
        self.grid.addWidget(self.pasword_widget, cons.ROW1,cons.COLUMN1)
        self.grid.addWidget(self.login_button, cons.ROW2,cons.COLUMN1)
        self.setLayout(self.grid)
        self.setGeometry(cons.DEFAULT_POSTION_X, cons.DEFAULT_POSTION_Y, cons.WIDTH, cons.HEIGTH)
        self.setWindowTitle('Identificate')
        self.show()

'''
Clase para ventanas de error
'''
class ErrorWindow(QtGui.QDialog):

    def __init__(self, mensaje, parent=None):
        QtGui.QDialog.__init__(self, parent)
        contenedor = QtGui.QVBoxLayout()
        self.setLayout(contenedor)
        error_label = QtGui.QLabel(mensaje, self)
        btnSalir = QtGui.QPushButton("Salir",None)
        contenedor.addWidget(error_label)
        contenedor.addWidget(btnSalir)
        self.setWindowTitle("Error!")
        self.connect(btnSalir, QtCore.SIGNAL("clicked()"), self.salir)
 
    def salir(self):
        self.close()

