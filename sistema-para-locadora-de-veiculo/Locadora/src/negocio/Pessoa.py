'''
Created on 25/06/2012

@author: Allan do Amaral
'''

class Pessoa(object):
    
    def __init__(self,nome,endereco,telefone,cep,bairro,cidade,uf,email):     
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__cep = cep
        self.__bairro = bairro
        self.__cidade = cidade
        self.__uf = uf
        self.__email = email

    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome
        
    def getCpf(self):
        return self.__cpf
    def setCpf(self, cpf):
        self.__cpf = cpf
        
    def getEndereco(self):
        return self.__endereco
    def setEndereco(self, endereco):
        self.__endereco = endereco
                    
    def getTelefone(self):
        return self.__telefone
    def setTelefone(self, telefone):
        self.__telefone = telefone
        
    def getCep(self):
        return self.__cep
    def setCep(self,cep):
        self.__cep = cep

    def getBairro(self):
        return self.__bairro
    def setBairro(self,bairro):
        self.__bairro = bairro

    def getCidade(self):
        return self.__cidade
    def setCidade(self,cidade):
        self.__cidade = cidade

    def getUf(self):
        return self.__uf
    def setUf(self, uf):
        self.__uf = uf

    def getEmail(self):
        return self.__email
    def setEmail(self,email):
        self.__email = email
        