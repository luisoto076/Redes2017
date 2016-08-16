#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
from Constants import Constants as cons
from Code import Calculator as cal
import sys

'''
Clase para la ventana de registro de usuarios
'''
class RegisterWindow(QtGui.QWidget):

    '''
        constructor
    '''
    def __init__(self ):
        super(RegisterWindow, self).__init__()
        self.initUI()


    def initUI(self):
        usr_label = QtGui.QLabel('Usuario:', self)
        usr_widget = QtGui.QLineEdit()
        pasword_label = QtGui.QLabel('Contraseña:', self)
        pasword_widget = QtGui.QLineEdit()
        pasword_widget.setEchoMode(QtGui.QLineEdit.Password)
        self.register_button = QtGui.QPushButton('Registrar')
        self.register_button.clicked.connect(lambda: self.access(usr_widget,pasword_widget))
        grid = QtGui.QGridLayout()
        grid.addWidget(usr_label, cons.ROW0,cons.COLUMN0)
        grid.addWidget(usr_widget, cons.ROW0,cons.COLUMN1)
        grid.addWidget(pasword_label, cons.ROW1,cons.COLUMN0)
        grid.addWidget(pasword_widget, cons.ROW1,cons.COLUMN1)
        grid.addWidget(self.register_button, cons.ROW2,cons.COLUMN1)
        self.setLayout(grid)
        self.setGeometry(cons.DEFAULT_POSTION_X, cons.DEFAULT_POSTION_Y, cons.WIDTH, cons.HEIGTH)
        self.setWindowTitle('Registrate')
        self.show()

    '''
        metodo que se ejecutara cuando se de clic al boton Registrar
    '''
    def access(self, usr_widget=None, pasword_widget=None):
        usr = usr_widget.text()
        psw = pasword_widget.text()
        cal.Calculator().registra(str(usr),str(psw))
        self.close()
