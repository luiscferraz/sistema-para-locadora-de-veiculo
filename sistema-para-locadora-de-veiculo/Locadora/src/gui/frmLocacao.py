# -*- coding: latin-1 -*-
#Boa:Frame:frmLocacao

import wx
from wx.lib.anchors import LayoutAnchors
import wx.lib.buttons
import wx.lib.masked.textctrl

from db.ClienteDAO import *

def create(parent):
    return frmLocacao(parent)

[wxID_FRMLOCACAO, wxID_FRMLOCACAOBTNCANCELAR, wxID_FRMLOCACAOBTNINCLUIR, 
 wxID_FRMLOCACAOBTNPESQUISARCPF, wxID_FRMLOCACAOLISTCTRLBUSCATIPOVEICULO, 
 wxID_FRMLOCACAOLSTCTRLBUSCAMODELO, wxID_FRMLOCACAOLSTIPOVEICULO, 
 wxID_FRMLOCACAOPANEL1, wxID_FRMLOCACAORADIOBOXTIPOBUSCA, 
 wxID_FRMLOCACAOSTCLIENTE, wxID_FRMLOCACAOSTCOR, wxID_FRMLOCACAOSTCPF, 
 wxID_FRMLOCACAOSTMODELO, wxID_FRMLOCACAOSTNOME, wxID_FRMLOCACAOSTNOMECLIENTE, 
 wxID_FRMLOCACAOSTRESULTADOMODELO, wxID_FRMLOCACAOSTRESULTADOTIPO, 
 wxID_FRMLOCACAOSTTIPOVEICULO, wxID_FRMLOCACAOSTVEICULO, 
 wxID_FRMLOCACAOTXTCOR, wxID_FRMLOCACAOTXTCPF, wxID_FRMLOCACAOTXTMODELO, 
] = [wx.NewId() for _init_ctrls in range(22)]

class frmLocacao(wx.Frame):
    def _init_coll_listCtrlBuscaTipoVeiculo_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Modelo',
              width=300)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Cor',
              width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Taxa Base - R$', width=100)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Pre\xe7o/KM - R$', width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading='Cau\xe7\xe3o - R$', width=89)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMLOCACAO, name='frmLocacao',
              parent=prnt, pos=wx.Point(390, 55), size=wx.Size(962, 680),
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

        self.radioBoxTipoBusca = wx.RadioBox(choices=['Tipo de ve�culo',
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

        self.lsTipoVeiculo = wx.Choice(choices=[],
              id=wxID_FRMLOCACAOLSTIPOVEICULO, name='lsTipoVeiculo',
              parent=self.panel1, pos=wx.Point(296, 136), size=wx.Size(624, 21),
              style=0)

        self.stModelo = wx.StaticText(id=wxID_FRMLOCACAOSTMODELO,
              label='Modelo :', name='stModelo', parent=self.panel1,
              pos=wx.Point(296, 166), size=wx.Size(42, 13), style=0)

        self.txtModelo = wx.TextCtrl(id=wxID_FRMLOCACAOTXTMODELO,
              name='txtModelo', parent=self.panel1, pos=wx.Point(296, 184),
              size=wx.Size(432, 21), style=0, value='')

        self.txtCor = wx.TextCtrl(id=wxID_FRMLOCACAOTXTCOR, name='txtCor',
              parent=self.panel1, pos=wx.Point(744, 184), size=wx.Size(176, 21),
              style=0, value='')

        self.stCor = wx.StaticText(id=wxID_FRMLOCACAOSTCOR, label='Cor :',
              name='stCor', parent=self.panel1, pos=wx.Point(744, 168),
              size=wx.Size(25, 13), style=0)

        self.stResultadoTipo = wx.StaticBox(id=wxID_FRMLOCACAOSTRESULTADOTIPO,
              label='Resultado por tipo de ve\xedculo', name='stResultadoTipo',
              parent=self.panel1, pos=wx.Point(144, 224), size=wx.Size(776,
              176), style=0)

        self.listCtrlBuscaTipoVeiculo = wx.ListCtrl(id=wxID_FRMLOCACAOLISTCTRLBUSCATIPOVEICULO,
              name='listCtrlBuscaTipoVeiculo', parent=self.panel1,
              pos=wx.Point(160, 248), size=wx.Size(744, 136),
              style=wx.LC_REPORT)
        self._init_coll_listCtrlBuscaTipoVeiculo_Columns(self.listCtrlBuscaTipoVeiculo)

        self.stResultadoModelo = wx.StaticBox(id=wxID_FRMLOCACAOSTRESULTADOMODELO,
              label='Resultado por modelo do ve\xedculo',
              name='stResultadoModelo', parent=self.panel1, pos=wx.Point(144,
              412), size=wx.Size(776, 204), style=0)

        self.lstCtrlBuscaModelo = wx.ListCtrl(id=wxID_FRMLOCACAOLSTCTRLBUSCAMODELO,
              name='lstCtrlBuscaModelo', parent=self.panel1, pos=wx.Point(160,
              440), size=wx.Size(744, 160), style=wx.LC_ICON)

        self.btnIncluir = wx.lib.buttons.GenButton(id=wxID_FRMLOCACAOBTNINCLUIR,
              label='Incluir', name='btnIncluir', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(76, 25), style=0)
        self.btnIncluir.SetConstraints(LayoutAnchors(self.btnIncluir, True,
              True, False, False))

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMLOCACAOBTNCANCELAR,
              label='Cancelar', name='btnCancelar', parent=self.panel1,
              pos=wx.Point(24, 64), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMLOCACAOBTNCANCELAR)
        
        
        

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.txtCor.Disable()
        self.txtModelo.Disable()
        self.lsTipoVeiculo.Disable()
        self.radioBoxTipoBusca.Disable()
    
    
    def OnTxtCPFTextMaxlen(self, event):
        event.Skip()

    def OnTxtCPFTextEnter(self, event):
        event.Skip()

    def OnBtnPesquisarCpfButton(self, event):  
        cpf = self.txtCPF.GetValue() 
        #print cpf
        dao = ClienteDAO()
        #print dao.verificarExistenciaCliente(cpf)
        if(dao.verificarExistenciaCliente(cpf) is True):
            cliente = dao.procurarCliente(cpf)
            self.stNomeCliente.SetLabel(cliente.getNome())  
            self.radioBoxTipoBusca.Enable() 
        else:
            caixaDeDialogo = wx.MessageDialog(self,'Cliente inexistente.', 'ERRO!', wx.OK | wx.ICON_INFORMATION)
            caixaDeDialogo.ShowModal()
            caixaDeDialogo.Destroy()
            
            self.txtCPF.Clear()
        

    def OnBtnCancelarButton(self, event):
        event.Skip()

    def OnRadioBoxTipoBuscaSetFocus(self, event):
        event.Skip()

    def OnRadioBoxTipoBuscaRadiobox(self, event):
        if (self.radioBoxTipoBusca.GetSelection() == 0):
            self.lsTipoVeiculo.Enable()
            self.txtModelo.Disable()
            self.txtCor.Disable()
        elif (self.radioBoxTipoBusca.GetSelection() == 1):
            self.txtModelo.Enable()
            self.txtCor.Disable()
            self.lsTipoVeiculo.Disable()

        elif (self.radioBoxTipoBusca.GetSelection() == 2):
            self.txtCor.Enable()
            self.txtModelo.Disable()
            self.lsTipoVeiculo.Disable()

    
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
        
                
