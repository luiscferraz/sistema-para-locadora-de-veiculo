# -*- coding: latin-1 -*-
#Boa:Frame:frmLocacao

import wx
from wx.lib.anchors import LayoutAnchors
import wx.lib.buttons
import wx.lib.masked.textctrl

from db.ClienteDAO import *
from db.VeiculoDAO import *
from db.TipoVeiculoDAO import TipoVeiculoDAO
from datetime import *
from negocio.Locacao import *
from db.LocacaoDAO import *


def create(parent):
    return frmLocacao(parent)

[wxID_FRMLOCACAO, wxID_FRMLOCACAOBTNCANCELAR, wxID_FRMLOCACAOBTNINCLUIR, 
 wxID_FRMLOCACAOBTNPESQUISARCOR, wxID_FRMLOCACAOBTNPESQUISARCPF, 
 wxID_FRMLOCACAOBTNPESQUISARMODELO, wxID_FRMLOCACAOLISTCTRLBUSCATIPOVEICULO, 
 wxID_FRMLOCACAOLSTCTRLLOCACAO, wxID_FRMLOCACAOLSTIPOVEICULO, 
 wxID_FRMLOCACAOPANEL1, wxID_FRMLOCACAORADIOBOXTIPOBUSCA, 
 wxID_FRMLOCACAOSTCLIENTE, wxID_FRMLOCACAOSTCOR, wxID_FRMLOCACAOSTCPF, 
 wxID_FRMLOCACAOSTMODELO, wxID_FRMLOCACAOSTNOME, wxID_FRMLOCACAOSTNOMECLIENTE, 
 wxID_FRMLOCACAOSTLOCACAO, wxID_FRMLOCACAOSTRESULTADOTIPO, 
 wxID_FRMLOCACAOSTTIPOVEICULO, wxID_FRMLOCACAOSTVEICULO, 
 wxID_FRMLOCACAOTXTCOR, wxID_FRMLOCACAOTXTCPF, wxID_FRMLOCACAOTXTMODELO, 
] = [wx.NewId() for _init_ctrls in range(24)]

