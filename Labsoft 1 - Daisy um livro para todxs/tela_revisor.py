# -*- coding: utf-8 -*-
import MySQLdb
import sys
import tela_login
from tela_revisao import Ui_revisao
from classe_imagem import Imagem
from classe_revisor import Revisor
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

class Ui_revisor(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_revisor, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(1294, 617)
        self.capas = QtGui.QLabel(self)
        self.capas.setGeometry(QtCore.QRect(30, 200, 242, 321))
        self.capas.setScaledContents(1)
        self.capas.setPixmap(QtGui.QPixmap("estante.jpg"))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 170, 191, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.livros = QtGui.QListWidget(self)
        self.livros.setGeometry(QtCore.QRect(290, 200, 251, 321))
        self.livros.setObjectName(_fromUtf8("livros"))
        self.pesquisar = QtGui.QLineEdit(self)
        self.pesquisar.setGeometry(QtCore.QRect(30, 110, 471, 41))
        self.pesquisar.setText(_fromUtf8("Pesquisar"))
        self.pesquisar.setPlaceholderText(_fromUtf8(""))
        self.pesquisar.setObjectName(_fromUtf8("pesquisar"))
        self.labelTitulo = QtGui.QLabel(self)
        self.labelTitulo.setGeometry(QtCore.QRect(430, 20, 461, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Narkisim"))
        font.setPointSize(16)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName(_fromUtf8("labelTitulo"))
        self.botaoIR = QtGui.QPushButton(self)
        self.botaoIR.setGeometry(QtCore.QRect(510, 110, 81, 41))
        self.botaoIR.setObjectName(_fromUtf8("botaoIR"))
        self.imagens = QtGui.QLabel(self)
        self.imagens.setGeometry(QtCore.QRect(610, 120, 441, 311))
        self.imagens.setObjectName(_fromUtf8("imagens"))
        self.imagens.setScaledContents(1)
        self.imagens.setPixmap(QtGui.QPixmap("icon.jpg"))
        self.info = QtGui.QTextBrowser(self)
        self.info.setGeometry(QtCore.QRect(610, 440, 441, 121))
        self.info.setObjectName(_fromUtf8("info"))
        self.direita = QtGui.QCommandLinkButton(self)
        self.direita.setGeometry(QtCore.QRect(1060, 250, 51, 52))
        self.direita.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("right.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.direita.setIcon(icon)
        self.direita.setIconSize(QtCore.QSize(40, 40))
        self.direita.setObjectName(_fromUtf8("direita"))
        self.esquerda = QtGui.QCommandLinkButton(self)
        self.esquerda.setGeometry(QtCore.QRect(540, 250, 51, 52))
        self.esquerda.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("left.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.esquerda.setIcon(icon1)
        self.esquerda.setIconSize(QtCore.QSize(40, 40))
        self.esquerda.setObjectName(_fromUtf8("esquerda"))
        self.botaoRevisar = QtGui.QPushButton(self)
        self.botaoRevisar.setGeometry(QtCore.QRect(1130, 110, 141, 51))
        self.botaoRevisar.setObjectName(_fromUtf8("botaoRevisar"))
        self.botaoRevisar.setEnabled(0)
        self.botaoRevisoes = QtGui.QPushButton(self)
        self.botaoRevisoes.setGeometry(QtCore.QRect(1130, 170, 141, 51))
        self.botaoRevisoes.setObjectName(_fromUtf8("botaoRevisoes"))
        self.botaoSeguir = QtGui.QPushButton(self)
        self.botaoSeguir.setGeometry(QtCore.QRect(1130, 230, 141, 51))
        self.botaoSeguir.setObjectName(_fromUtf8("botaoSeguir"))
        self.botaoSair = QtGui.QPushButton(self)
        self.botaoSair.setGeometry(QtCore.QRect(1130, 290, 141, 51))
        self.botaoSair.setObjectName(_fromUtf8("botaoSair"))
        self.botaoSeguidas = QtGui.QPushButton(self)
        self.botaoSeguidas.setGeometry(QtCore.QRect(1130, 350, 141, 51))
        self.botaoSeguidas.setObjectName(_fromUtf8("botaoSeguidas"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(290, 170, 191, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.setWindowTitle(_translate("self", "Bem-vindo Revisor", None))
        self.label.setText(_translate("self", "Capa:", None))
        self.labelTitulo.setText(_translate("self", "Projeto Daisy - Um Livro para Todxs", None))
        self.botaoIR.setText(_translate("self", "IR", None))
        
        self.botaoRevisar.setText(_translate("self", "Revisar", None))
        self.botaoRevisoes.setText(_translate("self", "Minhas Revisões", None))
        self.botaoSeguir.setText(_translate("self", "Seguir", None))
        self.botaoSair.setText(_translate("self", "Sair", None))
        self.botaoSeguidas.setText(_translate("self", "Imagens Seguidas", None))
        self.label_3.setText(_translate("self", "Livros:", None))

        self.show()

        QtCore.QMetaObject.connectSlotsByName(self)

        self.botaoIR.clicked.connect(self.pesquisa)
        self.livros.itemDoubleClicked.connect(self.carregar)
        self.direita.clicked.connect(self.irdireita)
        self.esquerda.clicked.connect(self.iresquerda)
        self.botaoRevisar.clicked.connect(self.revisar)
        self.botaoSair.clicked.connect(self.sair)

        global revisor
        revisor = tela_login.revisor
        
    def pesquisa(self):
        self.imagens.setPixmap(QtGui.QPixmap("icon.jpg"))
        self.livros.clear()
        query = self.pesquisar.text()
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        global c
        c = con.cursor()
        c.execute('SELECT ISBN FROM LIVRO WHERE NOME = %s OR AUTOR1 = %s OR AUTOR2 = %s OR AUTOR3 = %s OR AUTOR4 = %s OR EDITORA = %s OR EDICAO = %s OR ANO = %s OR ASSUNTO = %s', (query, query,query,query,query,query,query,query,query))
        listalivros = [item[0] for item in c.fetchall()]
        for i in range (0, len(listalivros)):
            it = str(listalivros[i])
            c.execute('SELECT NOME FROM LIVRO WHERE ISBN = %s',(it,))
            result = [item[0] for item in c.fetchall()]
            self.livros.insertItem(i, "%s, %s" % (result[0], it))

    def carregar(self):
        self.info.clear()
        self.imagens.setPixmap(QtGui.QPixmap("icon.jpg"))
        nome = self.livros.currentItem().text()
        nome = nome.split(",")[1].trimmed()
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        global result
        result = c.execute('SELECT * FROM IMAGEM WHERE ISBN = %s AND STATUS = "1"', (nome,))
        global lista_imagens
        lista_imagens = []
        del lista_imagens[:]
        if result:
            row = c.fetchone()
            global j
            j = 0
            while row is not None:
                row = [item for item in row]
                imagem = Imagem(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                lista_imagens.append(imagem)
                row = c.fetchone()

            imagem = lista_imagens[0]
            self.imagens.setPixmap(QtGui.QPixmap(str(lista_imagens[0].getFoto())))
            self.info.setText(u"ID da Imagem: %s\nPágina no livro: %s\nCapítulo: %s\nContexto: %s" % (str(lista_imagens[j].getIdimagem()),str(lista_imagens[j].getPagina()),str(lista_imagens[j].getCapitulo()),str(lista_imagens[j].getContexto())))
            self.botaoRevisar.setEnabled(1)

        c.execute('SELECT CAPA FROM LIVRO WHERE ISBN = %s', (nome,))
        capa = c.fetchone()
        capa = [item for item in capa]
        capa = capa[0]
        self.capas.setPixmap(QtGui.QPixmap(str(capa)))
        
    def irdireita(self):
        if result:
            self.info.clear()
            global j
            if j == len(lista_imagens)-1:
                j = -1
            self.imagens.setPixmap(QtGui.QPixmap(str(lista_imagens[j+1].getFoto())))
            self.info.setText(u"ID da Imagem: %s\nPágina no livro: %s\nCapítulo: %s\nContexto: %s" % (str(lista_imagens[j+1].getIdimagem()),str(lista_imagens[j+1].getPagina()),str(lista_imagens[j+1].getCapitulo()),str(lista_imagens[j+1].getContexto())))                
            j+=1
    def iresquerda(self):
        if result:
            self.info.clear()
            global j
            if j == 0:
                j = len(lista_imagens)
            self.imagens.setPixmap(QtGui.QPixmap(str(lista_imagens[j-1].getFoto())))
            self.info.setText(u"ID da Imagem: %s\nPágina no livro: %s\nCapítulo: %s\nContexto: %s" % (str(lista_imagens[j-1].getIdimagem()),str(lista_imagens[j-1].getPagina()),str(lista_imagens[j-1].getCapitulo()),str(lista_imagens[j-1].getContexto())))
            j-=1

    def revisar(self):
        self.info.clear()
        self.imagens.setPixmap(QtGui.QPixmap("icon.jpg"))
        self.botaoRevisar.setEnabled(0)
        self.child_win = Ui_revisao(self)
        self.child_win.exec_()

    def sair(self):
        self.close()
