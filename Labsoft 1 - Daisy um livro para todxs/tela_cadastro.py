# -*- coding: utf-8 -*-
import MySQLdb
import sys
from tela_usuario_existente import usuario_existente
from tela_senha_incomp import senha_incomp
from tela_cad_sucesso import sucesso
from tela_erro_cad import Ui_erro_cad
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

class Ui_cadastro(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_cadastro, self).__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(593, 415)
        self.labelNome = QtGui.QLabel(self)
        self.labelNome.setGeometry(QtCore.QRect(20, 110, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.labelNome.setFont(font)
        self.labelNome.setObjectName(_fromUtf8("labelNome"))
        self.labelArea = QtGui.QLabel(self)
        self.labelArea.setGeometry(QtCore.QRect(20, 190, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.labelArea.setFont(font)
        self.labelArea.setObjectName(_fromUtf8("labelArea"))
        self.labelSenha = QtGui.QLabel(self)
        self.labelSenha.setGeometry(QtCore.QRect(20, 230, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.labelSenha.setFont(font)
        self.labelSenha.setObjectName(_fromUtf8("labelSenha"))
        self.labelRepetir = QtGui.QLabel(self)
        self.labelRepetir.setGeometry(QtCore.QRect(20, 270, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.labelRepetir.setFont(font)
        self.labelRepetir.setObjectName(_fromUtf8("labelRepetir"))
        self.labelNUSP = QtGui.QLabel(self)
        self.labelNUSP.setGeometry(QtCore.QRect(20, 150, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        self.labelNUSP.setFont(font)
        self.labelNUSP.setObjectName(_fromUtf8("labelNUSP"))
        self.nome = QtGui.QLineEdit(self)
        self.nome.setGeometry(QtCore.QRect(180, 110, 391, 27))
        self.nome.setObjectName(_fromUtf8("nome"))
        self.nome.setText(_fromUtf8("Digite seu Nome"))
        self.nusp = QtGui.QLineEdit(self)
        self.nusp.setGeometry(QtCore.QRect(180, 150, 391, 27))
        self.nusp.setObjectName(_fromUtf8("nusp"))
        self.nusp.setText(_fromUtf8("Digite seu NUSP"))
        self.area = QtGui.QLineEdit(self)
        self.area.setGeometry(QtCore.QRect(180, 190, 391, 27))
        self.area.setObjectName(_fromUtf8("login"))
        self.area.setText(_fromUtf8("Digite sua Área de Estudo"))
        self.senha = QtGui.QLineEdit(self)
        self.senha.setGeometry(QtCore.QRect(180, 230, 391, 27))
        self.senha.setObjectName(_fromUtf8("senha"))
        self.senha.setEchoMode(2)
        self.repetirSenha = QtGui.QLineEdit(self)
        self.repetirSenha.setGeometry(QtCore.QRect(180, 270, 391, 27))
        self.repetirSenha.setObjectName(_fromUtf8("repetirSenha"))
        self.repetirSenha.setEchoMode(2)
        self.botaoEnviar = QtGui.QPushButton(self)
        self.botaoEnviar.setGeometry(QtCore.QRect(230, 320, 112, 34))
        self.botaoEnviar.setObjectName(_fromUtf8("botaoEnviar"))
        self.botaoCancelar = QtGui.QPushButton(self)
        self.botaoCancelar.setGeometry(QtCore.QRect(350, 320, 112, 34))
        self.botaoCancelar.setObjectName(_fromUtf8("botaoCancelar"))
        self.labelCadastro = QtGui.QLabel(self)
        self.labelCadastro.setGeometry(QtCore.QRect(240, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Narkisim"))
        font.setPointSize(16)
        self.labelCadastro.setFont(font)
        self.labelCadastro.setObjectName(_fromUtf8("labelCadastro"))


        self.setWindowTitle(_translate("self", "Cadastrar", None))
        self.labelNome.setText(_translate("self", "Nome:", None))
        self.labelArea.setText(_translate(u"self", "Área:", None))
        self.labelSenha.setText(_translate("self", u"Senha (8 dígitos):", None))
        self.labelRepetir.setText(_translate("self", "Repetir senha:", None))
        self.labelNUSP.setText(_translate("self", "NUSP:", None))
        self.botaoEnviar.setText(_translate("self", "Enviar", None))
        self.botaoCancelar.setText(_translate("self", "Cancelar", None))
        self.labelCadastro.setText(_translate("self", "Cadastro", None))

        self.show()
        
        QtCore.QMetaObject.connectSlotsByName(self)

        self.botaoEnviar.clicked.connect(self.enviar)
        self.botaoCancelar.clicked.connect(self.fechar)


    def enviar(self):
        nome = self.nome.text()
        nusp = self.nusp.text()
        senha = self.senha.text()
        repsen = self.repetirSenha.text()
        area = self.area.text()
        if len(senha) > 7 and len(nome) > 3 and len(nusp) > 4 and len(area) > 3:
            if senha != repsen:
                #As senhas digitadas são incompatíveis - chama uma tela de aviso
                self.child_win = senha_incomp(self)
                self.child_win.show()
            else:
                con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
                c = con.cursor()
                resultado = c.execute('SELECT NUSP FROM DESCRITOR WHERE NUSP = %s', (nusp,))
                if resultado:
                    #Já existe um usuário cadastrado neste NUSP - chama uma tela de aviso
                    self.child_win = usuario_existente(self)
                    self.child_win.show()
                else:
                    try:
                        c.execute('INSERT INTO DESCRITOR VALUES (%s,%s,%s,"0","0",%s,"")', (nusp, nome, senha, area))
                        con.commit()
                        #Cadastro efetuado com sucesso! - chama uma tela de aviso
                        self.child_win = sucesso(self)
                        self.child_win.show()
                        self.close()
                    except:
                        print(u"Não foi possível terminar a operação requisitada, tente novamente mais tarde")
                        exit
        else:
            self.child_win = Ui_erro_cad(self)
            self.child_win.show()
    def fechar(self):
        self.close()
