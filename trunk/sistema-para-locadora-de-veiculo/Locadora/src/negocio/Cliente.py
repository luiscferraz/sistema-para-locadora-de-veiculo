# -*- coding: latin-1 -*-
from negocio.Pessoa import * 

'''
Created on 02/07/2012

@author: Allan do Amaral
'''

class Cliente(Pessoa):
    
    def __init__(self, cpf,nome,endereco,telefone,cep,bairro,cidade,uf,email):
        Pessoa.__init__(self, cpf, nome, endereco, telefone, cep, bairro, cidade, uf, email);
        self.__idCliente = None
        
    
    def getIdCliente(self):
        return self.__idCliente    
    def setIdCliente(self,idCliente):
        self.__idCliente = idCliente     
        
    def getAtributos(self):
        cpf = self.getCpf()
        nome = self.getNome()
        endereco = self.getEndereco()
        telefone = self.getTelefone()
        cep = self.getCep()
        bairro = self.getBairro()
        cidade = self.getCidade()
        uf = self.getUf()
        email = self.getEmail()
       
        return [nome , endereco, telefone , cep , bairro , cidade, uf, email, cpf]  
    
    def toString(self):
        print "\nId: %d"  %self.getIdCliente() + \
            "\nCPF: " + self.getCpf() + \
            "\nNome: " + self.getNome() + \
            "\nEndereço: " + self.getEndereco() + \
            "\nTelefone: " + self.getTelefone() + \
            "\nCEP: " + self.getCep() + \
            "\nBairro: " + self.getBairro() + \
            "\nCidade: " + self.getCidade() + \
            "\nUF: " + self.getUf() + \
            "\nE-mail: " + self.getEmail()
            