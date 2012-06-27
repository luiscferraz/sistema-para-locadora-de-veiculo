'''
Created on 27/06/2012

@author: Allan do Amaral
'''
import sqlite3 as lite
import sys

class ConnectionUtil():
        
    @staticmethod
    def conectar():
        connection = None
        try:
            connection = lite.connect('..\banco\Locadora.db')            
            #print "Conexão criada com sucesso!"            
            return connection
        except lite.Error, e:
            if connection:
                connection.rollback()
                print "Error %s:" % e.args[0]
                sys.exit(1)  
                
    @staticmethod            
    def fecharConexao(cursor,conexao):   
        if cursor:
            cursor.close()
        if conexao :
            conexao.close()
        
        
            

        