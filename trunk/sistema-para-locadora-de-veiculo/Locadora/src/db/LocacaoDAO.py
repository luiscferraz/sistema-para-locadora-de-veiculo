# -*- coding: latin-1 -*-
'''
Created on 15/07/2012

@author: Allan do Amaral e Marcela Domingues
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
                
    def verificarExistenciaLocacao(self, idLocacao):
        
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
    
    def deleteLocacao(self, idLocacao):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                if self.verificarExistenciaLocacao(idLocacao) is True:
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
            
    
    def procurarLocacaoById(self, idLocacao):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM LOCACAO WHERE ID_LOCACAO = ?", (idLocacao,))
                print "\nBuscou no banco"
                row = cur.fetchone()
                print row
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
        