import MySQLdb
from classe_usuario import Usuario
class Descritor(Usuario):
    def __init__(self, bloqueado, pontuacao, *args, **kwargs):
        super(Descritor, self).__init__(*args, **kwargs)
        self.bloqueado = bloqueado
        self.pontuacao = pontuacao

#declarar um Descritor passando primeiro seus parametros, depois os parametros
#da classe Usuario: Descritor(bloqueado, pontuacao, nusp, nome, senha, area)

    def getBloqueado(self):
        return self.bloqueado

    def setBloqueado(self, bloq):
        self.bloqueado = bloq

    def getPontuacao(self):
        return self.pontuacao

    def addPontuacao(self):
        self.pontuacao = self.pontuacao + 1
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        c.execute('UPDATE DESCRITOR SET PONTUACAO = %s WHERE NUSP = %s', (self.pontuacao, self.nusp))
        con.commit()
        if self.pontuacao == 10:
            c.execute('INSERT INTO REVISOR VALUES (%s,%s,%s," ",%s,"")', (self.nusp, self.nome, self.senha, self.area))
            con.commit()
