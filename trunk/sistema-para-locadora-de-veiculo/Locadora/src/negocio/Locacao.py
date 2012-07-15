# -*- coding: latin-1 -*-
'''
Created on 07/07/2012

@author: Jean Karlos e Marcela Domingues
'''

class Locacao:
    
    def __init__(self,dataLocacao, quilometragemDeSaida, cpfCliente, idVeiculo):
        self.__idLocacao = None
        self.__dataLocacao = dataLocacao
        self.__quilometragemDeSaida = quilometragemDeSaida
        self.__valorContaParcial = 0
        self.__cpfCliente = cpfCliente
        self.__idVeiculo = idVeiculo
        
    def getIdLocacao(self):
        return self.__idLocacao
    def setIdLocacao(self, idLocacao):
        self.__idLocacao = idLocacao
        
    def getDataLocacao(self):
        return self.__dataLocacao
    def setDataLocacao(self, dataLocacao):
        self.__dataLocacao = dataLocacao        
            
    def getQuilometragemDeSaida(self):
        return self.__quilometragemDeSaida
    def setQuilometragemDeSaida(self, quilometragemDeSaida):
        self.__quilometragemDeSaida = quilometragemDeSaida
    
    def getValorContaParcial(self):
        return self.__valorContaParcial
    def setValorContaParcial(self, valorContaParcial):
        self.__valorContaParcial = valorContaParcial
    
    def getCpfCliente(self):
        return self.__cpfCliente
    def setIdCliente(self, cpfCliente):
        self.__cpfCliente = cpfCliente
        
    def getIdVeiculo(self):
        return self.__idVeiculo
    def setIdVeiculo(self, idVeiculo):
        self.__idVeiculo = idVeiculo
        
            
    def getAtributos(self):
        dataLocacao = self.getDataLocacao()
        quilometragemDeSaida = self.getQuilometragemDeSaida()
        cpfCliente = self.getCpfCliente()
        idVeiculo = self.getIdVeiculo()
        
        return [dataLocacao, quilometragemDeSaida, cpfCliente, idVeiculo]
    
    def toString(self):
        print "ID Locação %d: " %self.getIdLocacao() + \
            "\nQuilometragem de saída: " + self.getQuilometragemDeSaida() + \
            "\nValor Parcial: " + self.getValorContaParcial() + \
            "\nCPF Cliente: " + self.getCpfCliente() + \
            "\nID Veículo: " + self.getIdVeiculo()
            
        
        
        
        
        
    