class frmLocacao(wx.Frame):
    def _init_coll_listCtrlBuscaTipoVeiculo_Columns(self, parent):
        # generated method, don't edit
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Placa',
              width=70)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Modelo',
              width=260)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Cor',
              width=100)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Taxa Base - R$', width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading='Pre\xe7o/KM - R$', width=100)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT,
              heading='Cau\xe7\xe3o - R$', width=90)
        
    def _init_coll_listCtrlLocacao_Columns(self,parent):
        # generated method, don't edit
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Id',
              width=50)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Data',
              width=140)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='CPF',
              width=100)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Placa',
              width=70)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='Modelo',
              width=220)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='Km Saída',
              width=70)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='Valor Parcial',
              width=90)
    
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMLOCACAO, name='frmLocacao',
              parent=prnt, pos=wx.Point(350, 28), size=wx.Size(962, 680),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION,
              title='Loca\xe7\xe3o de Ve\xedculo')
        self.SetClientSize(wx.Size(946, 642))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRMLOCACAOPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(946, 642),
              style=wx.TAB_TRAVERSAL)

        self.stCliente = wx.StaticBox(id=wxID_FRMLOCACAOSTCLIENTE,
              label='Cliente', name='stCliente', parent=self.panel1,
              pos=wx.Point(128, 8), size=wx.Size(808, 80), style=0)
        self.stCliente.Enable(True)

        self.stCPF = wx.StaticText(id=wxID_FRMLOCACAOSTCPF, label='CPF :',
              name='stCPF', parent=self.panel1, pos=wx.Point(144, 32),
              size=wx.Size(27, 13), style=0)

        self.txtCPF = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMLOCACAOTXTCPF,
              name='txtCPF', parent=self.panel1, pos=wx.Point(144, 48),
              size=wx.Size(128, 24), style=0, value='')
        self.txtCPF.SetMask('XXX.XXX.XXX-XX')
        self.txtCPF.SetAutoformat('')
        self.txtCPF.SetDatestyle('MDY')
        self.txtCPF.SetFormatcodes('')
        self.txtCPF.SetDescription('')
        self.txtCPF.SetExcludeChars('')
        self.txtCPF.SetValidRegex('')
        self.txtCPF.SetMaxLength(14)
        self.txtCPF.Bind(wx.EVT_TEXT_MAXLEN, self.OnTxtCPFTextMaxlen,
              id=wxID_FRMLOCACAOTXTCPF)
        self.txtCPF.Bind(wx.EVT_TEXT_ENTER, self.OnTxtCPFTextMaxlen,
              id=wxID_FRMLOCACAOTXTCPF)

        self.btnPesquisarCpf = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMLOCACAOBTNPESQUISARCPF,
              name='btnPesquisarCpf', parent=self.panel1, pos=wx.Point(280, 44),
              size=wx.Size(31, 32), style=0)
        self.btnPesquisarCpf.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarCpfButton,
              id=wxID_FRMLOCACAOBTNPESQUISARCPF)

        self.stNomeCliente = wx.StaticText(id=wxID_FRMLOCACAOSTNOMECLIENTE,
              label='', name='stNomeCliente', parent=self.panel1,
              pos=wx.Point(336, 56), size=wx.Size(200, 13), style=0)

        self.stNome = wx.StaticText(id=wxID_FRMLOCACAOSTNOME, label='Nome :',
              name='stNome', parent=self.panel1, pos=wx.Point(336, 32),
              size=wx.Size(35, 13), style=0)

        self.stVeiculo = wx.StaticBox(id=wxID_FRMLOCACAOSTVEICULO,
              label='Ve\xedculo', name='stVeiculo', parent=self.panel1,
              pos=wx.Point(128, 96), size=wx.Size(808, 536), style=0)

        self.radioBoxTipoBusca = wx.RadioBox(choices=['Tipo de Veículo',
              'Modelo', 'Cor'], id=wxID_FRMLOCACAORADIOBOXTIPOBUSCA,
              label='Efetuar busca por', majorDimension=1,
              name='radioBoxTipoBusca', parent=self.panel1, pos=wx.Point(144,
              116), size=wx.Size(110, 90), style=wx.RA_SPECIFY_COLS)
        self.radioBoxTipoBusca.SetAutoLayout(True)
        self.radioBoxTipoBusca.SetSelection(2)
        self.radioBoxTipoBusca.SetStringSelection('Tipo de ve\xedculo')
        self.radioBoxTipoBusca.Bind(wx.EVT_SET_FOCUS,
              self.OnRadioBoxTipoBuscaSetFocus)
        self.radioBoxTipoBusca.Bind(wx.EVT_RADIOBOX,
              self.OnRadioBoxTipoBuscaRadiobox,
              id=wxID_FRMLOCACAORADIOBOXTIPOBUSCA)

        self.stTipoVeiculo = wx.StaticText(id=wxID_FRMLOCACAOSTTIPOVEICULO,
              label='Tipo de Ve\xedculo : ', name='stTipoVeiculo',
              parent=self.panel1, pos=wx.Point(296, 116), size=wx.Size(82, 13),
              style=0)

        self.lsTipoVeiculo = wx.Choice(choices=TipoVeiculoDAO.listarTiposDeVeiculos(), id=wxID_FRMLOCACAOLSTIPOVEICULO, name='lsTipoVeiculo',
              parent=self.panel1, pos=wx.Point(296, 136), size=wx.Size(624, 21),
              style=0)
        self.lsTipoVeiculo.Bind(wx.EVT_CHOICE, self.OnLsTipoVeiculoChoice,
              id=wxID_FRMLOCACAOLSTIPOVEICULO)
        self.lsTipoVeiculo.Bind(wx.EVT_SET_FOCUS, self.OnLsTipoVeiculoSetFocus)

        self.stModelo = wx.StaticText(id=wxID_FRMLOCACAOSTMODELO,
              label='Modelo :', name='stModelo', parent=self.panel1,
              pos=wx.Point(296, 166), size=wx.Size(42, 13), style=0)

        self.txtModelo = wx.TextCtrl(id=wxID_FRMLOCACAOTXTMODELO,
              name='txtModelo', parent=self.panel1, pos=wx.Point(296, 184),
              size=wx.Size(400, 21), style=0, value='')
        self.txtModelo.Bind(wx.EVT_TEXT_ENTER, self.OnTxtModeloTextEnter,
              id=wxID_FRMLOCACAOTXTMODELO)

        self.txtCor = wx.TextCtrl(id=wxID_FRMLOCACAOTXTCOR, name='txtCor',
              parent=self.panel1, pos=wx.Point(744, 184), size=wx.Size(147, 21),
              style=0, value='')

        self.stCor = wx.StaticText(id=wxID_FRMLOCACAOSTCOR, label='Cor :',
              name='stCor', parent=self.panel1, pos=wx.Point(744, 168),
              size=wx.Size(25, 13), style=0)

        self.stResultadoTipo = wx.StaticBox(id=wxID_FRMLOCACAOSTRESULTADOTIPO,
              label='Resultado da busca', name='stResultadoTipo',
              parent=self.panel1, pos=wx.Point(144, 224), size=wx.Size(776,
              176), style=0)

        self.listCtrlBuscaTipoVeiculo = wx.ListCtrl(id=wxID_FRMLOCACAOLISTCTRLBUSCATIPOVEICULO,
              name='listCtrlBuscaTipoVeiculo', parent=self.panel1,
              pos=wx.Point(160, 248), size=wx.Size(744, 136),
              style=wx.LC_REPORT)
        self._init_coll_listCtrlBuscaTipoVeiculo_Columns(self.listCtrlBuscaTipoVeiculo)

        self.stLocacoes = wx.StaticBox(id=wxID_FRMLOCACAOSTLOCACAO,
              label='Loca\xe7\xe3o',
              name='stLocacao', parent=self.panel1, pos=wx.Point(144,
              412), size=wx.Size(776, 204), style=0)

        self.lstCtrlLocacao = wx.ListCtrl(id=wxID_FRMLOCACAOLSTCTRLLOCACAO,
              name='lstCtrlLocacao', parent=self.panel1, pos=wx.Point(160,
              440), size=wx.Size(744, 160), style=wx.LC_REPORT)
        self._init_coll_listCtrlLocacao_Columns(self.lstCtrlLocacao)
        

        self.btnIncluir = wx.lib.buttons.GenButton(id=wxID_FRMLOCACAOBTNINCLUIR,
              label='Incluir', name='btnIncluir', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(76, 25), style=0)
        self.btnIncluir.Bind(wx.EVT_BUTTON, self.OnBtnIncluirButton,
              id=wxID_FRMLOCACAOBTNINCLUIR)
        self.btnIncluir.SetConstraints(LayoutAnchors(self.btnIncluir, True,
              True, False, False))

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMLOCACAOBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self.panel1,
              pos=wx.Point(24, 64), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMLOCACAOBTNCANCELAR)

        self.btnPesquisarModelo = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMLOCACAOBTNPESQUISARMODELO,
              name='btnPesquisarModelo', parent=self.panel1, pos=wx.Point(696,
              184), size=wx.Size(31, 21), style=0)
        self.btnPesquisarModelo.Bind(wx.EVT_BUTTON,self.OnBtnPesquisarModelo,
              id=wxID_FRMLOCACAOBTNPESQUISARMODELO)

        self.btnPesquisarCor = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMLOCACAOBTNPESQUISARCOR,
              name='btnPesquisarCor', parent=self.panel1, pos=wx.Point(891,
              184), size=wx.Size(31, 21), style=0)
        self.btnPesquisarCor.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarCor,
              id=wxID_FRMLOCACAOBTNPESQUISARCOR)
        
        
        
    

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.radioBoxTipoBusca.Disable()
        self.txtModelo.Disable()
        self.btnPesquisarModelo.Disable()
        self.txtCor.Disable()
        self.btnPesquisarCor.Disable()
        self.lsTipoVeiculo.Disable()
        self.inserirDadosNasColunasDaTabelaLocacao(self.lstCtrlLocacao)
        
    def criarTabela(self):
        self.listCtrlBuscaTipoVeiculo = wx.ListCtrl(id=wxID_FRMLOCACAOLISTCTRLBUSCATIPOVEICULO,
              name='listCtrlBuscaTipoVeiculo', parent=self.panel1,
              pos=wx.Point(160, 248), size=wx.Size(744, 136),
              style=wx.LC_REPORT)
        self._init_coll_listCtrlBuscaTipoVeiculo_Columns(self.listCtrlBuscaTipoVeiculo)
        
    def criarTabelaLocacao(self):
        self.lstCtrlLocacao = wx.ListCtrl(id=wxID_FRMLOCACAOLSTCTRLLOCACAO,
              name='lstCtrlLocacao', parent=self.panel1, pos=wx.Point(160,
              440), size=wx.Size(744, 160), style=wx.LC_REPORT)
        self._init_coll_listCtrlLocacao_Columns(self.lstCtrlLocacao)
        self.inserirDadosNasColunasDaTabelaLocacao(self.lstCtrlLocacao)
        
    def getIdTipo(self,event):
        # pega o id do tipo de veículo selecionado
        tipos = TipoVeiculoDAO().getAllTipos()
        for i in tipos:
            if (i[3] == self.lsTipoVeiculo.GetStringSelection()):
                self.idTipo = i[0]
                #print self.idTipo
                return self.idTipo
    
    def getValorRadioBox(self,event):
        retorno = self.radioBoxTipoBusca.GetSelection()
        #print retorno 
        return retorno
    
    def OnTxtCPFTextMaxlen(self, event):
        event.Skip()

    def OnTxtCPFTextEnter(self, event):
        event.Skip()

    def OnBtnPesquisarCpfButton(self, event):  
        cpf = self.txtCPF.GetValue() 
        #print cpf
        
        #print ClienteDAO.verificarExistenciaCliente(cpf)
        if(ClienteDAO.verificarExistenciaCliente(cpf) is True):
            cliente = ClienteDAO.procurarCliente(cpf)
            self.stNomeCliente.SetLabel(cliente.getNome())  
            self.radioBoxTipoBusca.Enable() 
            self.getValorRadioBox(self.radioBoxTipoBusca)
        else:
            caixaDeDialogo = wx.MessageDialog(self,'Cliente inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
            
            self.txtCPF.Clear()
        
    def OnBtnIncluirButton(self, event):
        #Método para editar um veículo selecionado na Listctrl
                
        #pegar o indice do item selecionado no Listctrl
        indice = self.listCtrlBuscaTipoVeiculo.GetFocusedItem()
        #print indice
        
        #se o indice for -1 é pq nada foi selecionado
        if indice != -1: 
            placa = self.listCtrlBuscaTipoVeiculo.GetItemText(indice)
            #print placa
            
            #busca o veículo selecionado no banco de dados         
            veiculoSelecionado = VeiculoDAO.procurarVeiculo(placa)
            #print veiculoSelecionado.toString()
            veiculoSelecionado.setDisponibilidade("LOCADO")
            
            idTipoVeiculo = veiculoSelecionado.getIdTipoVeiculo()
            tipoVeiculo = TipoVeiculoDAO.procurarTipo(idTipoVeiculo)
            
            #atualizando a disponibilidade do veículo no banco de dados
            VeiculoDAO.updateVeiculo(veiculoSelecionado)
            
            dataLocacao = datetime.today()
            quilometragemDeSaida = veiculoSelecionado.getQuilometragemAtual()
            valorContaParcial = tipoVeiculo.getCaucao()
            cpfCliente = self.txtCPF.GetValue()
            
            locacao = Locacao(dataLocacao,quilometragemDeSaida,valorContaParcial,cpfCliente,placa)
            
            LocacaoDAO.insertLocacao(locacao)
            
            self.listCtrlBuscaTipoVeiculo.Destroy()
            self.criarTabela()
            
            #print "Locação efetuada com sucesso" 
            caixaDeMensagem = wx.MessageDialog(self,'Locação efetuada com sucesso.', 'CONFIRMAÇÃO', wx.OK | wx.ICON_INFORMATION)
            caixaDeMensagem.ShowModal()
            caixaDeMensagem.Destroy()
            
            self.lstCtrlLocacao.Destroy()
            self.criarTabelaLocacao()
        else:            
                caixaDeMensagem = wx.MessageDialog(self,'Selecione um veículo.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeMensagem.ShowModal()
                caixaDeMensagem.Destroy()

    def OnBtnCancelarButton(self, event):
        self.listCtrlBuscaTipoVeiculo.Destroy()
        self.criarTabela()        

    def OnRadioBoxTipoBuscaSetFocus(self, event):
        event.Skip()
            

    def OnRadioBoxTipoBuscaRadiobox(self, event):
        if (self.radioBoxTipoBusca.GetSelection() == 0):
            self.lsTipoVeiculo.Enable()
            self.txtModelo.Disable()
            
            self.txtCor.Disable()
            self.btnPesquisarCor.Disable()
            
            self.listCtrlBuscaTipoVeiculo.Destroy()
            self.criarTabela()
        elif (self.radioBoxTipoBusca.GetSelection() == 1):
            
            self.txtModelo.Enable()
            self.btnPesquisarModelo.Enable()
            
            self.txtCor.Disable()
            self.btnPesquisarCor.Disable()
            
            self.lsTipoVeiculo.Disable()
            self.lsTipoVeiculo.Select(-1)
            
            self.listCtrlBuscaTipoVeiculo.Destroy()
            self.criarTabela()
        elif (self.radioBoxTipoBusca.GetSelection() == 2):
            self.txtModelo.Disable()
            self.btnPesquisarModelo.Disable()
            
            self.lsTipoVeiculo.Disable()
            self.lsTipoVeiculo.Select(-1)
            
            self.txtCor.Enable()
            self.btnPesquisarCor.Enable()
            
            self.listCtrlBuscaTipoVeiculo.Destroy()
            self.criarTabela()

    def OnTxtModeloTextEnter(self, event):
        event.Skip()

    def OnLsTipoVeiculoChoice(self, event):
        #Destrói a tabela anterior para que seja reconstruída de acordo com a escolha
        self.listCtrlBuscaTipoVeiculo.Destroy()
        #Cria uma nova tabela
        self.criarTabela()
      
        #Pega o id do tipo de veículo selecionado
        idTipoVeiculo = self.getIdTipo(self.lsTipoVeiculo)
        #insere na tabela os dados de acordo com o tipo de veículo escolhido
        self.inserirInformacoesNaListctrlByTipo(self.listCtrlBuscaTipoVeiculo, idTipoVeiculo)
        

    def OnBtnPesquisarModelo(self, event):
        #Destrói a tabela anterior para que seja reconstruída de acordo com a escolha
        self.listCtrlBuscaTipoVeiculo.Destroy()
        self.criarTabela()
        
        #obtém o modelo informado
        modelo = str(self.txtModelo.GetValue())
        
        #insere na tabela os dados de acordo com a cor fornecida
        self.inserirInformacoesNaListctrlByModelo(self.listCtrlBuscaTipoVeiculo, modelo.upper())
        self.txtModelo.Clear()

    def OnBtnPesquisarCor(self, event):
        #Destrói a tabela anterior para que seja reconstruída de acordo com a escolha
        self.listCtrlBuscaTipoVeiculo.Destroy()
        self.criarTabela()
                
        #obtém a cor informada        
        cor = str(self.txtCor.GetValue())
        
        #insere na tabela os dados de acordo com a cor fornecida
        self.inserirInformacoesNaListctrlByCor(self.listCtrlBuscaTipoVeiculo, cor.upper())
        
        self.txtCor.Clear()

    def OnLsTipoVeiculoSetFocus(self, event):
        event.Skip()
        
    def inserirInformacoesNaListctrlByCor(self,listCtrl,cor):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega todos os tipos de veículos presentes no banco de dados
        rows = VeiculoDAO.getVeiculosByCorAndDisponibilidade(cor,'DISPONIVEL')
        
        #usa este método para inserir os dados nas colunas da ListCtrl do frame
        self.inserirDadosNasColunasDaTabelaDeResultados(listCtrl, rows)
                
    def inserirInformacoesNaListctrlByTipo(self,listCtrl,idTipoVeiculo):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega todos os tipos de veículos presentes no banco de dados
        rows = VeiculoDAO.getVeiculosByTipoAndDisponibilidade(idTipoVeiculo, "DISPONIVEL")
        
        #usa este método para inserir os dados nas colunas da ListCtrl do frame
        self.inserirDadosNasColunasDaTabelaDeResultados(listCtrl, rows)
                
    def inserirInformacoesNaListctrlByModelo(self,listCtrl,modelo):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega todos os tipos de veículos presentes no banco de dados
        rows = VeiculoDAO.getVeiculosByModeloAndDisponibilidade(modelo, "DISPONIVEL")        
        self.inserirDadosNasColunasDaTabelaDeResultados(listCtrl, rows)
    
    def inserirDadosNasColunasDaTabelaDeResultados(self,listCtrl,rows):        
        #Método responsável por colocar as informações do banco nas colunas da ListCtrl.
        #Desenvolvido para evitar a repetição de código nos 3 tipos de buscas de um veículo.
        #Recebe como parâmetro a ListCtrl na qual deseja inserir dados e as linhas
        #de informações obtidas numa busca no banco de dados.
        if rows:
            for row in rows:
                num_itens = listCtrl.GetItemCount()
                listCtrl.InsertStringItem(num_itens,str(row[1]))
                listCtrl.SetStringItem(num_itens,1,row[4])
                #Vai na coluna correspondente da Listctrl e coloca a coluna correspondete
                #do banco de dados. 
                listCtrl.SetStringItem(num_itens,2,row[3])
                
                tipoVeiculo = TipoVeiculoDAO.procurarTipo(row[6]) 
                #referente à tabela de tipo de veículos
                listCtrl.SetStringItem(num_itens,3,str(tipoVeiculo.getTaxaBase()))
                listCtrl.SetStringItem(num_itens,4,str(tipoVeiculo.getPrecoKm()))
                listCtrl.SetStringItem(num_itens,5,str(tipoVeiculo.getCaucao()))
                
    def inserirDadosNasColunasDaTabelaLocacao(self,listCtrl):   
        rows = LocacaoDAO.getAllLocacoes()
        #print rows 
         
        if rows:
            for row in rows:
                num_itens = listCtrl.GetItemCount()
                #print num_itens
                listCtrl.InsertStringItem(num_itens,str(row[0]))
                listCtrl.SetStringItem(num_itens,1,row[1])
                listCtrl.SetStringItem(num_itens,2,row[4])
                listCtrl.SetStringItem(num_itens,3,row[5])
                
                veiculo = VeiculoDAO.procurarVeiculo(row[5])
                modelo = veiculo.getModelo()
                
                listCtrl.SetStringItem(num_itens,4,modelo)
                listCtrl.SetStringItem(num_itens,5,str(row[3]))
                listCtrl.SetStringItem(num_itens,6,str(row[2]))
                
                  
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
        
                
