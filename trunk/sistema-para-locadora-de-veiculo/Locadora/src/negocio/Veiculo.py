# -*- coding: latin-1 -*-

'''
Created on 05/07/2012

@author: Marcela Domingues
'''

class Veiculo:
    
    def __init__(self,placa,marca,cor,modelo):
        self.__placa = placa
        self.__marca = marca
        self.__cor = cor
        self.__modelo = modelo
        self.__disponivel = True
        self.__quilometragemAtual = None
        self.__numeroDelocacoes = None
        self.__idVeiculo = None
        self.__idLocacao = None
        self.__idCodTipoVeiculo = None
        
    def getPlaca(self):
        return self.__placa
    def setPlaca(self, placa):
        self.__placa = placa
        
    def getMarca(self):
        return self.__marca
    def setMarca(self, marca):
        self.__marca = marca
        
    def getCor(self):
        return self.__cor
    def setCor(self, cor):
        self.__cor = cor
        
    def getModelo(self):
        return self.__modelo
    def setModelo(self, modelo):
        self.__modelo = modelo
        
    def getDisponivel(self):
        return self.__disponivel
    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel
        
    def getQuilometragemAtual(self):
        return self.__quilometragemAtual
    def setQuilometragemAtual(self, quilometragemAtual):
        self.__quilometragemAtual = quilometragemAtual
        
    def getNumeroDeLocacoes(self):
        return self.__numeroDelocacoes
    def setNumeroDeLocacoes(self, numeroDelocacoes):
        self.__numeroDelocacoes = numeroDelocacoes
        
    def getIdVeiculo(self):
        return self.__idVeiculo
    def setIdVeiculo(self, idVeiculo):
        self.__idVeiculo = idVeiculo
    
    def getIdLocacao(self):
        return self.__idLocacao
    def setIdLocacao(self, idLocacao):
        self.__idLocacao = idLocacao
        
    def getIdCodTipoVeiculo(self):
        return self.__idCodTipoVeiculo
    def setIdCodTipoVeiculo(self, idCodTipoVeiculo):
        self.__idCodTipoVeiculo = idCodTipoVeiculo
    
    def toString(self):
        print "\nPlaca: %d"  %self.getPlaca() + \
            "\nMarca: " + self.getMarca() + \
            "\nCor: " + self.getCor() + \
            "\nModelo: " + self.getModelo() + \
            "\nDisponivel: " + self.getDisponivel() + \
            "\nQuilometragemAtual: " + self.getQuilometragemAtual() + \
            "\nNumeroDeLocacoes: " + self.getNumeroDeLocacoes() + \
            "\nIdLocacao:" + self.getIdLocacao() + \
            "\nIdCodTipoVeiculo:" + self.getIdCodTipoVeiculo()
            