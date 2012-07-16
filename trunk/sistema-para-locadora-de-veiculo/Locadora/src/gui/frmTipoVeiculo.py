# -*- coding: latin-1 -*-
#Boa:Frame:frmTipoVeiculo

import wx
import wx.lib.buttons

#para funcionar no Boa tem que comentar esta parte
from negocio.TipoVeiculo import *
from db.TipoVeiculoDAO import *
from wx.tools.Editra.src.ebmlib.miscutil import Singleton
#comentar até a linha acima

def create(parent):
    return frmTipoVeiculo(parent)

[wxID_FRMTIPOVEICULO, wxID_FRMTIPOVEICULOBTNATUALIZAR, 
 wxID_FRMTIPOVEICULOBTNCANCELAR, wxID_FRMTIPOVEICULOBTNEDITAR, 
 wxID_FRMTIPOVEICULOBTNEXCLUIR, wxID_FRMTIPOVEICULOBTNINCLUIR, 
 wxID_FRMTIPOVEICULOBTNPESQUISAR, wxID_FRMTIPOVEICULOLSTTIPOVEICULOS, 
 wxID_FRMTIPOVEICULOPNLTIPOVEICULO, wxID_FRMTIPOVEICULOSTCAUCAO, 
 wxID_FRMTIPOVEICULOSTCODIGO, wxID_FRMTIPOVEICULOSTCOR, 
 wxID_FRMTIPOVEICULOSTDESCRICAO, wxID_FRMTIPOVEICULOSTPESQUISA, 
 wxID_FRMTIPOVEICULOSTTAXA, wxID_FRMTIPOVEICULOSTVEICULO, 
 wxID_FRMTIPOVEICULOTXTCAUCAO, wxID_FRMTIPOVEICULOTXTCODIGO, 
 wxID_FRMTIPOVEICULOTXTDESCRICAO, wxID_FRMTIPOVEICULOTXTPESQUISA, 
 wxID_FRMTIPOVEICULOTXTPRECO, wxID_FRMTIPOVEICULOTXTTAXA, 
] = [wx.NewId() for _init_ctrls in range(22)]

