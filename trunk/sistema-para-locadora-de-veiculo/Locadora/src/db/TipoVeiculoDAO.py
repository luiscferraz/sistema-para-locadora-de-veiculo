# -*- coding: latin-1 -*-
'''
Created on 05/07/2012

@author: Allan do Amaral e Luis Carlos Ferraz
'''

from negocio.TipoVeiculo import *
from db.ConnectionUtil import *

class TipoVeiculoDAO(object):
    
                     
    def insertTipo(self,tipoVeiculo):
        
        INSERT_TIPO = "INSERT INTO TIPO_VEICULOS (ID_TIPO_VEICULO, TAXA_BASE, PRECO_KM, DESCRICAO , CAUCAO) \
                     VALUES ( ?, ?, ?, ?, ?)"
                     
                     
        if(tipoVeiculo != None):
            try:
                lista = tipoVeiculo.getAtributos()
                print "Lista - ", lista
                conexao = ConnectionUtil.conectar()
                                
                with conexao:
                    cur = conexao.cursor()
                    cur.execute(INSERT_TIPO , tuple(lista))
                                        
                conexao.commit()
                print "Salvou no banco"
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)   
            finally:
                ConnectionUtil.fecharConexao(cur, conexao) 
                
                
    def verificarExistenciaTipo(self, id):
        
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM TIPO_VEICULOS WHERE ID_TIPO_VEICULO = ? ", (id,))
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
            
    def deleteTipo(self, id):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                if self.verificarExistenciaTipo(id) is True:
                    cur.execute("DELETE FROM TIPO_VEICULOS WHERE ID_TIPO_VEICULO = ?" , (id,))
                    print "Removeu do banco"
                    conexao.commit()
                else:
                    print "Tipo de veículo não encontrado ou já foi removido!"
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
            
    def procurarTipo(self, id):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM TIPO_VEICULOS WHERE ID_TIPO_VEICULO = ?", (id,))
                print "\nBuscou no banco"
                row = cur.fetchone()
                #print row
                tipoEncontrado = TipoVeiculo(row[0], row[1],row[2],row[3],row[4])     
                
                return tipoEncontrado
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1) 
        except:
            print "\nTipo de Veiculo Inexistente"   
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
    
    def updateTipo(self, tipo):
        if(tipo != None):
            try:                                                             
                conexao = ConnectionUtil.conectar()
                with conexao:
                    cur = conexao.cursor()
                    if self.verificarExistenciaTipo(tipo.getIdTipoVeiculo()) is True:
                        lista = tipo.getAtributos()
                        cur.execute("UPDATE TIPO_VEICULOS SET TAXA_BASE=?, PRECO_KM=?, DESCRICAO=?, CAUCAO=?  WHERE ID_TIPO_VEICULO = ?", \
                                    tuple([lista[1],lista[2],lista[3],lista[4], lista[0]]))

                        print "Atualizou no banco"
                        conexao.commit()
                    else:
                        print "ID do tipo nao encontrado!"
                
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)    
            finally:
                ConnectionUtil.fecharConexao(cur,conexao)
                
    def getAllTipos(self):
        try:    
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM TIPO_VEICULOS ")
                row = cur.fetchall()      
                return row
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
                ConnectionUtil.fecharConexao(cur,conexao)
            


#tipo = TipoVeiculo(30, 200, 12, "descricao", 23)
#dao = TipoVeiculoDAO()
#dao.insertTipo(tipo)
#print dao.verificarExistenciaTipo(12)
#dao.deleteTipo(12)
#tipo_encontrado1 = dao.procurarTipo(12)
#tipo_encontrado = dao.procurarTipo(1234)
#tipo_encontrado1.toString()
#tipo_encontrado1.setDescricao("default")
#tipo_encontrado.toString()
#dao.updateTipo(tipo_encontrado1)