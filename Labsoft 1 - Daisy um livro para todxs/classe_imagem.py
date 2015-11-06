import MySQLdb
class Imagem(object):
    def __init__(self, idimagem, status, pagina, capitulo, foto, contexto, isbn):
        self.idimagem = idimagem
        self.status = status
        self.pagina = pagina
        self.capitulo = capitulo
        self.isbn = isbn
        self.foto = foto
        self.contexto = contexto

    def getIdimagem(self):
        return self.idimagem

    def getStatus(self):
        return self.status

    def getPagina(self):
        return self.pagina

    def getCapitulo(self):
        return self.capitulo

    def getISBN(self):
        return self.isbn

    def getFoto(self):
        return self.foto

    def getContexto(self):
        return self.contexto
        
    def setStatus(self, status):
        self.status = status
        con = MySQLdb.connect(host='localhost', user='root', passwd='engsoft',db='test')
        c = con.cursor()
        c.execute('UPDATE IMAGEM SET STATUS = %s WHERE IDIMAGEM = %s', (self.status, self.idimagem))
        con.commit()
        
