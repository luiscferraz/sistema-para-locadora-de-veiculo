# -*- coding: latin-1 -*-
#Boa:Frame:frmTipoVeiculo

import wx
import wx.lib.buttons

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
    def _init_coll_lstTipoVeiculos_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='C\xf3digo', width=-1)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Descri\xe7\xe3o', width=-1)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Taxa Base - R$', width=-1)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Pre\xe7o/Km - R$', width=-1)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading='Cau\xe7\xe3o - R$', width=-1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMTIPOVEICULO, name=u'frmTipoVeiculo',
              parent=prnt, pos=wx.Point(390, 126), size=wx.Size(697, 526),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX,
              title=u'Cadastro de Tipo de Ve\xedculos')
        self.SetClientSize(wx.Size(681, 488))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',wx.BITMAP_TYPE_ICO))

        self.pnlTipoVeiculo = wx.Panel(id=wxID_FRMTIPOVEICULOPNLTIPOVEICULO,
              name=u'pnlTipoVeiculo', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(681, 488), style=wx.TAB_TRAVERSAL)

        self.stVeiculo = wx.StaticBox(id=wxID_FRMTIPOVEICULOSTVEICULO,
              label=u'Dados do Ve\xedculo', name=u'stVeiculo',
              parent=self.pnlTipoVeiculo, pos=wx.Point(128, 8),
              size=wx.Size(536, 144), style=0)

        self.stTaxa = wx.StaticText(id=wxID_FRMTIPOVEICULOSTTAXA,
              label=u'Taxa Base (R$) :', name=u'stTaxa',
              parent=self.pnlTipoVeiculo, pos=wx.Point(240, 40),
              size=wx.Size(82, 13), style=0)

        self.txtTaxa = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTTAXA,
              name=u'txtTaxa', parent=self.pnlTipoVeiculo, pos=wx.Point(240,
              56), size=wx.Size(112, 21), style=0, value=u'')

        self.txtDescricao = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTDESCRICAO,
              name=u'txtDescricao', parent=self.pnlTipoVeiculo,
              pos=wx.Point(144, 104), size=wx.Size(456, 21), style=0,
              value=u'')

        self.stDescricao = wx.StaticText(id=wxID_FRMTIPOVEICULOSTDESCRICAO,
              label=u'Descri\xe7\xe3o :', name=u'stDescricao',
              parent=self.pnlTipoVeiculo, pos=wx.Point(144, 88),
              size=wx.Size(54, 13), style=0)

        self.txtPreco = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTPRECO,
              name=u'txtPreco', parent=self.pnlTipoVeiculo, pos=wx.Point(376,
              56), size=wx.Size(88, 21), style=0, value=u'')

        self.stCor = wx.StaticText(id=wxID_FRMTIPOVEICULOSTCOR,
              label=u'Pre\xe7o KM (R$) :', name=u'stCor',
              parent=self.pnlTipoVeiculo, pos=wx.Point(376, 40),
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
              size=wx.Size(536, 312), style=0)

        self.stCaucao = wx.StaticText(id=wxID_FRMTIPOVEICULOSTCAUCAO,
              label=u'Valor Cau\xe7\xe3o (R$) :', name=u'stCaucao',
              parent=self.pnlTipoVeiculo, pos=wx.Point(488, 40),
              size=wx.Size(95, 13), style=0)

        self.lstTipoVeiculos = wx.ListCtrl(id=wxID_FRMTIPOVEICULOLSTTIPOVEICULOS,
              name=u'lstTipoVeiculos', parent=self.pnlTipoVeiculo,
              pos=wx.Point(144, 240), size=wx.Size(456, 216),
              style=wx.LC_REPORT)
        self._init_coll_lstTipoVeiculos_Columns(self.lstTipoVeiculos)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNCANCELAR,
              label=u'Cancelar', name=u'btnCancelar',
              parent=self.pnlTipoVeiculo, pos=wx.Point(24, 64), size=wx.Size(76,
              25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMTIPOVEICULOBTNCANCELAR)

        self.btnEditar = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNEDITAR,
              label=u'Editar', name=u'btnEditar', parent=self.pnlTipoVeiculo,
              pos=wx.Point(24, 184), size=wx.Size(76, 25), style=0)

        self.btnAtualizar = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNATUALIZAR,
              label=u'Atualizar', name=u'btnAtualizar',
              parent=self.pnlTipoVeiculo, pos=wx.Point(24, 224),
              size=wx.Size(76, 25), style=0)

        self.btnExcluir = wx.lib.buttons.GenButton(id=wxID_FRMTIPOVEICULOBTNEXCLUIR,
              label=u'Excluir', name=u'btnExcluir', parent=self.pnlTipoVeiculo,
              pos=wx.Point(24, 272), size=wx.Size(76, 25), style=0)

        self.txtCodigo = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTCODIGO,
              name=u'txtCodigo', parent=self.pnlTipoVeiculo, pos=wx.Point(144,
              56), size=wx.Size(72, 21), style=0, value=u'')

        self.txtCaucao = wx.TextCtrl(id=wxID_FRMTIPOVEICULOTXTCAUCAO,
              name=u'txtCaucao', parent=self.pnlTipoVeiculo, pos=wx.Point(488,
              56), size=wx.Size(112, 21), style=0, value=u'')

        self.stCodigo = wx.StaticText(id=wxID_FRMTIPOVEICULOSTCODIGO,
              label=u'C\xf3digo :', name=u'stCodigo',
              parent=self.pnlTipoVeiculo, pos=wx.Point(144, 40),
              size=wx.Size(41, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtnCancelarButton(self, event):
        event.Skip()

    def OnBtnEditarButton(self, event):
        event.Skip()

    def OnBtnAualizarButton(self, event):
        event.Skip()

    def OnBtnExcluirButton(self, event):
        event.Skip()

    def OnBtnPesquisarButton(self, event):
        event.Skip()

    def OnBtnIncluirButton(self, event):
        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
