import MySQLdb

class TextoDescritivo(object):
    def __init__(self, idtexto=None, texto=None, status=None, revisao=None, idimagem=None, nusp=None):
        self.nusp = nusp
        self.idtexto = idtexto
        self.texto = texto
        self.status = status
        self.idimagem = idimagem
        self.revisao = revisao

    def getIdtexto(self):
        return self.idtexto

    def getStatus(self):
        return self.status

    def getNusp(self):
        return self.nusp

    def getTexto(self):
        return self.texto

    def getIdimagem(self):
        return self.idimagem

    def getRevisao(self):
        return self.revisao

    def setAll(self):
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        c.execute('INSERT INTO TEXTO_DESCRITIVO VALUES (%s,%s,%s,%s,%s,%s)', (self.idtexto, self.texto, self.status, self.revisao, self.idimagem, self.nusp))
        con.commit()

    def setRevisao(self, revisao):
        self.revisao = revisao
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        c.execute('UPDATE TEXTO_DESCRITIVO SET REVISAO = %s WHERE IDIMAGEM = %s', (self.revisao, self.idimagem))
        con.commit()

    def setStatus(self, status):
        self.status = status
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        c.execute('UPDATE TEXTO_DESCRITIVO SET STATUS = %s WHERE IDIMAGEM = %s', (self.status, self.idimagem))
        con.commit()

    def destroy(self):
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        c.execute('DELETE FROM TEXTO_DESCRITIVO WHERE IDTEXTO = %s', (self.idtexto,))
        con.commit()
