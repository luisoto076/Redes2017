#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel

#           Mis bibliotecas

import sys
LOGIN_WIDTH = 250
LOGIN_HEIGTH = 200
DEFAULT_POSTION_X =350
DEFAULT_POSTION_Y =350

#**************************************************
#Clase que representa la ventana de login, en donde
#se pide la ip del contacto con el que se mantendrá
#el chat.
#**************************************************
class RegisterWindow(QtGui.QWidget):

    def __init__(self ):
        super(RegisterWindow, self).__init__()
        self.initUI()


    def initUI(self):
        usr_label = QtGui.QLabel('Usuario:', self)
        usr_widget = QtGui.QLineEdit()
        pasword_label = QtGui.QLabel('Contraseña:', self)
        pasword_widget = QtGui.QLineEdit()
        pasword_widget.setEchoMode(QtGui.QLineEdit.Password)
        #Definimos el boton para llamar
        login_button = QtGui.QPushButton('Registrar')
        login_button.clicked.connect(lambda: self.access(usr_widget,pasword_widget))
        grid = QtGui.QGridLayout()
        grid.addWidget(usr_label, 0, 0)
        grid.addWidget(usr_widget, 0, 1)
        grid.addWidget(pasword_label, 1, 0)
        grid.addWidget(pasword_widget, 1, 1)
        grid.addWidget(login_button, 2, 1)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('RegistroS')
        self.show()

    def access(self, usr_widget=None, pasword_widget=None):
        contact_ip = usr_widget.text()
        print contact_ip
        self.close()
