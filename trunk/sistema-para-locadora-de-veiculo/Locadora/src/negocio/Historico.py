# -*- coding: latin-1 -*-
'''
Created on 03/08/2012

@author: Marcela Domingues e Allan do Amaral
'''

class Historico:
    
    def __init__(self, dataLocacao, dataDevolucao, quilometragemDeSaida, quilometragemDeChegada, placaVeiculo, cpfCliente, valorTotalConta):
        self.__dataLocacao = dataLocacao
        self.__dataDevolucao = dataDevolucao
        self.__quilometragemDeSaida = quilometragemDeSaida
        self.__quilometragemDeChegada = quilometragemDeChegada
        self.__placaVeiculo = placaVeiculo
        self.__cpfCliente = cpfCliente
        self.__valorTotalConta = valorTotalConta
     
    def getDataLocacao(self):
        return self.__dataLocacao
    def setDataLocacao(self, dataLocacao):
        self.__dataLocacao = dataLocacao
    
    def getDataDevolucao(self):
        return self.__dataDevolucao
    def setDataDevolucao(self, dataDevolucao):
        self.__dataDevolucao = dataDevolucao
        
    def getQuilometragemDeSaida(self):
        return self.__quilometragemDeSaida
    def setQuilometragemDeSaida(self, quilometragemDeSaida):
        self.__quilometragemDeSaida = quilometragemDeSaida
        
    def getQuilometragemDeChegada(self):
        return self.__quilometragemDeChegada
    def setQuilometragemDeChegada(self, quilometragemDeChegada):
        self.__quilometragemDeChegada = quilometragemDeChegada
    
    def getPlacaVeiculo(self):
        return self.__placaVeiculo
    def setPlacaCarro(self, placaVeiculo):
        self.__placaCarro = placaVeiculo  
    
    def getCpfCliente(self):
        return self.__cpfCliente
    def setCpfCliente(self, cpfCliente):
        self.__cpfCliente = cpfCliente
    
    def getValorTotalConta(self):
        return self.__valorTotalConta
    def setValorTotalConta(self, valorTotalConta):
        self.__valorTotalConta = valorTotalConta
        
    def getAtributos(self):
        dataLocacao = self.getDataLocacao()
        dataDevolucao = self.getDataDevolucao()
        quilometragemDeSaida = self.getQuilometragemDeSaida()
        quilometragemDeChegada = self.getQuilometragemDeChegada()
        placaVeiculo = self.getPlacaVeiculo()
        cpfCliente = self.getCpfCliente()
        valorTotalConta = self.getValorTotalConta()
        
        return [dataLocacao, dataDevolucao, quilometragemDeSaida, quilometragemDeChegada, placaVeiculo, cpfCliente, valorTotalConta]
    
    def toString(self):
        print "Data da Locação : " + str(self.getDataLocacao()) + \
            "Data da Devolução: " + str(self.getDataDevolucao()) + \
            "\nQuilometragem de Saida: " + str(self.getQuilometragemDeChegada()) + \
            "\nQuilometragem de Chegada: " + str(self.getQuilometragemDeChegada()) + \
            "\nPlaca Veículo: " + str(self.getPlacaVeiculo()) + \
            "\nCPF Cliente: " + str(self.getCpfCliente()) + \
            "\nValor Total: " + str(self.getValorTotalConta())