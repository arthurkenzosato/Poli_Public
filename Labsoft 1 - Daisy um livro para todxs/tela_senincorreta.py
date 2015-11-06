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

class Ui_senincorreta(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_senincorreta, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(293, 187)
        self.labelConfirmar = QtGui.QLabel(self)
        self.labelConfirmar.setGeometry(QtCore.QRect(60, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelConfirmar.setFont(font)
        self.labelConfirmar.setObjectName(_fromUtf8("labelConfirmar"))
        self.botaoOK = QtGui.QPushButton(self)
        self.botaoOK.setGeometry(QtCore.QRect(70, 90, 161, 51))
        self.botaoOK.setObjectName(_fromUtf8("botaoOK"))

        self.setWindowTitle(_translate("self", "Atenção!", None))
        self.labelConfirmar.setText(_translate("self", "Senha incorreta!", None))
        self.botaoOK.setText(_translate("self", "OK", None))

        self.show()
        
        QtCore.QMetaObject.connectSlotsByName(self)

        self.botaoOK.clicked.connect(self.fechar)

    def fechar(self):
        self.close()
