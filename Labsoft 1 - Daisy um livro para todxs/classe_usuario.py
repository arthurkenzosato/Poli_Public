class Usuario(object):
    def __init__(self, nusp, nome, senha, area):
        self.nusp = nusp
        self.nome = nome
        self.senha = senha
        self.area = area

    def getNusp(self):
        return self.nusp

    def getNome(self):
        return self.nome

    def getSenha(self):
        return self.senha

    def getArea(self):
        return self.area
