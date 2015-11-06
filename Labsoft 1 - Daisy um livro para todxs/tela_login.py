# -*- coding: utf-8 -*-
import MySQLdb
from PyQt4 import QtCore, QtGui
from tela_cadastro import Ui_cadastro
from tela_semcad import Ui_semcad
from tela_senincorreta import Ui_senincorreta
from tela_descritor import Ui_self
from tela_revisor import Ui_revisor
from classe_descritor import Descritor
from classe_revisor import Revisor

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

class Ui_login(QtGui.QDialog):
    def __init__(self):
        super(Ui_login, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(487, 326)
        self.botaoOK_Cancelar = QtGui.QDialogButtonBox(self)
        self.botaoOK_Cancelar.setGeometry(QtCore.QRect(180, 230, 241, 32))
        self.botaoOK_Cancelar.setOrientation(QtCore.Qt.Horizontal)
        self.botaoOK_Cancelar.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.botaoOK_Cancelar.setObjectName(_fromUtf8("botaoOK_Cancelar"))
        self.textoLogin = QtGui.QLineEdit(self)
        self.textoLogin.setGeometry(QtCore.QRect(140, 80, 231, 27))
        self.textoLogin.setObjectName(_fromUtf8("textoself"))
        self.textoSenha = QtGui.QLineEdit(self)
        self.textoSenha.setGeometry(QtCore.QRect(140, 130, 231, 27))
        self.textoSenha.setObjectName(_fromUtf8("textoSenha"))
        self.textoSenha.setEchoMode(2)
        self.labelLogin = QtGui.QLabel(self)
        self.labelLogin.setGeometry(QtCore.QRect(50, 80, 70, 21))
        self.labelLogin.setObjectName(_fromUtf8("labelself"))
        self.labelSenha = QtGui.QLabel(self)
        self.labelSenha.setGeometry(QtCore.QRect(50, 130, 70, 21))
        self.labelSenha.setObjectName(_fromUtf8("labelSenha"))
        self.labelTitulo = QtGui.QLabel(self)
        self.labelTitulo.setGeometry(QtCore.QRect(70, 30, 391, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Narkisim"))
        font.setPointSize(16)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName(_fromUtf8("labelTitulo"))
        self.botaoDescritor = QtGui.QRadioButton(self)
        self.botaoDescritor.setGeometry(QtCore.QRect(110, 170, 124, 25))
        self.botaoDescritor.setObjectName(_fromUtf8("botaoDescritor"))
        self.botaoRevisor = QtGui.QRadioButton(self)
        self.botaoRevisor.setGeometry(QtCore.QRect(220, 170, 91, 25))
        self.botaoRevisor.setObjectName(_fromUtf8("botaoRevisor"))
        self.botaoAdmin = QtGui.QRadioButton(self)
        self.botaoAdmin.setGeometry(QtCore.QRect(310, 170, 151, 25))
        self.botaoAdmin.setObjectName(_fromUtf8("botaoAdmin"))
        self.botaoCadastrar = QtGui.QPushButton(self)
        self.botaoCadastrar.setGeometry(QtCore.QRect(70, 230, 112, 31))
        self.botaoCadastrar.setObjectName(_fromUtf8("botaoCadastrar"))

        self.setWindowTitle(_translate("self", "Efetuar Login", None))
        self.labelLogin.setText(_translate("self", "Login:", None))
        self.labelSenha.setText(_translate("self", "Senha:", None))
        self.labelTitulo.setText(_translate("self", "Daisy - Um Livro para Todxs", None))
        self.botaoDescritor.setText(_translate("self", "Descritor", None))
        self.botaoRevisor.setText(_translate("self", "Revisor", None))
        self.botaoAdmin.setText(_translate("self", "Administrador", None))
        self.botaoCadastrar.setText(_translate("self", "Cadastrar", None))

        self.show()
        
        QtCore.QObject.connect(self.botaoOK_Cancelar, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.botaoOK_Cancelar, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.botaoCadastrar.clicked.connect(self.cadastro)
        

    def cadastro(self):
        self.child_win = Ui_cadastro(self)
        self.child_win.show()

    def accept(self):
        global nusp
        nusp = self.textoLogin.text()
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        if len(self.textoSenha.text()) < 8:
            self.child_win = Ui_senincorreta(self)
            self.child_win.show()
        else:
            if self.botaoDescritor.isChecked():
                result = c.execute('SELECT NUSP FROM DESCRITOR WHERE NUSP = %s', (nusp,))
                if not result:
                    self.child_win = Ui_semcad(self)
                    self.child_win.show()
                else:
                    c.execute('SELECT SENHA FROM DESCRITOR WHERE NUSP = %s', (nusp,))
                    senha = [item[0] for item in c.fetchall()]
                    senha = senha[0]
                    if senha != self.textoSenha.text():
                        self.child_win = Ui_senincorreta(self)
                        self.child_win.show()
                    else:
                        c.execute('SELECT * FROM DESCRITOR WHERE NUSP = %s', (nusp,))
                        info = [item for item in c.fetchall()]
                        info = info[0]
                        global usuario
                        usuario = Descritor(info[3],info[4],info[0],info[1],info[2],info[5])
                        self.child_win = Ui_self(self)
                        self.child_win.show()
                        self.close()
            if self.botaoRevisor.isChecked():
                result = c.execute('SELECT NUSP FROM REVISOR WHERE NUSP = %s', (nusp,))
                if not result:
                    self.child_win = Ui_semcad(self)
                    self.child_win.show()
                else:
                    c.execute('SELECT SENHA FROM REVISOR WHERE NUSP = %s', (nusp,))
                    senha = [item[0] for item in c.fetchall()]
                    senha = senha[0]
                    if senha != self.textoSenha.text():
                        self.child_win = Ui_senincorreta(self)
                        self.child_win.show()
                    else:
                        c.execute('SELECT * FROM REVISOR WHERE NUSP = %s', (nusp,))
                        info = [item for item in c.fetchall()]
                        info = info[0]
                        global revisor
                        revisor = Revisor(info[3],info[5],info[0],info[1],info[2],info[4])
                        self.child_win = Ui_revisor(self)
                        self.child_win.show()
                        self.close()
        
        
