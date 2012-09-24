# -*- coding: latin-1 -*-

'''
Created on 23/08/2012

@author: Marcela Domingues
'''

from db.ConnectionUtil import *
from negocio.Historico import *
from datetime import *

class HistoricoDAO(object):
    
    @staticmethod
    def insertHistorico(historico):
        
        INSERT_HISTORICO = "INSERT INTO HISTORICO (DATA_LOCACAO, DATA_DEVOLUCAO, QUILOMETRAGEM_DE_SAIDA, \
        QUILOMETRAGEM_DE_CHEGADA, FK_PLACA_VEICULO, FK_CPF_CLIENTE, VALOR_CONTA_TOTAL) VALUES ( ?, ?, ?, ?, ?, ?, ?)"
                     
                     
        if(historico != None):
            try:
                lista = historico.getAtributos()
                print lista
                conexao = ConnectionUtil.conectar()
                                
                with conexao:
                    cur = conexao.cursor()
                    cur.execute(INSERT_HISTORICO , tuple(lista))
                                        
                conexao.commit()
                print "Salvou no banco"
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)   
            finally:
                ConnectionUtil.fecharConexao(cur, conexao) 

    @staticmethod
    def getHistoricoByCpf(cpf):
        conexao = ConnectionUtil.conectar()
        try:
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM HISTORICO WHERE FK_CPF_CLIENTE LIKE ? ",(cpf+"%",))
                row = cur.fetchall()      
                return row
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
                ConnectionUtil.fecharConexao(cur,conexao)
                
    @staticmethod
    def getHistoricoByPlaca(placa):
        conexao = ConnectionUtil.conectar()
        try:
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM HISTORICO WHERE FK_PLACA_VEICULO LIKE ? ",(placa+"%",))
                row = cur.fetchall()      
                return row
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
                ConnectionUtil.fecharConexao(cur,conexao)

    
    @staticmethod
    def getAllHistorico():
        try:    
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM HISTORICO ")
                row = cur.fetchall()      
                return row
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
                ConnectionUtil.fecharConexao(cur,conexao)


#hoje = datetime.now()
#historico = Historico(hoje, hoje, 1200, 833,'000.111.222-33',28, 2234)
#dao = HistoricoDAO()
#dao.insertHistorico(historico)  