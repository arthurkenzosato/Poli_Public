# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import tela_revisor
import MySQLdb
from classe_imagem import Imagem
from classe_textodescritivo import TextoDescritivo
from tela_confirmar_alteracao2 import Ui_confirmar
import tela_confirmar_alteracao2
from classe_descritor import Descritor
from classe_revisor import Revisor
from tela_certeza import Ui_certeza

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

class Ui_revisao(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_revisao, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(1200, 689)
        self.foto = QtGui.QLabel(self)
        self.foto.setGeometry(QtCore.QRect(40, 140, 491, 491))
        self.foto.setObjectName(_fromUtf8("foto"))
        self.foto.setScaledContents(1)
        self.labelRevisao = QtGui.QLabel(self)
        self.labelRevisao.setGeometry(QtCore.QRect(530, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Narkisim"))
        font.setPointSize(20)
        self.labelRevisao.setFont(font)
        self.labelRevisao.setObjectName(_fromUtf8("labelRevisao"))
        self.caixaDescricao = QtGui.QTextEdit(self)
        self.caixaDescricao.setGeometry(QtCore.QRect(590, 140, 441, 231))
        self.caixaDescricao.setObjectName(_fromUtf8("caixaDescricao"))
        self.caixaComentarios = QtGui.QTextEdit(self)
        self.caixaComentarios.setGeometry(QtCore.QRect(590, 410, 441, 231))
        self.caixaComentarios.setObjectName(_fromUtf8("caixaComentarios"))
        self.botaoAceitar = QtGui.QPushButton(self)
        self.botaoAceitar.setGeometry(QtCore.QRect(1060, 140, 112, 61))
        self.botaoAceitar.setObjectName(_fromUtf8("botaoAceitar"))
        self.botaoRecusar = QtGui.QPushButton(self)
        self.botaoRecusar.setGeometry(QtCore.QRect(1060, 220, 112, 61))
        self.botaoRecusar.setObjectName(_fromUtf8("botaoRecusar"))
        self.botaoBloquear = QtGui.QPushButton(self)
        self.botaoBloquear.setGeometry(QtCore.QRect(1060, 300, 112, 61))
        self.botaoBloquear.setObjectName(_fromUtf8("botaoBloquear"))
        self.botaoVoltar = QtGui.QPushButton(self)
        self.botaoVoltar.setGeometry(QtCore.QRect(1060, 380, 112, 61))
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

        

        self.setWindowTitle(_translate("self", "Tela de Revisão", None))
        self.foto.setText(_translate("self", "TextLabel", None))
        self.labelRevisao.setText(_translate("self", "Revisão", None))
        self.botaoAceitar.setText(_translate("self", "Aceitar", None))
        self.botaoRecusar.setText(_translate("self", "Recusar", None))
        self.botaoBloquear.setText(_translate("self", "Bloquear", None))
        self.botaoVoltar.setText(_translate("self", "Voltar", None))
        self.label_2.setText(_translate("self", "Faça aqui seus comentários:", None))
        self.label_3.setText(_translate("self", "Descrição:", None))

        self.show()

        global imagem
        global revisor
        global descritor
        global texto_des
        
        QtCore.QMetaObject.connectSlotsByName(self)

        imagem = tela_revisor.lista_imagens[tela_revisor.j]
        revisor = tela_revisor.revisor
        self.foto.setPixmap(QtGui.QPixmap(str(imagem.getFoto())))
        idimagem = imagem.getIdimagem()
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        c.execute('SELECT * FROM TEXTO_DESCRITIVO WHERE IDIMAGEM = %s', (idimagem,))
        texto_des = [item for item in c.fetchall()]
        texto_des = texto_des[0]
        texto_des = TextoDescritivo(texto_des[0],texto_des[1],texto_des[2],texto_des[3],texto_des[4],texto_des[5])
        nusp = texto_des.getNusp()
        texto = texto_des.getTexto()
        self.caixaDescricao.setText(texto)
        c.execute('SELECT * FROM DESCRITOR WHERE NUSP = %s', (nusp,))
        info = [item for item in c.fetchall()]
        info = info[0]
        descritor = Descritor(info[3],info[4],info[0],info[1],info[2],info[5])

        self.botaoAceitar.clicked.connect(self.aceitar)
        self.botaoVoltar.clicked.connect(self.voltar)
        self.botaoRecusar.clicked.connect(self.recusar)

    def aceitar(self):
        global revisao
        revisao = self.caixaComentarios.toPlainText()
        self.child_win = Ui_confirmar(self)
        self.child_win.exec_()
        if tela_confirmar_alteracao2.ok == 1:
            self.close()
        
    def recusar(self):
        self.child_win = Ui_certeza(self)
        self.child_win.exec_()
        if tela_certeza.ok == 1:
            self.close()

    def voltar(self):
        self.close()
