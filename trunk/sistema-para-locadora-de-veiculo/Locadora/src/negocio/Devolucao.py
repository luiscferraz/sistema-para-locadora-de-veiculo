'''
Created on 03/08/2012

@author: Marcela Domingues e Allan do Amaral
'''

class Devolucao:
    
    def __init__(self, dataDevolucao, quilometragemDeChegada, valorTotalConta, idLocacao):
        self.__idDevolucao = None
        self.__dataDevolucao = dataDevolucao
        self.__quilometragemDeChegada = quilometragemDeChegada
        self.__valorTotalConta = valorTotalConta
        self.__idLocacao = idLocacao
    
    def getIdDevolucao(self):
        return self.__idDevolucao
    def setIdDevolucao(self, idDevolucao):
        self.__idLocacao = idDevolucao  
    
    def getDataDevolucao(self):
        return self.__dataDevolucao
    def setDataDevolucao(self, dataDevolucao):
        self.__dataDevolucao = dataDevolucao
        
    def getQuilometragemDeChegada(self):
        return self.__quilometragemDeChegada
    def setQuilometragemDeChegada(self, quilometragemDeChegada):
        self.__quilometragemDeChegada = quilometragemDeChegada
        
    def getValorTotalConta(self):
        return self.__valorTotalConta
    def setValorTotalConta(self, valorTotalConta):
        self.__valorTotalConta = valorTotalConta
    
    def getIdLocacao(self):
        return self.__idLocacao
    def setIdLocacao(self, idLocacao):
        self.__idLocacao = idLocacao
        
    def getAtributos(self):
        dataDevolucao = self.getDataDevolucao()
        quilometragemDeChegada = self.getQuilometragemDeChegada()
        valorTotalConta = self.getValorTotalConta()
        idLocacao = self.getIdLocacao()
        
        return [dataDevolucao, quilometragemDeChegada, valorTotalConta, idLocacao]
    
    def toString(self):
        print "ID Devolução : " + str(self.getIdDevolucao()) + \
            "\nData da Devolução: " + str(self.getDataDevolucao()) +\
            "\nQuilometragem de Chegada: " + str(self.getQuilometragemDeChegada()) + \
            "\nValor Total: " + str(self.getValorTotalConta()) + \
            "\nID Locação: " + str(self.getIdLocacao()) 