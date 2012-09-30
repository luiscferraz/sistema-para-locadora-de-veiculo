'''
Created on 30/09/2012

@author: Marcela Domingues
'''

class Usuario:

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha
        
    def getAtributos(self):
        login = self.getLogin()
        senha = self.getSenha()
       
        return [login, senha] 