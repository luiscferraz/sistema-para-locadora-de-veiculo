# -*- coding: latin-1 -*-
'''
Created on 07/07/2012

@author: Allan do Amaral, Marcela Domingues e Jean Macena.
'''

from db.ConnectionUtil import *
from negocio.Veiculo import *

class VeiculoDAO(object):
    
    def insertVeiculo(self,veiculo):
        
        INSERT_VEICULO = "INSERT INTO VEICULOS (PLACA, MARCA, COR , MODELO , DISPONIBILIDADE,  \
        FK_ID_TIPO_VEICULO) VALUES ( ?, ?, ?, ?, ?, ?)"
                     
                     
        if(veiculo != None):
            try:
                lista = veiculo.getAtributos()
                conexao = ConnectionUtil.conectar()
                                
                with conexao:
                    cur = conexao.cursor()
                    cur.execute(INSERT_VEICULO , tuple(lista))
                                        
                conexao.commit()
                print "Salvou no banco"
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)   
            finally:
                ConnectionUtil.fecharConexao(cur, conexao) 

    
        
        