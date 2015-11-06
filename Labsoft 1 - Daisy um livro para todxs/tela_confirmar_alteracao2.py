# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import tela_revisao

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

class Ui_confirmar(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_confirmar, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(641, 234)
        self.labelConfirmar = QtGui.QLabel(self)
        self.labelConfirmar.setGeometry(QtCore.QRect(20, 60, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelConfirmar.setFont(font)
        self.labelConfirmar.setObjectName(_fromUtf8("labelConfirmar"))
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(210, 160, 233, 34))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.setWindowTitle(_translate("self", "Confirmar", None))
        self.labelConfirmar.setText(_translate("self", "Confirmar descrição? Esta alteração não pode ser desfeita!", None))

        self.show()

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        
        QtCore.QMetaObject.connectSlotsByName(self)

    def accept(self):
        status = 2
        tela_revisao.texto_des.setRevisao(tela_revisao.revisao)
        tela_revisao.texto_des.setStatus(status)
        tela_revisao.imagem.setStatus(status)
        tela_revisao.descritor.addPontuacao()
        global ok
        ok = 1
        self.close()
