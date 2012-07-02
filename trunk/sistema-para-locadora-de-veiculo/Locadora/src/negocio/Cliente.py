from negocio.Pessoa import * 

'''
Created on 02/07/2012

@author: Allan do Amaral
'''

class Cliente(Pessoa):
    
    def __init__(self, cpf,nome,endereco,telefone,cep,bairro,cidade,uf,email,idCliente):
        Pessoa.__init__(self, cpf, nome, endereco, telefone, cep, bairro, cidade, uf, email);
        self.__idCliente = idCliente
        
    
    def getIdCliente(self):
        return self.__idCliente    
    def setIdCliente(self,idCliente):
        self.__idCliente = idCliente       