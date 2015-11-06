# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

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

class Ui_erro_cad(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_erro_cad, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(687, 180)
        self.botaoOK = QtGui.QPushButton(self)
        self.botaoOK.setGeometry(QtCore.QRect(280, 120, 112, 34))
        self.botaoOK.setObjectName(_fromUtf8("botaoOK"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 50, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.setWindowTitle(_translate("self", "Atenção!", None))
        self.botaoOK.setText(_translate("self", "OK", None))
        self.label.setText(_translate("self", "Não foi possível completar a requisição, ", None))
        self.label_2.setText(_translate("self", "verifique se todos os campos foram devidamente preenchidos", None))

        self.show()
        
        QtCore.QMetaObject.connectSlotsByName(self)
        self.botaoOK.clicked.connect(self.fechar)

    def fechar(self):
        self.close()