class frmTipoVeiculo(wx.Frame):
    #Luís explicou que é para que não abra mais de uma página de cliente.
    __metaclass__ = Singleton
    
    def _init_coll_lstTipoVeiculos_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='COD', width=65)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Descri\xe7\xe3o', width=260)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Taxa Base - R$', width=95)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Pre\xe7o/Km - R$', width=90)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading='Cau\xe7\xe3o - R$', width=90)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMTIPOVEICULO, name=u'frmTipoVeiculo',
              parent=prnt, pos=wx.Point(390, 126), size=wx.Size(697, 526),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX,
              title=u'Cadastro de Tipo de Ve\xedculos')
        self.SetClientSize(wx.Size(781, 488))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',wx.BITMAP_TYPE_ICO))

        self.pnlTipoVeiculo = wx.Panel(id=wxID_FRMTIPOVEICULOPNLTIPOVEICULO,
              name=u'pnlTipoVeiculo', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(781, 488), style=wx.TAB_TRAVERSAL)

        self.stVeiculo = wx.StaticBox(id=wxID_FRMTIPOVEICULOSTVEICULO,
              label=u'Dados do Ve\xedculo', name=u'stVeiculo',
              parent=self.pnlTipoVeiculo, pos=wx.Point(128, 8),
              size=wx.Size(636, 144), style=0)

        self.stTaxa = wx.StaticText(id=wxID_FRMTIPOVEICULOSTTAXA,
              label=u'Taxa Base (R$) :', name=u'stTaxa',
              parent=self.pnlTipoVeiculo, pos=wx.Point(260, 40),
              size=wx.Size(82, 13), style=0)
        
        self.txtCodigo = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTCODIGO,
              name=u'txtCodigo', parent=self.pnlTipoVeiculo, pos=wx.Point(144,
              56), size=wx.Size(102, 21), style=0, value=u'')

        self.txtTaxa = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTTAXA,
              name=u'txtTaxa', parent=self.pnlTipoVeiculo, pos=wx.Point(260,
              56), size=wx.Size(152, 21), style=0, value=u'')
        
        self.txtPreco = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTPRECO,
              name=u'txtPreco', parent=self.pnlTipoVeiculo, pos=wx.Point(430,
              56), size=wx.Size(152, 21), style=0, value=u'')
        
        self.txtCaucao = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTCAUCAO,
              name=u'txtCaucao', parent=self.pnlTipoVeiculo, pos=wx.Point(598,
              56), size=wx.Size(152, 21), style=0, value=u'')
        
        self.txtDescricao = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTDESCRICAO,
              name=u'txtDescricao', parent=self.pnlTipoVeiculo,
              pos=wx.Point(144, 104), size=wx.Size(606, 21), style=0,
              value=u'')

        self.stDescricao = wx.StaticText(id=wxID_FRMTIPOVEICULOSTDESCRICAO,
              label=u'Descri\xe7\xe3o :', name=u'stDescricao',
              parent=self.pnlTipoVeiculo, pos=wx.Point(144, 88),
              size=wx.Size(54, 13), style=0)        

        self.stCor = wx.StaticText(id=wxID_FRMTIPOVEICULOSTCOR,
              label=u'Pre\xe7o KM (R$) :', name=u'stCor',
              parent=self.pnlTipoVeiculo, pos=wx.Point(430, 40),
              size=wx.Size(76, 13), style=0)

        self.txtPesquisa = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTPESQUISA,
              name=u'txtPesquisa', parent=self.pnlTipoVeiculo, pos=wx.Point(144,
              200), size=wx.Size(400, 21), style=0, value=u'')

        self.btnPesquisar = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMTIPOVEICULOBTNPESQUISAR,
              name=u'btnPesquisar', parent=self.pnlTipoVeiculo,
              pos=wx.Point(568, 192), size=wx.Size(31, 32), style=0)
        self.btnPesquisar.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarButton,
              id=wxID_FRMTIPOVEICULOBTNPESQUISAR)

        self.btnIncluir = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNINCLUIR,
              label=u'Incluir', name=u'btnIncluir', parent=self.pnlTipoVeiculo,
              pos=wx.Point(24, 24), size=wx.Size(76, 25), style=0)
        self.btnIncluir.Bind(wx.EVT_BUTTON, self.OnBtnIncluirButton,
              id=wxID_FRMTIPOVEICULOBTNINCLUIR)

        self.stPesquisa = wx.StaticBox(id=wxID_FRMTIPOVEICULOSTPESQUISA,
              label=u'Pesquisa por C\xf3digo', name=u'stPesquisa',
              parent=self.pnlTipoVeiculo, pos=wx.Point(128, 168),
              size=wx.Size(636, 312), style=0)

        self.stCaucao = wx.StaticText(id=wxID_FRMTIPOVEICULOSTCAUCAO,
              label=u'Valor Cau\xe7\xe3o (R$) :', name=u'stCaucao',
              parent=self.pnlTipoVeiculo, pos=wx.Point(598, 40),
              size=wx.Size(95, 13), style=0)
        
        #Para funcionar no boa o comentário começa nesta linha
