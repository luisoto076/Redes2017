#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
from Constants import Constants as cons

import sys
#**************************************************
#Clase que representa la ventana de login, en donde
#se pide la ip del contacto con el que se mantendrá
#el chat.
#**************************************************
class LoginWindow(QtGui.QWidget):

    def __init__(self ):
        super(LoginWindow, self).__init__()
        self.initUI()


    def initUI(self):
        self.usr_label = QtGui.QLabel('Usuario:', self)
        self.usr_widget = QtGui.QLineEdit()
        self.pasword_label = QtGui.QLabel('Contraseña:', self)
        self.pasword_widget = QtGui.QLineEdit()
        self.pasword_widget.setEchoMode(QtGui.QLineEdit.Password)
        #Definimos el boton para llamar
        self.login_button = QtGui.QPushButton('Acceder')
        #login_button.clicked.connect(lambda: self.access(usr_widget,pasword_widget))
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.usr_label, 0, 0)
        self.grid.addWidget(self.usr_widget, 0, 1)
        self.grid.addWidget(self.pasword_label, 1, 0)
        self.grid.addWidget(self.pasword_widget, 1, 1)
        self.grid.addWidget(self.login_button, 2, 1)
        self.setLayout(self.grid)
        self.setGeometry(cons.DEFAULT_POSTION_X, cons.DEFAULT_POSTION_Y, cons.WIDTH, cons.HEIGTH)
        self.setWindowTitle('Identificate')
        self.show()

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

