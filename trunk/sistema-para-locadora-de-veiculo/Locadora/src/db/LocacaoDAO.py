# -*- coding: latin-1 -*-
'''
Created on 15/07/2012

@author: Allan do Amaral
'''
from db.ConnectionUtil import *
from negocio.Locacao import *
from datetime import *

class LocacaoDAO(object):
    
    def insertLocacao(self,locacao):
        
        INSERT_LOCACAO = "INSERT INTO LOCACAO (DATA_LOCACAO, QUILOMETRAGEM_SAIDA, VALOR_CONTA_PARCIAL ,  \
        FK_CPF_CLIENTE, FK_ID_VEICULO) VALUES ( ?, ?, ?, ?, ?)"
                     
                     
        if(locacao != None):
            try:
                lista = locacao.getAtributos()
                print lista
                conexao = ConnectionUtil.conectar()
                                
                with conexao:
                    cur = conexao.cursor()
                    cur.execute(INSERT_LOCACAO , tuple(lista))
                                        
                conexao.commit()
                print "Salvou no banco"
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)   
            finally:
                ConnectionUtil.fecharConexao(cur, conexao) 
                

#hoje = datetime.today()
#print hoje
#locacao = Locacao(hoje,1200,833,'000.111.222-33',28)
#dao = LocacaoDAO()
#dao.insertLocacao(locacao)


    
        