# -*- coding: latin-1 -*-
'''
Created on 03/07/2012

@author: Allan do Amaral e Luis Carlos Ferraz
'''
from negocio.Cliente import *
from db.ConnectionUtil import *
from negocio.Cliente import *

class ClienteDAO(object):
    
                     
    def insertCliente(self,cliente):
        
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
                
                
    def verificarExistenciaCliente(self, cpf):
        
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
            


#cliente = Cliente("111.111.111-11","nome", "endereco", "telefone" , "cep" , "bairro" , "cidade", "uf", "email")
#dao = ClienteDAO()
#dao.insertCliente(cliente)
#print dao.verificarExistenciaCliente("111.111.111-11")