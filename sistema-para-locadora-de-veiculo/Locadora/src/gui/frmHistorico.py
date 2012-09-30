# -*- coding: latin-1 -*-
#Boa:Frame:Frame1

import wx
import wx.lib.stattext
import wx.lib.masked.textctrl
import wx.lib.buttons

from db.ClienteDAO import *
from db.VeiculoDAO import *
from db.TipoVeiculoDAO import TipoVeiculoDAO
from datetime import *
from negocio.Locacao import *
from db.LocacaoDAO import *
from negocio.Historico import *
from db.HistoricoDAO import *

def create(parent):
    return frmHistorico(parent)

[wxID_FRMHISTORICO, wxID_FRMHISTORICOBTNPESQUISARCPF, 
 wxID_FRMHISTORICOBTNPESQUISARPLACA, wxID_FRMHISTORICOBTNCANCELAR, wxID_FRMHISTORICOLBLCPF, 
 wxID_FRMHISTORICOLBLPLACA, wxID_FRMHISTORICOLISTCTRLBUSCA, wxID_FRMHISTORICOPNLHISTORICO, 
 wxID_FRMHISTORICOSTHISTORICO, wxID_FRMHISTORICOSTBUSCAR, wxID_FRMHISTORICOTXTCPF, 
 wxID_FRMHISTORICOTXTPLACA, 
] = [wx.NewId() for _init_ctrls in range(12)]

