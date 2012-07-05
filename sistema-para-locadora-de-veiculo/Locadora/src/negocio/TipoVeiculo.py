'''
Created on 05/07/2012

@author: Allan do Amaral
'''

class TipoVeiculo:

    def __init__ (self, taxaBase, precoKm, idTipoVeiculo, descricao, caucao):
        self.__taxaBase = taxaBase 
        self.__precoKm = precoKm
        self.__idTipoVeiculo = idTipoVeiculo
        self.__descricao = descricao
        self.__caucao = caucao
        
    def getTaxaBase(self):
        self.__taxaBase
    def setTaxaBase(self, taxaBase):
        self.__taxaBase = taxaBase
    
    def getPrecoKm(self):
        self.__precoKm
    def setPrecoKm(self, precoKm):
        self.__precoKm = precoKm
    
    def getIdTipoVeiculo(self):
        self.__idTipoVeiculo
    def setIdTipoVeiculo(self, idTipoVeiculo):
        self.__idTipoVeiculo = idTipoVeiculo
        
    def getDescricao(self):
        self.__descricao
    def setDescricao(self, descricao):
        self.__descricao = descricao 
        
    def getCaucao(self):
        self.__caucao
    def setCaucao(self, caucao):
        self.__caucao = caucao
