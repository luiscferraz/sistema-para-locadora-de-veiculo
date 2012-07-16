# -*- coding: latin-1 -*-
'''
Created on 03/07/2012

@author: Allan do Amaral e Luis Carlos Ferraz
'''
from negocio.Cliente import *
from db.ConnectionUtil import *
from negocio.Cliente import *

class ClienteDAO(object):
    
    @staticmethod                 
    def insertCliente(cliente):
        
        INSERT_CLIENTE = "INSERT INTO CLIENTES (NOME, ENDERECO, TELEFONE , CEP , \
                     BAIRRO, CIDADE , UF , EMAIL , CPF)  VALUES ( ?, ?, ?, ? , ? , ? , ?, ? , ?)"
                     
                     
        if(cliente != None):
            try:
                lista = cliente.getAtributos()
                conexao = ConnectionUtil.conectar()
                                
                with conexao:
                    cur = conexao.cursor()
                    cur.execute(INSERT_CLIENTE , tuple(lista))
                                        
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
    def verificarExistenciaCliente(cpf):
        
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM CLIENTES WHERE CPF = ? ", (cpf,))
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
    def deleteCliente(cpf):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                if ClienteDAO.verificarExistenciaCliente(cpf) is True:
                    cur.execute("DELETE FROM CLIENTES WHERE CPF = ?" , (cpf,))
                    print "Removeu do banco"
                    conexao.commit()
                else:
                    print "Cliente não encontrado ou já foi removido!"
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
            
    @staticmethod         
    def procurarCliente(cpf):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM CLIENTES WHERE CPF = ?", (cpf,))
                print "\nBuscou no banco"
                row = cur.fetchone()
                #print row
                clienteEncontrado = Cliente(row[1],row[2],row[3],row[4],row[5],\
                                                row[6],row[7],row[8],row[9])
                clienteEncontrado.setIdCliente(row[0])     
                
                return clienteEncontrado
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1) 
        except:
            print "\nCliente Inexistente"   
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
    
    @staticmethod 
    def updateCliente(cliente):
        if(cliente != None):
            try:                                                             
                conexao = ConnectionUtil.conectar()
                with conexao:
                    cur = conexao.cursor()
                    if ClienteDAO.verificarExistenciaCliente(cliente.getCpf()) is True:
                        lista = cliente.getAtributos()
                        cur.execute("UPDATE CLIENTES SET NOME =? , ENDERECO = ?, TELEFONE =? , CEP=? , \
                     BAIRRO=?, CIDADE=? , UF =? , EMAIL =?   WHERE CPF = ?", \
                                    tuple([lista[0],lista[1],lista[2],lista[3],\
                                          lista[4],lista[5],lista[6],lista[7], lista[8]]))

                        print "Atualizou no banco"
                        conexao.commit()
                    else:
                        print "CPF nao encontrado!"
                
            except lite.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)    
            finally:
                ConnectionUtil.fecharConexao(cur,conexao)
                
    @staticmethod             
    def getAllClientes():
        try:    
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM CLIENTES ")
                row = cur.fetchall()      
                return row
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
                ConnectionUtil.fecharConexao(cur,conexao)
                
    def getClienteByNome(self):
        pass
            


#cliente = Cliente("111.111.111-11","nome", "endereco", "telefone" , "cep" , "bairro" , "cidade", "uf", "email")
#ClienteDAO.insertCliente(cliente)
#print ClienteDAO.verificarExistenciaCliente("211.111.111-11")
#ClienteDAO.deleteCliente("111.111.111-11")
#cliente_encontrado1 = ClienteDAO.procurarCliente("001.111.222-33")
#cliente_encontrado = ClienteDAO.procurarCliente("000.111.222-33")
#cliente_encontrado.toString()
#cliente_encontrado.setNome("ALLAN DO AMARAL")
#cliente_encontrado.toString()
#ClienteDAO.updateCliente(cliente_encontrado)