##        self.lstTipoVeiculos = wx.ListCtrl(id=wxID_FRMTIPOVEICULOLSTTIPOVEICULOS,
##              name=u'lstTipoVeiculos', parent=self.pnlTipoVeiculo,
##              pos=wx.Point(144, 240), size=wx.Size(456, 216),
##              style=wx.LC_REPORT)
##        self._init_coll_lstTipoVeiculos_Columns(self.lstTipoVeiculos)     

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNCANCELAR,
              label=u'Cancelar', name=u'btnCancelar',
              parent=self.pnlTipoVeiculo, pos=wx.Point(24, 64), size=wx.Size(76,
              25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMTIPOVEICULOBTNCANCELAR)

        self.btnEditar = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNEDITAR,
              label=u'Editar', name=u'btnEditar', parent=self.pnlTipoVeiculo,
              pos=wx.Point(24, 184), size=wx.Size(76, 25), style=0)
        self.btnEditar.Bind(wx.EVT_BUTTON, self.OnBtnEditarButton,
              id=wxID_FRMTIPOVEICULOBTNEDITAR)

        self.btnAtualizar = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNATUALIZAR,
              label=u'Atualizar', name=u'btnAtualizar',
              parent=self.pnlTipoVeiculo, pos=wx.Point(24, 224),
              size=wx.Size(76, 25), style=0)
        self.btnAtualizar.Bind(wx.EVT_BUTTON, self.OnBtnAtualizarButton,
              id=wxID_FRMTIPOVEICULOBTNATUALIZAR)

        self.btnExcluir = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNEXCLUIR,
              label=u'Excluir', name=u'btnExcluir', parent=self.pnlTipoVeiculo,
              pos=wx.Point(24, 272), size=wx.Size(76, 25), style=0)
        self.btnExcluir.Bind(wx.EVT_BUTTON, self.OnBtnExcluirButton,
              id=wxID_FRMTIPOVEICULOBTNEXCLUIR)           

        self.stCodigo = wx.StaticText(id=wxID_FRMTIPOVEICULOSTCODIGO,
              label=u'C\xf3digo :', name=u'stCodigo',
              parent=self.pnlTipoVeiculo, pos=wx.Point(144, 40),
              size=wx.Size(41, 13), style=0)
        
        self.gerarListctrl(self)
        
        self.btnAtualizar.Disable()
    
    def gerarListctrl(self,event):
        self.lstTipoVeiculos = wx.ListCtrl(id=wxID_FRMTIPOVEICULOLSTTIPOVEICULOS,
              name=u'lstTipoVeiculos', parent=self.pnlTipoVeiculo,
              pos=wx.Point(144, 240), size=wx.Size(606, 216),
              style=wx.LC_REPORT)
        self._init_coll_lstTipoVeiculos_Columns(self.lstTipoVeiculos)
        
        self.inserirInformacoesNaListctrl(self.lstTipoVeiculos)
        
        return self.lstTipoVeiculos

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def clearTextfield(self):
        #Método responsável por limpar os campos
        self.txtTaxa.Clear()
        self.txtDescricao.Clear()
        self.txtPreco.Clear()
        self.txtCaucao.Clear()
        self.txtCodigo.Clear()
    
    def obterDadosInformados(self):
        #Método para obter os dados fornecidos
        taxa = self.txtTaxa.GetValue()
        preco = self.txtPreco.GetValue()
        descricao = str(self.txtDescricao.GetValue())
        caucao = self.txtCaucao.GetValue()      
        codigo = self.txtCodigo.GetValue()
        
        #a lista será usada posteriormente na ação do botão de incluir um tipo de veículo
        lista = [codigo,taxa,preco,descricao.upper(),caucao]
        
        return lista
        
    def updateListctrl(self):
        #Método responsável por atualizar a listctrl após inserir,deletar e atualizar um tipo de veículo.
        self.lstTipoVeiculos.Destroy()
        self.gerarListctrl(self)
        
    def inserirInformacoesNaListctrl(self,lista):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega todos os tipos de veículos presentes no banco de dados
        rows = TipoVeiculoDAO.getAllTipos()
        if rows:
            for row in rows:
                print row
                num_itens = lista.GetItemCount()
                lista.InsertStringItem(num_itens,str(row[0]))
                #Vai na coluna correspondente da Listctrl e coloca a coluna correspondete
                #do banco de dados. 
                lista.SetStringItem(num_itens,1,row[3])
                lista.SetStringItem(num_itens,2,str(row[1]))
                lista.SetStringItem(num_itens,3,str(row[2]))
                lista.SetStringItem(num_itens,4,str(row[4]))
    
    def OnBtnIncluirButton(self, event):
        #Método que inclui um tipo de veículo no banco de dados.                
        try:
            lista = self.obterDadosInformados()
            tipo = TipoVeiculo(lista[0],lista[1],lista[2],lista[3],lista[4]) 
            
            TipoVeiculoDAO.insertTipo(tipo)
            
            self.updateListctrl()
            
            self.clearTextfield()
        except:
            print "Erro ao salvar no banco."

    
    def OnBtnCancelarButton(self, event):
        self.clearTextfield()
        
        #Habilitando os botões outra vez caso o botão cancelar seja usado na edição.
        self.txtCodigo.Enable()
        self.btnIncluir.Enable()
        self.btnExcluir.Enable()
        self.btnEditar.Enable()
        self.btnAtualizar.Disable()
        
        #Caso seja feita usado após alguma pesquisa
        self.txtPesquisa.Clear()
        self.btnPesquisar.Enable()
        
    def OnBtnEditarButton(self, event):        
        #Método para editar um tipo de veículo selecionado na Listctrl
                
        #pegar o indice do item selecionado no Listctrl
        indice = self.lstTipoVeiculos.GetFocusedItem()
        
        #desabilitando os botões desnecessários
        self.btnAtualizar.Enable()
        self.btnIncluir.Disable()
        self.btnExcluir.Disable()
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1: 
            idTipoVeiculo = self.lstTipoVeiculos.GetItemText(indice)
            
            #busca o tipo de veículo selecionado no banco de dados         
            tipoSelecionado = TipoVeiculoDAO.procurarTipo(idTipoVeiculo)
            
            #Colocando os valores do banco nos campos da tela
            self.txtCodigo.SetValue(str(tipoSelecionado.getIdTipoVeiculo()))            
            #O código não pode ser editado
            self.txtCodigo.Disable()               
            self.txtTaxa.SetValue(str(tipoSelecionado.getTaxaBase()))
            self.txtPreco.SetValue(str(tipoSelecionado.getPrecoKm()))
            self.txtCaucao.SetValue(str(tipoSelecionado.getCaucao()))
            self.txtDescricao.SetValue((tipoSelecionado.getDescricao()))
            self.btnEditar.Disable()
        else:            
            caixaDeMensagem = wx.MessageDialog(self,'Selecione um tipo.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeMensagem.ShowModal()
            caixaDeMensagem.Destroy()
            #Voltando o estado dos botões
            self.btnAtualizar.Disable()
            self.btnIncluir.Enable()
            self.btnExcluir.Enable()
    
    def OnBtnAtualizarButton(self, event):
        #Método para atualizar tipo
        
        #obtendo informações dos campos da tela  
        lista = self.obterDadosInformados()
        #guardando informações em um tipo
        tipo = TipoVeiculo(lista[0],lista[1],lista[2],lista[3],lista[4]) 
        
        
        #atualizando um tipo no banco de dados
        TipoVeiculoDAO.updateTipo(tipo)
        
        #atualiza a Listctrl
        self.updateListctrl()
        
        #limpando os campos
        self.clearTextfield()
                
        #retornando o estado incial dos botões
        self.txtCodigo.Enable()
        self.btnExcluir.Enable()
        self.btnIncluir.Enable()
        self.btnEditar.Enable()
        self.btnAtualizar.Disable()

    def OnBtnExcluirButton(self, event):
        
        
        #pegar o indice do item selecionado no Listctrl
        indice = self.lstTipoVeiculos.GetFocusedItem()
        
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1:
            idTipoVeiculo = self.lstTipoVeiculos.GetItemText(indice)
            try:                
                #deleta o tipo do banco
                TipoVeiculoDAO.deleteTipoVeiculo(idTipoVeiculo)
                #para atualizar a Listctrl retirando o tipo que existia nela
                self.updateListctrl()                
            except:
                #caso o tipo não seja removido, uma caixa de diálogo será mostrada
                caixaDeDialogo = wx.MessageDialog(self,'Tipo inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeDialogo.ShowModal()
                caixaDeDialogo.Destroy()
        else:
            caixaDeDialogo = wx.MessageDialog(self,'Selecione um tipo.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
        
    def OnBtnPesquisarButton(self, event):
        codigoInformado = int(self.txtPesquisa.GetValue())
        print codigoInformado
                
        try:
            tipoVeiculo = TipoVeiculoDAO.procurarTipo(codigoInformado)
            
            self.txtCodigo.SetValue (str(tipoVeiculo.getIdTipoVeiculo()))
            self.txtTaxa.SetValue (str(tipoVeiculo.getTaxaBase()))
            self.txtPreco.SetValue (str(tipoVeiculo.getPrecoKm()))
            self.txtCaucao.SetValue(str(tipoVeiculo.getCaucao()))
            self.txtDescricao.SetValue(tipoVeiculo.getDescricao())
            
            self.btnAtualizar.Disable()
            self.btnIncluir.Disable()
            self.btnEditar.Disable()
            self.btnExcluir.Disable()
            self.btnPesquisar.Disable()
        except:
            self.txtPesquisa.Clear()
            
            caixaDeDialogo = wx.MessageDialog(self,'Código inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
