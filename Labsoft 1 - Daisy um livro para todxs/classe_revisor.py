from classe_usuario import Usuario
class Revisor(Usuario):
    def __init__(self, email, revisoes, *args, **kwargs):
        super(Revisor, self).__init__(*args, **kwargs)
        self.email = email
        self.revisoes = revisoes

#declarar um Descritor passando primeiro seus parametros, depois os parametros
#da classe Usuario: Descritor(bloqueado, pontuacao, nusp, nome, senha, area)

    def getEmail(self):
        return self.email

    def getRevisoes(self):
        return self.revisoes

    def setRevisoes(self, pont):
        self.revisoes = revisoes
    
