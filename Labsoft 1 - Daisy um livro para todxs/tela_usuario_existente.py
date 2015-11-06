# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class usuario_existente(QtGui.QDialog):
    def __init__(self, parent=None):
        super(usuario_existente, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(479, 177)
        self.botaoOK = QtGui.QPushButton(self)
        self.botaoOK.setGeometry(QtCore.QRect(190, 120, 112, 34))
        self.botaoOK.setObjectName(_fromUtf8("botaoOK"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 70, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.setWindowTitle(_translate("self", "Atenção!", None))
        self.botaoOK.setText(_translate("self", "OK", None))
        self.label.setText(_translate("self", "Já existe um usuário cadastrado neste NUSP!", None))
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()
        self.botaoOK.clicked.connect(self.fechar)

    def fechar(self):
        self.close()
