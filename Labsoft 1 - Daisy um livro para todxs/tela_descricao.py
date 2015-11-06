# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import tela_descritor
import MySQLdb
from classe_imagem import Imagem
from classe_textodescritivo import TextoDescritivo
from tela_confirmar_alteracao import Ui_confirmar
import tela_confirmar_alteracao
from tela_poucos_caracteres import Ui_erro

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

class Ui_descricao(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_descricao, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(1200, 689)
        self.foto = QtGui.QLabel(self)
        self.foto.setGeometry(QtCore.QRect(40, 140, 491, 491))
        self.foto.setObjectName(_fromUtf8("foto"))
        self.foto.setScaledContents(1)
        self.labelDescricao = QtGui.QLabel(self)
        self.labelDescricao.setGeometry(QtCore.QRect(530, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Narkisim"))
        font.setPointSize(20)
        self.labelDescricao.setFont(font)
        self.labelDescricao.setObjectName(_fromUtf8("labelDescricao"))
        self.caixaDescricao = QtGui.QTextEdit(self)
        self.caixaDescricao.setGeometry(QtCore.QRect(590, 140, 441, 231))
        self.caixaDescricao.setObjectName(_fromUtf8("caixaDescricao"))
        self.botaoSubmeter = QtGui.QPushButton(self)
        self.botaoSubmeter.setGeometry(QtCore.QRect(1060, 140, 112, 61))
        self.botaoSubmeter.setObjectName(_fromUtf8("botaoSubmeter"))
        self.botaoVoltar = QtGui.QPushButton(self)
        self.botaoVoltar.setGeometry(QtCore.QRect(1060, 220, 112, 61))
        self.botaoVoltar.setObjectName(_fromUtf8("botaoVoltar"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(590, 380, 271, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(590, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.caixaInfos = QtGui.QTextBrowser(self)
        self.caixaInfos.setGeometry(QtCore.QRect(590, 410, 441, 241))
        self.caixaInfos.setObjectName(_fromUtf8("caixaInfos"))

        self.setWindowTitle(_translate("self", "Tela de Descrição", None))
        self.foto.setText(_translate("self", "TextLabel", None))
        self.labelDescricao.setText(_translate("self", "Descrição", None))
        self.botaoSubmeter.setText(_translate("self", "Submeter", None))
        self.botaoVoltar.setText(_translate("self", "Voltar", None))
        self.label_2.setText(_translate("self", "Informações:", None))
        self.label_3.setText(_translate("self", "Descrição:", None))

        self.show()

        global imagem
        global usuario
        global alt
        
        QtCore.QMetaObject.connectSlotsByName(self)
        imagem = tela_descritor.lista_imagens[tela_descritor.j]
        usuario = tela_descritor.usuario
        self.foto.setPixmap(QtGui.QPixmap(str(imagem.getFoto())))
        self.caixaInfos.setText(str(imagem.getContexto()))
        self.botaoSubmeter.clicked.connect(self.submeter)
        self.botaoVoltar.clicked.connect(self.voltar)


    def submeter(self):
        texto = self.caixaDescricao.toPlainText()
        tamtexto = len(texto)
        if tamtexto >= 10:
            idimagem = str(imagem.getIdimagem())
            nusp = str(usuario.getNusp())
            status = 1
            global textodes
            textodes = TextoDescritivo(idimagem, texto, status, "", idimagem, nusp)
            self.child_win = Ui_confirmar(self)
            self.child_win.exec_()
            if tela_confirmar_alteracao.ok == 1:
                self.close()
        else:
            self.child_win = Ui_erro(self)
            self.child_win.exec_()
            
    def voltar(self):
        self.close()
