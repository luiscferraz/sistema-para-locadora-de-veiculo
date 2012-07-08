# -*- coding: latin-1 -*-

'''
Created on 05/07/2012

@author: Marcela Domingues
'''

class Veiculo:
    
    def __init__(self,placa,marca,cor,modelo,idTipoVeiculo):
        self.__placa = placa
        self.__marca = marca
        self.__cor = cor
        self.__modelo = modelo
        self.__disponibilidade = "DISPONIVEL"
        self.__idTipoVeiculo = idTipoVeiculo
        self.__idVeiculo = None
        
        
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

    def getIdVeiculo(self):
        return self.__idVeiculo
    def setIdVeiculo(self, idVeiculo):
        self.__idVeiculo = idVeiculo
        
    def getIdTipoVeiculo(self):
        return self.__idTipoVeiculo
    def setIdTipoVeiculo(self, idTipoVeiculo):
        self.__idTipoVeiculo = idTipoVeiculo
        
    def getAtributos(self):
        placa = self.getPlaca()
        marca = self.getMarca()
        cor = self.getCor()
        modelo = self.getModelo()
        disponibilidade = self.getDisponibilidade()
        idTipoVeiculo = self.getIdTipoVeiculo()
        
        return [placa,marca,cor,modelo,disponibilidade,idTipoVeiculo]
    
    def toString(self):
        print "\nPlaca: " + self.getPlaca() + \
            "\nMarca: " + self.getMarca() + \
            "\nCor: " + self.getCor() + \
            "\nModelo: " + self.getModelo() + \
            "\nDisponibilidade: " + self.getDisponibilidade() + \
            "\nCódigo Tipo Veículo:" + str(self.getIdTipoVeiculo())
            