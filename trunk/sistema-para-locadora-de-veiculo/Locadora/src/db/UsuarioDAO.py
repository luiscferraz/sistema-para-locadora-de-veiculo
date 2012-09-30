# -*- coding: latin-1 -*-
'''
Created on 30/09/2012

@author: Marcela Domingues
'''

import sqlite3
import sys
from db.ConnectionUtil import *
from negocio.Usuario import *

class UsuarioDAO():  

    @staticmethod
    def insertUsuario(usuario):
        
        INSERT_USUARIO = "INSERT INTO USUARIOS (LOGIN, SENHA) VALUES ( ?, ?)"
                     
                     
        if(usuario != None):
            try:
                lista = usuario.getAtributos()
                print lista
                conexao = ConnectionUtil.conectar()
                                
                with conexao:
                    cur = conexao.cursor()
                    cur.execute(INSERT_USUARIO , tuple(lista))
                                        
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
    def verificarExistenciaUsuario(login, senha):
        
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM USUARIOS WHERE LOGIN = ? AND SENHA = ?", (login, senha,))
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
    def procurarUsuario(login):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM USUARIOS WHERE LOGIN = ?", (login,))
                print "\nBuscou no banco"
                row = cur.fetchone()
                #print row
                usuarioEncontrado = Usuario(row[0],row[1])    
                
                return usuarioEncontrado
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1) 
        except:
            print "\nUsuário Inexistente"   
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)
    
                
    @staticmethod               
    def verificarLogin(login):
        
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM USUARIOS WHERE LOGIN = ? ", (login,))
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
    def verificarSenha(senha):
        
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                cur.execute("SELECT * FROM USUARIOS WHERE SENHA = ? ", (senha,))
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
    def deleteUsuario(login, senha):
                
        try:
            conexao = ConnectionUtil.conectar()
            with conexao:
                cur = conexao.cursor()
                if UsuarioDAO.verificarExistenciaUsuario(login, senha) is True:
                    cur.execute("DELETE FROM USUARIOS WHERE LOGIN = ? AND SENHA = ?" , (login, senha,))
                    print "Removeu do banco"
                    conexao.commit()
                else:
                    print "Usuario não encontrado ou já foi removido!"
            
        except lite.Error, e:
            if conexao:
                conexao.rollback()        
                print "Error %s:" % e.args[0]
                sys.exit(1)    
        finally:
            ConnectionUtil.fecharConexao(cur,conexao)

                    
    @staticmethod
    def alterarSenha(self, login, senha, valor):
        if(login != None) and (senha != None):
            try:
                conexao = self.conectar()
                with conexao:
                    cur = conexao.cursor()
                    if self.verificarLogin(login) is 1:
                        if self.verificarSenha(senha) is 1:                   
                            cur.execute("UPDATE USUARIOS SET SENHA=? WHERE LOGIN=? AND SENHA=?", (valor, login, senha))
                            print "Atualizado no banco"
                            conexao.commit()
            except sqlite3.Error, e:
                if conexao:
                    conexao.rollback()        
                    print "Error %s:" % e.args[0]
                    sys.exit(1)    
            finally:
                ConnectionUtil.fecharConexao(cur,conexao)
            
        
        
    
usuario = Usuario("allan", "1994")
dao = UsuarioDAO()
print usuario.getAtributos()
dao.insertUsuario(usuario)
print UsuarioDAO.verificarExistenciaUsuario("allan", "1994")
#UsuarioDAO.deleteUsuario("allan", "1994")