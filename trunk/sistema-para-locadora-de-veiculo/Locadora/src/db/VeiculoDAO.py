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
                
                
    def verificarExistenciaVeiculo(self, placa):
        
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM VEICULOS WHERE PLACA = ? ", (placa,))
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
            
            
    def deleteVeiculo(self, placa):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                if self.verificarExistenciaVeiculo(placa) is True:
                    cur.execute("DELETE FROM VEICULOS WHERE PLACA = ?" , (placa,))
                    print "Removeu do banco"
                    conexao.commit()
                else:
                    print "Veiculo n�o encontrado ou j� foi removido!"
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
            
    def procurarVeiculo(self, placa):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM VEICULOS WHERE PLACA = ?", (placa,))
                print "\nBuscou no banco"
                row = cur.fetchone()
                #print row
                veiculoEncontrado = Veiculo(row[1],row[2],row[3],row[4],row[6])
                veiculoEncontrado.setIdVeiculo(row[0])   
                
                return veiculoEncontrado
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1) 
        except:
            print "\nVeiculo Inexistente"   
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
    
    def updateVeiculo(self, veiculo):
        if(veiculo != None):
            try:                                                             
                conexao = ConnectionUtil.conectar()
                with conexao:
                    cur = conexao.cursor()
                    if self.verificarExistenciaVeiculo(veiculo.getPlaca()) is True:
                        lista = veiculo.getAtributos()
                        cur.execute("UPDATE VEICULOS SET MARCA=?, COR=?, MODELO=? , \
                     DISPONIBILIDADE=?, FK_ID_TIPO_VEICULO=?  WHERE PLACA = ?", \
                                    tuple([lista[1],lista[2],lista[3],lista[4], lista[5], lista[0]]))

                        print "Atualizou no banco"
                        conexao.commit()
                    else:
                        print "Veiculo de placa nao encontrada!"
                
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)    
            finally:
                ConnectionUtil.fecharConexao(cur,conexao)
                
    def getAllVeiculos(self):
        try:    
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM VEICULOS ")
                row = cur.fetchall()      
                return row
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
                ConnectionUtil.fecharConexao(cur,conexao)

    
        
#veiculo = Veiculo("WHK-2510","HONDA", "PRATA", "FIT" , 30)
dao = VeiculoDAO()
#dao.insertVeiculo(veiculo)
#print dao.verificarExistenciaVeiculo("WHK-2010")
#dao.deleteVeiculo("WHK-2010")
#veiculo_encontrado1 = dao.procurarVeiculo("WHK-2010")
veiculo_encontrado = dao.procurarVeiculo("HZG-1000")
print veiculo_encontrado.getAtributos()
#veiculo_encontrado.toString()
veiculo_encontrado.setMarca("CHEVROLET")
print veiculo_encontrado.getAtributos()
#veiculo_encontrado.toString()
dao.updateVeiculo(veiculo_encontrado)