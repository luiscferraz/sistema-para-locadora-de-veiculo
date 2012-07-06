'''
Created on 05/07/2012

@author: Allan do Amaral
'''

class TipoVeiculo:

    def __init__ (self, idTipoVeiculo, taxaBase, precoKm, descricao, caucao):
        self.__idTipoVeiculo = idTipoVeiculo
        self.__taxaBase = taxaBase
        self.__precoKm = precoKm
        self.__descricao = descricao
        self.__caucao = caucao
        
    def getTaxaBase(self):
        return self.__taxaBase
    def setTaxaBase(self, taxaBase):
        self.__taxaBase = taxaBase
    
    def getPrecoKm(self):
        return self.__precoKm
    def setPrecoKm(self, precoKm):
        self.__precoKm = precoKm
    
    def getIdTipoVeiculo(self):
        return self.__idTipoVeiculo
    def setIdTipoVeiculo(self, idTipoVeiculo):
        self.__idTipoVeiculo = idTipoVeiculo
        
    def getDescricao(self):
        return self.__descricao
    def setDescricao(self, descricao):
        self.__descricao = descricao 
        
    def getCaucao(self):
        return self.__caucao
    def setCaucao(self, caucao):
        self.__caucao = caucao
        
    def getAtributos(self):
        ID = self.getIdTipoVeiculo()
        taxaBase = self.getTaxaBase()
        precoKm = self.getPrecoKm()
        descricao = self.getDescricao()
        caucao = self.getCaucao()
        
        return [ID, taxaBase, precoKm, descricao, caucao]
