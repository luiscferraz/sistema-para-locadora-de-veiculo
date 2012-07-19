# -*- coding: latin-1 -*-
'''
Created on 15/07/2012

@author: Allan do Amaral e Marcela Domingues
'''
from db.ConnectionUtil import *
from negocio.Locacao import *
from datetime import *

class LocacaoDAO(object):
    
    @staticmethod
    def insertLocacao(locacao):
        
        INSERT_LOCACAO = "INSERT INTO LOCACAO (DATA_LOCACAO, QUILOMETRAGEM_SAIDA, VALOR_CONTA_PARCIAL ,  \
        FK_CPF_CLIENTE, FK_PLACA_VEICULO) VALUES ( ?, ?, ?, ?, ?)"
                     
                     
        if(locacao != None):
            try:
                lista = locacao.getAtributos()
                #print lista
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
    
    @staticmethod            
    def verificarExistenciaLocacao(idLocacao):
        
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM LOCACAO WHERE ID_LOCACAO = ? ", (idLocacao,))
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
    def deleteLocacao(idLocacao):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                if LocacaoDAO.verificarExistenciaLocacao(idLocacao) is True:
                    cur.execute("DELETE FROM LOCACAO WHERE ID_LOCACAO = ?" , (idLocacao,))
                    print "Removeu do banco"
                    conexao.commit()
                else:
                    print "Locação não encontrada ou já foi removida!"
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
            
    
    @staticmethod
    def procurarLocacaoById(idLocacao):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM LOCACAO WHERE ID_LOCACAO = ?", (idLocacao,))
                print "\nBuscou no banco"
                row = cur.fetchone()
                #print row
                locacaoEncontrada = Locacao(row[1],row[2],row[3],row[4],row[5])
                                                
                locacaoEncontrada.setIdLocacao(row[0])     
                
                return locacaoEncontrada
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1) 
        except:
            print "\nLocação Inexistente"   
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
    
    @staticmethod       
    def updateLocacao(locacao):
        if(locacao != None):
            try:                                                             
                conexao = ConnectionUtil.conectar()
                with conexao:
                    cur = conexao.cursor()
                    #idLocacao = locacao.getIdLocacao()
                    if LocacaoDAO.verificarExistenciaLocacao(locacao.getIdLocacao()) is True:
                        lista = locacao.getAtributos()
                        cur.execute("UPDATE LOCACAO SET DATA_LOCACAO = ?, QUILOMETRAGEM_SAIDA = ?, \
                                    VALOR_CONTA_PARCIAL = ? ,  FK_CPF_CLIENTE = ?, FK_PLACA_VEICULO = ? \
                                    WHERE ID_LOCACAO = ?", \
                                    tuple([lista[0],lista[1],lista[2],lista[3],\
                                          lista[4], locacao.getIdLocacao()]))

                        print "Atualizou no banco"
                        conexao.commit()
                    else:
                        print "Locação não encontrada!"
                
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)    
            finally:
                ConnectionUtil.fecharConexao(cur,conexao)
    
    @staticmethod
    def getAllLocacoes():
        try:    
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM LOCACAO ")
                row = cur.fetchall()      
                return row
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
                ConnectionUtil.fecharConexao(cur,conexao)
                

#hoje = datetime.today()
#print hoje
#locacao = Locacao(hoje,1200,833,'000.111.222-33',28)
#dao = LocacaoDAO()
#dao.insertLocacao(locacao)
#print dao.verificarExistenciaLocacao(5)
#print dao.verificarExistenciaLocacao(95)
#dao.deleteLocacao(4)
#locacaoEncontrada = dao.procurarLocacaoById(5)
#locacaoEncontrada.toString() 
#locacaoEncontrada.setIdCliente("111.222.333-44")
#dao.updateLocacao(locacaoEncontrada)   
#print dao.getAllLocacoes()        