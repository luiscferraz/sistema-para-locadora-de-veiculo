# -*- coding: latin-1 -*-

'''
Created on 05/07/2012

@author: Marcela Domingues
'''

class Veiculo:
    
    def __init__(self,placa,marca,cor,modelo,quilometragemAtual):
        self.__placa = placa
        self.__marca = marca
        self.__cor = cor
        self.__modelo = modelo
        self.__disponibilidade = "Disponivel"
        self.__quilometragemAtual = quilometragemAtual
        self.__idVeiculo = None
        self.__idTipoVeiculo = None
        
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
        
    def getDisponibilidade(self):
        return self.__disponibilidade
    def setDisponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade
        
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
        
    def getIdTipoVeiculo(self):
        return self.__idTipoVeiculo
    def setIdTipoVeiculo(self, idTipoVeiculo):
        self.__idTipoVeiculo = idTipoVeiculo
    
    def toString(self):
        print "\nPlaca: %d"  %self.getPlaca() + \
            "\nMarca: " + self.getMarca() + \
            "\nCor: " + self.getCor() + \
            "\nModelo: " + self.getModelo() + \
            "\nDisponibilidade: " + self.getDisponibilidade() + \
            "\nQuilometragem Atual: " + self.getQuilometragemAtual() + \
            "\nCódigo Tipo Veículo:" + self.getIdTipoVeiculo()
            