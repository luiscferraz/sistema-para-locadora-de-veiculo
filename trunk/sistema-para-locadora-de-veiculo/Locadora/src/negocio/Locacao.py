# -*- coding: latin-1 -*-
'''
Created on 07/07/2012

@author: Jean
'''

class Locacao:
    
    def __init__(self, idLocacao, quilometragemDeSaida, quilometragemDeEntrada, total):
        self.__idLocacao = idLocacao
        self.__quilometragemDeSaida = quilometragemDeSaida
        self.__quilometragemDeEntrada = quilometragemDeEntrada
        self.__total = total
        self.__idCliente = None
        self.__idVeiculo = None
        
    def getIdLocacao(self):
        return self.__idLocacao
    def setIdLocacao(self, idLocacao):
        self.__idLocacao = idLocacao
        
    def getQuilometragemDeSaida(self):
        return self.__quilometragemDeSaida
    def setQuilometragemDeSaida(self, quilometragemDeSaida):
        self.__quilometragemDeSaida = quilometragemDeSaida
    
    def getQuilometragemDeEntrada(self):
        return self.__quilomeetragemDeEntrada
    def setQuilometragemDeEntrada(self, quilometragemDeEntrada):
        self.__quilomeetragemDeEntrada = quilometragemDeEntrada
        
    def getTotal(self):
        return self.__total
    def setTotal(self, total):
        self.__total = total
    
    def getIdCliente(self):
        return self.__idCliente
    def setIdCliente(self, idCliente):
        self.__idCliente = idCliente
        
    def getIdVeiculo(self):
        return self.__idVeiculo
    def setIdVeiculo(self, idVeiculo):
        self.__idVeiculo = idVeiculo
        
            
    def getAtributos(self):
        idLocacao = self.getIdLocacao()
        quilometragemDeSaida = self.getQuilometragemDeSaida()
        quilometragemDeEntrada = self.getQuilometragemDeEntrada()
        total = self.getTotal()
        idCliente = self.getIdCliente()
        idVeiculo = self.getIdVeiculo()
        
        return [idLocacao, quilometragemDeSaida, quilometragemDeEntrada, total, idCliente, idVeiculo]
    
    def toString(self):
        print "ID Locação %d: " %self.getIdLocacao() + \
            "\nQuilometragem de saída: " + self.getQuilometragemDeSaida() + \
            "\nQuilometragem de Entrada: " + self.getQuilometragemDeEntrada() + \
            "\nTotal: " + self.getTotal() + \
            "\nID Cliente: " + self.getIdCliente() + \
            "\nID Veículo: " + self.getIdVeiculo()
            
        
        
        
        
        
    
