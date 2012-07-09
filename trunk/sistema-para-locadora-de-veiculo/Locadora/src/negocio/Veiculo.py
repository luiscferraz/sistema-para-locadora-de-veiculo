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
            
    def validarPlaca(self):
        for i in range (0,3):
            if((self.getPlaca()[i]== '0' )or (self.getPlaca()[i]== '1' ) or (self.getPlaca()[i]== '2' ) or\
               (self.getPlaca()[i]== '3' )or (self.getPlaca()[i]== '4' ) or (self.getPlaca()[i]== '5' ) or\
               (self.getPlaca()[i]== '6' )or (self.getPlaca()[i]== '7' ) or (self.getPlaca()[i]== '8' ) or\
               (self.getPlaca()[i]== '9' )):
                #print self.getPlaca()[i]
                return False
        for i in range (4,8):
            if((self.getPlaca()[i]!= '0' )and (self.getPlaca()[i]!= '1' ) and (self.getPlaca()[i]!= '2' ) and\
               (self.getPlaca()[i]!= '3' )and (self.getPlaca()[i]!= '4' ) and (self.getPlaca()[i]!= '5' ) and\
               (self.getPlaca()[i]!= '6' )and (self.getPlaca()[i]!= '7' ) and (self.getPlaca()[i]!= '8' ) and\
               (self.getPlaca()[i]!= '9' )):
                #print self.getPlaca()[i]
                return False
        return True
            