class frmHistorico(wx.Frame):
    def _init_coll_listCtrlBuscaLocacaoFinalizada_Columns(self,parent):
        # generated method, don't edit
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Placa de veículo',
              width=100)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='CPF',
              width=95)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Data de Locação',
              width=155)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Km de saída',
              width=90)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='Data de devolução',
              width=155)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='Km de chegada',
              width=100)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_LEFT, heading='Valor Total',
              width=80)
        
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMHISTORICO, name='', parent=prnt,
              pos=wx.Point(115, 42), size=wx.Size(932, 580),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Histórico')
        self.SetClientSize(wx.Size(1016, 542))

        self.pnlHistorico = wx.Panel(id=wxID_FRMHISTORICOPNLHISTORICO, name='pnlHistorico', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1116, 542),
              style=wx.TAB_TRAVERSAL)

        self.stHistorico = wx.StaticBox(id=wxID_FRMHISTORICOSTHISTORICO,
              label=u'Histórico', name='stHistorico', parent=self.pnlHistorico,
              pos=wx.Point(144, 184), size=wx.Size(836, 328), style=0)

        self.stBuscar = wx.StaticBox(id=wxID_FRMHISTORICOSTBUSCAR,
              label=u'Buscar Loca\xe7\xe3o finalizada', name='stBuscar',
              parent=self.pnlHistorico, pos=wx.Point(144, 32), size=wx.Size(836, 120),
              style=0)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMHISTORICOBTNCANCELAR,
              label=u'Cancelar', name='btnCancelar', parent=self.pnlHistorico,
              pos=wx.Point(24, 40), size=wx.Size(96, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMHISTORICOBTNCANCELAR)
        

        self.txtCpf = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMHISTORICOLBLCPF,
              name=u'txtCpf', parent=self.pnlHistorico, pos=wx.Point(168, 88),
              size=wx.Size(160, 21), style=0, value='')
        self.txtCpf.SetMask(u'XXX.XXX.XXX-XX')
        self.txtCpf.SetAutoformat('')
        self.txtCpf.SetDatestyle('MDY')
        self.txtCpf.SetFormatcodes('')
        self.txtCpf.SetDescription('')
        self.txtCpf.SetExcludeChars('')
        self.txtCpf.SetValidRegex('')
        self.txtCpf.SetMaxLength(14)

        self.lblCpf = wx.lib.stattext.GenStaticText(ID=wxID_FRMHISTORICOLBLCPF,
              label=u'CPF :', name=u'lblCpf', parent=self.pnlHistorico,
              pos=wx.Point(168, 72), size=wx.Size(27, 13), style=0)

        self.lblPlaca = wx.lib.stattext.GenStaticText(ID=wxID_FRMHISTORICOLBLPLACA,
              label=u'Placa :', name=u'lblPlaca', parent=self.pnlHistorico,
              pos=wx.Point(392, 72), size=wx.Size(33, 13), style=0)

        self.txtPlaca = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMHISTORICOLBLPLACA,
              name=u'txtPlaca', parent=self.pnlHistorico, pos=wx.Point(392, 88),
              size=wx.Size(152, 21), style=0, value=u'   -    ')
        self.txtPlaca.SetMaxLength(8)
        self.txtPlaca.SetMask(u'XXX-XXXX')
        self.txtPlaca.SetAutoformat('')
        self.txtPlaca.SetDatestyle('MDY')
        self.txtPlaca.SetFormatcodes('')
        self.txtPlaca.SetDescription('')
        self.txtPlaca.SetExcludeChars('')
        self.txtPlaca.SetValidRegex('')

        self.btnPesquisarCpf = wx.lib.buttons.GenBitmapToggleButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMHISTORICOBTNPESQUISARCPF,
              name='btnPesquisarCpf', parent=self.pnlHistorico,
              pos=wx.Point(336, 80), size=wx.Size(31, 30), style=0)
        self.btnPesquisarCpf.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarCpfButton,
              id=wxID_FRMHISTORICOBTNPESQUISARCPF)

        self.btnPesquisarPlaca = wx.lib.buttons.GenBitmapToggleButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMHISTORICOBTNPESQUISARPLACA,
              name='btnPesquisarPlaca', parent=self.pnlHistorico,
              pos=wx.Point(552, 80), size=wx.Size(31, 30), style=0)
        self.btnPesquisarPlaca.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarPlacaButton,
              id=wxID_FRMHISTORICOBTNPESQUISARPLACA)

        self.lstCtrlBuscaLocacaoFinalizada = wx.ListCtrl(id=wxID_FRMHISTORICOLISTCTRLBUSCA, name='lstCtrlBuscaLocacaoFinalizada',
              parent=self.pnlHistorico, pos=wx.Point(160, 224), size=wx.Size(804,
              264), style=wx.LC_ICON)
        self._init_coll_listCtrlBuscaLocacaoFinalizada_Columns(self.lstCtrlBuscaLocacaoFinalizada)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.criarTabela()
        self.inserirDadosNasColunasDaTabelaHistorico(self.lstCtrlBuscaLocacaoFinalizada)
        
    def criarTabela(self):
        self.lstCtrlBuscaLocacaoFinalizada = wx.ListCtrl(id=wxID_FRMHISTORICOLISTCTRLBUSCA,
              name='lstCtrlBuscaLocacaoFinalizada', parent=self.pnlHistorico,
              pos=wx.Point(160,224), size=wx.Size(804, 264), style=wx.LC_REPORT)
        self._init_coll_listCtrlBuscaLocacaoFinalizada_Columns(self.lstCtrlBuscaLocacaoFinalizada)
    
    def OnBtnPesquisarCpfButton(self, event):
        self.lstCtrlBuscaLocacaoFinalizada.Destroy() 
        cpf = self.txtCpf.GetValue() 
        print cpf
        
        self.criarTabela()
        print ClienteDAO.verificarExistenciaCliente(cpf)
        if(ClienteDAO.verificarExistenciaCliente(cpf) is True):
            if HistoricoDAO.getHistoricoByCpf(cpf) != []:
                #insere na tabela os dados de acordo com a cor fornecida
                self.inserirInformacoesNaListctrlByCpf(self.lstCtrlBuscaLocacaoFinalizada, cpf)
            
                self.txtCpf.Clear()
            else:
                caixaDeDialogo = wx.MessageDialog(self,'Este cliente ainda não realizou locações.', 'AVISO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeDialogo.ShowModal()
                caixaDeDialogo.Destroy()
                self.txtCpf.Clear()
                self.criarTabela()
                self.inserirDadosNasColunasDaTabelaHistorico(self.lstCtrlBuscaLocacaoFinalizada)
        else:
            self.lstCtrlBuscaLocacaoFinalizada.Destroy()
            self.criarTabela()
            self.inserirDadosNasColunasDaTabelaHistorico(self.lstCtrlBuscaLocacaoFinalizada)
            caixaDeDialogo = wx.MessageDialog(self,'Cliente inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
            
            self.txtCpf.Clear()
            
    def inserirInformacoesNaListctrlByCpf(self,listCtrl,cpf):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega as locacoes feitas pelo respectivo CPF
        rows = HistoricoDAO.getHistoricoByCpf(cpf)        
        self.inserirDadosNasColunasDaTabelaDeResultados(listCtrl, rows)
        
    def OnBtnPesquisarPlacaButton(self, event):
        self.lstCtrlBuscaLocacaoFinalizada.Destroy()  
        placa = self.txtPlaca.GetValue().upper() 
        #print placa
        
        self.criarTabela()
        #print VeiculoDAO.verificarExistenciaVeiculo(placa)
        if(VeiculoDAO.verificarExistenciaVeiculo(placa) is True):
            if HistoricoDAO.getHistoricoByPlaca(placa) != []:
                #insere na tabela os dados de acordo com a cor fornecida
                self.inserirInformacoesNaListctrlByPlaca(self.lstCtrlBuscaLocacaoFinalizada, placa)
            
                self.txtPlaca.Clear()
            else:
                caixaDeDialogo = wx.MessageDialog(self,'Não foram feitas locações com este veículo.', 'AVISO!', wx.OK | wx.ICON_INFORMATION)
                caixaDeDialogo.ShowModal()
                caixaDeDialogo.Destroy()
                self.txtPlaca.Clear()
                self.criarTabela()
                self.inserirDadosNasColunasDaTabelaHistorico(self.lstCtrlBuscaLocacaoFinalizada)
        else:
            self.lstCtrlBuscaLocacaoFinalizada.Destroy()
            self.criarTabela()
            self.inserirDadosNasColunasDaTabelaHistorico(self.lstCtrlBuscaLocacaoFinalizada)
            caixaDeDialogo = wx.MessageDialog(self,'Veículo inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
            
            self.txtPlaca.Clear()
        
    def inserirInformacoesNaListctrlByPlaca(self,listCtrl,placa):
        #Método que pegará a informação do banco e colocará na ListCtrl.
        
        #Pega as locacoes feitas pela respectiva placa
        rows = HistoricoDAO.getHistoricoByPlaca(placa)        
        self.inserirDadosNasColunasDaTabelaDeResultados(listCtrl, rows)
    
    def OnBtnCancelarButton(self, event):
        self.lstCtrlBuscaLocacaoFinalizada.Destroy()
        self.criarTabela()
        self.inserirDadosNasColunasDaTabelaHistorico(self.lstCtrlBuscaLocacaoFinalizada)
        self.txtPlaca.Clear()
        self.txtCpf.Clear()
        
    def inserirDadosNasColunasDaTabelaDeResultados(self,listCtrl,rows):        
        #Método responsável por colocar as informações do banco nas colunas da ListCtrl.
        #Recebe como parâmetro a ListCtrl na qual deseja inserir dados e as linhas
        #de informações obtidas numa busca no banco de dados.
        if rows:
            for row in rows:
                num_itens = listCtrl.GetItemCount()
                listCtrl.InsertStringItem(num_itens,str(row[5]))
                listCtrl.SetStringItem(num_itens,1,row[4])
                listCtrl.SetStringItem(num_itens,2,row[0])
                listCtrl.SetStringItem(num_itens,3,str(row[2]))
                listCtrl.SetStringItem(num_itens,4,str(row[1]))
                listCtrl.SetStringItem(num_itens,5,str(row[3]))
                listCtrl.SetStringItem(num_itens,6,"R$ " + str(row[6]))
    
    def inserirDadosNasColunasDaTabelaHistorico(self,listCtrl):   
        rows = HistoricoDAO.getAllHistorico()
        #print rows 
         
        if rows:
            for row in rows:
                num_itens = listCtrl.GetItemCount()
                listCtrl.InsertStringItem(num_itens,str(row[5]))
                listCtrl.SetStringItem(num_itens,1,row[4])
                listCtrl.SetStringItem(num_itens,2,row[0])
                listCtrl.SetStringItem(num_itens,3,str(row[2]))
                listCtrl.SetStringItem(num_itens,4,str(row[1]))
                listCtrl.SetStringItem(num_itens,5,str(row[3]))
                listCtrl.SetStringItem(num_itens,6,"R$ " + str(row[6]))
                
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
        
                
