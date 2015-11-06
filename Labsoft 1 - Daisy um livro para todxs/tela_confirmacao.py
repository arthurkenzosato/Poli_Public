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

class Ui_confirmacao(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_confirmacao, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(617, 227)
        self.labelConfirmar = QtGui.QLabel(self)
        self.labelConfirmar.setGeometry(QtCore.QRect(30, 70, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelConfirmar.setFont(font)
        self.labelConfirmar.setObjectName(_fromUtf8("labelConfirmar"))
        self.botaoSIM = QtGui.QPushButton(self)
        self.botaoSIM.setGeometry(QtCore.QRect(140, 150, 161, 51))
        self.botaoSIM.setObjectName(_fromUtf8("botaoSIM"))
        self.botaoNAO = QtGui.QPushButton(self)
        self.botaoNAO.setGeometry(QtCore.QRect(320, 150, 161, 51))
        self.botaoNAO.setObjectName(_fromUtf8("botaoNAO"))

        self.setWindowTitle(_translate("self", "Confirmar", None))
        self.labelConfirmar.setText(_translate("self", u"Você tem certeza que deseja submeter esta descrição?", None))
        self.botaoSIM.setText(_translate("self", "SIM", None))
        self.botaoNAO.setText(_translate("self", u"NÃO", None))

        self.show()
        
        QtCore.QMetaObject.connectSlotsByName(self)



