# -*- coding: latin-1 -*-

'''
Created on 23/08/2012

@author: Marcela Domingues
'''

from db.ConnectionUtil import *
from negocio.Devolucao import *
from datetime import *

class DevolucaoDAO(object):
    
    @staticmethod
    def insertDevolucao(devolucao):
        
        INSERT_DEVOLUCAO = "INSERT INTO DEVOLUCAO (DATA_DEVOLUCAO, QUILOMETRAGEM_DE_CHEGADA, VALOR_CONTA_TOTAL ,  \
        FK_ID_LOCACAO) VALUES ( ?, ?, ?, ?)"
                     
                     
        if(devolucao != None):
            try:
                lista = devolucao.getAtributos()
                #print lista
                conexao = ConnectionUtil.conectar()
                                
                with conexao:
                    cur = conexao.cursor()
                    cur.execute(INSERT_DEVOLUCAO , tuple(lista))
                                        
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
    def verificarExistenciaDevolucao(idDevolucao):
        
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM DEVOLUCAO WHERE ID_DEVOLUCAO = ? ", (idDevolucao,))
                print "Verificou no banco"
                retorno = cur.fetchone()
                                
                if retorno is not None:
                    return True
                else:
                    return False
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
    
    @staticmethod
    def deleteDevolucao(idDevolucao):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                if DevolucaoDAO.verificarExistenciaLocacao(idDevolucao) is True:
                    cur.execute("DELETE FROM DEVOLUCAO WHERE ID_DEVOLUCAO = ?" , (idDevolucao,))
                    print "Removeu do banco"
                    conexao.commit()
                else:
                    print "Devolução não encontrada ou já foi removida!"
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
            
    
    @staticmethod
    def procurarDevolucaById(idDevolucao):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM DEVOLUCAO WHERE ID_DEVOLUCAO = ?", (idDevolucao,))
                print "\nBuscou no banco"
                row = cur.fetchone()
                #print row
                devolucaoEncontrada = Devolucao(row[1],row[2],row[3],row[4])
                                                
                devolucaoEncontrada.setIdDevolucao(row[0])     
                
                return devolucaoEncontrada
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1) 
        except:
            print "\nDevolução Inexistente"   
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
    
    @staticmethod       
    def updateDevolucao(devolucao):
        if(devolucao != None):
            try:                                                             
                conexao = ConnectionUtil.conectar()
                with conexao:
                    cur = conexao.cursor()
                    #idDevolucao = devolucao.getIdDevolucao()
                    if DevolucaoDAO.verificarExistenciaDevolucao(devolucao.getIdDevolucao()) is True:
                        lista = devolucao.getAtributos()
                        cur.execute("UPDATE DEVOLUCAO SET DATA_DEVOLUCAO = ?, QUILOMETRAGEM_DE_CHEGADA = ?, \
                                    VALOR_CONTA_TOTAL = ? ,  FK_ID_LOCACAO = ?", \
                                    tuple([lista[0],lista[1],lista[2],lista[3],\
                                          devolucao.getIdDevolucao()]))

                        print "Atualizou no banco"
                        conexao.commit()
                    else:
                        print "Devolução não encontrada!"
                
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)    
            finally:
                ConnectionUtil.fecharConexao(cur,conexao)
    
    @staticmethod
    def getAllDevolucoes():
        try:    
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM DEVOLUCAO ")
                row = cur.fetchall()      
                return row
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
                ConnectionUtil.fecharConexao(cur,conexao)
                
