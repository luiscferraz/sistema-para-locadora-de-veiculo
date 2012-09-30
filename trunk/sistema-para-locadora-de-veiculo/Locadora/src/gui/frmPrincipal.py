# -*- coding: latin-1 -*-
#Boa:Frame:frmPrincipal

import wx
import wx.lib.buttons

import frmCliente
import frmVeiculo
import frmTipoVeiculo
import frmLocacao
import frmDevolucao
import frmHistorico

def create(parent):
    return frmPrincipal(parent)

[wxID_FRMPRINCIPAL, wxID_FRMPRINCIPALBACKGROUND, wxID_FRMPRINCIPALBTNCLIENTES, 
 wxID_FRMPRINCIPALBTNDEVOLUCAO, wxID_FRMPRINCIPALBTNHISTORICO,  wxID_FRMPRINCIPALBTNLOCACAO, 
 wxID_FRMPRINCIPALBTNSAIR, wxID_FRMPRINCIPALALTERAR, wxID_FRMPRINCIPALBTNTIPOS, wxID_FRMPRINCIPALBTNVEICULOS, 
 wxID_FRMPRINCIPALPNLPRINCIPAL, wxID_FRMPRINCIPALSTINDEX, 
] = [wx.NewId() for _init_ctrls in range(12)]

class frmPrincipal(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMPRINCIPAL, name=u'frmPrincipal',
              parent=prnt, pos=wx.Point(175, 142), size=wx.Size(986, 468),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX,
              title=u'Sistema de Loca\xe7\xe3o de Ve\xedculos')
        self.SetClientSize(wx.Size(970, 433))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',wx.BITMAP_TYPE_ICO))

        self.pnlPrincipal = wx.Panel(id=wxID_FRMPRINCIPALPNLPRINCIPAL,
              name=u'pnlPrincipal', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(970, 433), style=wx.TAB_TRAVERSAL)
        self.pnlPrincipal.SetLabel(u'In\xedcio')

        self.btnClientes = wx.lib.buttons.GenButton(id=wxID_FRMPRINCIPALBTNCLIENTES,
              label=u'Clientes', name=u'btnClientes', parent=self.pnlPrincipal,
              pos=wx.Point(24, 32), size=wx.Size(128, 32), style=0)
        self.btnClientes.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnClientes.Bind(wx.EVT_BUTTON, self.OnBtnClientesButton,
              id=wxID_FRMPRINCIPALBTNCLIENTES)

        self.stIndex = wx.StaticBox(id=wxID_FRMPRINCIPALSTINDEX, label=u'',
              name=u'stIndex', parent=self.pnlPrincipal, pos=wx.Point(176, 8),
              size=wx.Size(784, 416), style=0)

        self.btnTipos = wx.lib.buttons.GenButton(id=wxID_FRMPRINCIPALBTNTIPOS,
              label=u'Tipos de Ve\xedculos', name=u'btnTipos',
              parent=self.pnlPrincipal, pos=wx.Point(24, 80), size=wx.Size(128,
              32), style=0)
        self.btnTipos.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.btnTipos.Bind(wx.EVT_BUTTON, self.OnBtnTiposButton,
              id=wxID_FRMPRINCIPALBTNTIPOS)

        self.btnVeiculos = wx.lib.buttons.GenButton(id=wxID_FRMPRINCIPALBTNVEICULOS,
              label=u'Ve\xedculos', name=u'btnVeiculos',
              parent=self.pnlPrincipal, pos=wx.Point(24, 128), size=wx.Size(128,
              32), style=0)
        self.btnVeiculos.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnVeiculos.Bind(wx.EVT_BUTTON, self.OnBtnVeiculosButton,
              id=wxID_FRMPRINCIPALBTNVEICULOS)

        self.btnLocacao = wx.lib.buttons.GenButton(id=wxID_FRMPRINCIPALBTNLOCACAO,
              label=u'Loca\xe7\xe3o', name=u'btnLocacao',
              parent=self.pnlPrincipal, pos=wx.Point(24, 176), size=wx.Size(128,
              32), style=0)
        self.btnLocacao.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnLocacao.Bind(wx.EVT_BUTTON, self.OnBtnLocacaoButton,
              id=wxID_FRMPRINCIPALBTNLOCACAO)

        self.background = wx.StaticBitmap(bitmap=wx.Bitmap(u'../gui/images/back.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMPRINCIPALBACKGROUND,
              name=u'background', parent=self.pnlPrincipal, pos=wx.Point(184,
              24), size=wx.Size(767, 381), style=0)

        self.btnDevolucao = wx.lib.buttons.GenButton(id=wxID_FRMPRINCIPALBTNDEVOLUCAO,
              label=u'Devolu\xe7\xe3o', name=u'btnDevolucao',
              parent=self.pnlPrincipal, pos=wx.Point(24, 224), size=wx.Size(128,
              32), style=0)
        self.btnDevolucao.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnDevolucao.Bind(wx.EVT_BUTTON, self.OnBtnDevolucaoButton,
              id=wxID_FRMPRINCIPALBTNDEVOLUCAO)
        
        self.btnHistorico = wx.lib.buttons.GenButton(id=wxID_FRMPRINCIPALBTNHISTORICO,
              label=u'Histórico', name=u'btnHistorico',
              parent=self.pnlPrincipal, pos=wx.Point(24, 272), size=wx.Size(128,
              32), style=0)
        self.btnHistorico.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.btnHistorico.Bind(wx.EVT_BUTTON, self.OnBtnHistoricoButton,
              id=wxID_FRMPRINCIPALBTNHISTORICO)

        self.btnSair = wx.lib.buttons.GenButton(id=wxID_FRMPRINCIPALBTNSAIR,
              label=u'Sair', name=u'btnSair', parent=self.pnlPrincipal,
              pos=wx.Point(24, 368), size=wx.Size(128, 32), style=0)
        self.btnSair.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.btnSair.Bind(wx.EVT_BUTTON, self.OnBtnSairButton,
              id=wxID_FRMPRINCIPALBTNSAIR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtnClientesButton(self, event):
        telaCliente = frmCliente.create(None)
        telaCliente.Show()
        telaCliente.Center()

    def OnBtnTiposButton(self, event):
        telaTipoVeiculo = frmTipoVeiculo.create(None)
        telaTipoVeiculo.Show()
        telaTipoVeiculo.Center()

    def OnBtnVeiculosButton(self, event):
        telaVeiculo = frmVeiculo.create(None)
        telaVeiculo.Show()
        telaVeiculo.Center()

    def OnBtnLocacaoButton(self, event):
        telaLocacao = frmLocacao.create(None)
        telaLocacao.Show()
        telaLocacao.Center()

    def OnBtnDevolucaoButton(self, event):
        telaDevolucao = frmDevolucao.create(None)
        telaDevolucao.Show()
        telaDevolucao.Center()
        
    def OnBtnHistoricoButton(self, event):
        telaHistorico = frmHistorico.create(None)
        telaHistorico.Show()
        telaHistorico.Center()

    def OnBtnSairButton(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
