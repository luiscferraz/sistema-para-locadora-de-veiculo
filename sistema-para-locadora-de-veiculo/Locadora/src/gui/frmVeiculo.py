# -*- coding: latin-1 -*-
#Boa:Frame:frmVeiculo

import wx
import wx.lib.buttons
import wx.lib.masked.textctrl

def create(parent):
    return frmVeiculo(parent)

[wxID_FRMVEICULO, wxID_FRMVEICULOBTNATUALIZAR, wxID_FRMVEICULOBTNCANCELAR, 
 wxID_FRMVEICULOBTNEDITAR, wxID_FRMVEICULOBTNEXCLUIR, 
 wxID_FRMVEICULOBTNINCLUIR, wxID_FRMVEICULOBTNPESQUISAR, 
 wxID_FRMVEICULOLSTTIPO, wxID_FRMVEICULOLSTVEICULOS, 
 wxID_FRMVEICULOPNLVEICULO, wxID_FRMVEICULOSTCOR, wxID_FRMVEICULOSTMARCA, 
 wxID_FRMVEICULOSTMODELO, wxID_FRMVEICULOSTPESQUISA, wxID_FRMVEICULOSTPLACA, 
 wxID_FRMVEICULOSTTIPO, wxID_FRMVEICULOSTVEICULO, wxID_FRMVEICULOTXTCOR, 
 wxID_FRMVEICULOTXTMARCA, wxID_FRMVEICULOTXTMODELO, 
 wxID_FRMVEICULOTXTPESQUISA, wxID_FRMVEICULOTXTPLACA, 
] = [wx.NewId() for _init_ctrls in range(22)]

class frmVeiculo(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMVEICULO, name=u'frmVeiculo',
              parent=prnt, pos=wx.Point(390, 126), size=wx.Size(641, 523),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX,
              title=u'Cadastro de Ve\xedculos')
        self.SetClientSize(wx.Size(625, 488))

        self.pnlVeiculo = wx.Panel(id=wxID_FRMVEICULOPNLVEICULO,
              name=u'pnlVeiculo', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(625, 488), style=wx.TAB_TRAVERSAL)

        self.stVeiculo = wx.StaticBox(id=wxID_FRMVEICULOSTVEICULO,
              label=u'Dados do Ve\xedculo', name=u'stVeiculo',
              parent=self.pnlVeiculo, pos=wx.Point(128, 8), size=wx.Size(488,
              144), style=0)

        self.txtPlaca = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMVEICULOTXTPLACA,
              name=u'txtPlaca', parent=self.pnlVeiculo, pos=wx.Point(144, 56),
              size=wx.Size(104, 21), style=0, value='')
        self.txtPlaca.SetMask(u'XXX-XXXX')
        self.txtPlaca.SetAutoformat('')
        self.txtPlaca.SetDatestyle('MDY')
        self.txtPlaca.SetFormatcodes('')
        self.txtPlaca.SetDescription('')
        self.txtPlaca.SetExcludeChars('')
        self.txtPlaca.SetValidRegex('')
        self.txtPlaca.SetMaxLength(8)
        self.txtPlaca.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.stPlaca = wx.StaticText(id=wxID_FRMVEICULOSTPLACA,
              label=u'Placa :', name=u'stPlaca', parent=self.pnlVeiculo,
              pos=wx.Point(144, 40), size=wx.Size(33, 13), style=0)
        self.stPlaca.SetToolTipString(u'stCpf')

        self.stMarca = wx.StaticText(id=wxID_FRMVEICULOSTMARCA,
              label=u'Marca :', name=u'stMarca', parent=self.pnlVeiculo,
              pos=wx.Point(272, 40), size=wx.Size(37, 13), style=0)

        self.txtMarca = wx.TextCtrl(id=wxID_FRMVEICULOTXTMARCA,
              name=u'txtMarca', parent=self.pnlVeiculo, pos=wx.Point(272, 56),
              size=wx.Size(152, 21), style=0, value=u'')

        self.txtModelo = wx.TextCtrl(id=wxID_FRMVEICULOTXTMODELO,
              name=u'txtModelo', parent=self.pnlVeiculo, pos=wx.Point(144, 104),
              size=wx.Size(224, 21), style=0, value=u'')

        self.stModelo = wx.StaticText(id=wxID_FRMVEICULOSTMODELO,
              label=u'Modelo :', name=u'stModelo', parent=self.pnlVeiculo,
              pos=wx.Point(144, 88), size=wx.Size(42, 13), style=0)

        self.txtCor = wx.TextCtrl(id=wxID_FRMVEICULOTXTCOR, name=u'txtCor',
              parent=self.pnlVeiculo, pos=wx.Point(448, 56), size=wx.Size(152,
              21), style=0, value=u'')

        self.stCor = wx.StaticText(id=wxID_FRMVEICULOSTCOR, label=u'Cor :',
              name=u'stCor', parent=self.pnlVeiculo, pos=wx.Point(448, 40),
              size=wx.Size(25, 13), style=0)

        self.txtPesquisa = wx.TextCtrl(id=wxID_FRMVEICULOTXTPESQUISA,
              name=u'txtPesquisa', parent=self.pnlVeiculo, pos=wx.Point(144,
              200), size=wx.Size(400, 21), style=0, value=u'')

        self.btnPesquisar = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMVEICULOBTNPESQUISAR,
              name=u'btnPesquisar', parent=self.pnlVeiculo, pos=wx.Point(568,
              192), size=wx.Size(31, 32), style=0)
        self.btnPesquisar.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarButton,
              id=wxID_FRMVEICULOBTNPESQUISAR)

        self.btnIncluir = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNINCLUIR,
              label=u'Incluir', name=u'btnIncluir', parent=self.pnlVeiculo,
              pos=wx.Point(24, 24), size=wx.Size(76, 25), style=0)
        self.btnIncluir.Bind(wx.EVT_BUTTON, self.OnBtnIncluirButton,
              id=wxID_FRMVEICULOBTNINCLUIR)

        self.stPesquisa = wx.StaticBox(id=wxID_FRMVEICULOSTPESQUISA,
              label=u'Pesquisa por Placa', name=u'stPesquisa',
              parent=self.pnlVeiculo, pos=wx.Point(128, 168), size=wx.Size(488,
              312), style=0)

        self.stTipo = wx.StaticText(id=wxID_FRMVEICULOSTTIPO,
              label=u'Tipo de Ve\xedculo :', name=u'stTipo',
              parent=self.pnlVeiculo, pos=wx.Point(392, 88), size=wx.Size(79,
              13), style=0)

        self.lstTipo = wx.Choice(choices=[], id=wxID_FRMVEICULOLSTTIPO,
              name=u'lstTipo', parent=self.pnlVeiculo, pos=wx.Point(392, 104),
              size=wx.Size(208, 21), style=0)
        self.lstTipo.Bind(wx.EVT_CHOICE, self.OnLstTipoChoice,
              id=wxID_FRMVEICULOLSTTIPO)

        self.lstVeiculos = wx.ListCtrl(id=wxID_FRMVEICULOLSTVEICULOS,
              name=u'lstVeiculos', parent=self.pnlVeiculo, pos=wx.Point(144,
              240), size=wx.Size(456, 216), style=wx.LC_ICON)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNCANCELAR,
              label=u'Cancelar', name=u'btnCancelar', parent=self.pnlVeiculo,
              pos=wx.Point(24, 64), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMVEICULOBTNCANCELAR)

        self.btnEditar = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNEDITAR,
              label=u'Editar', name=u'btnEditar', parent=self.pnlVeiculo,
              pos=wx.Point(24, 184), size=wx.Size(76, 25), style=0)

        self.btnAtualizar = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNATUALIZAR,
              label=u'Atualizar', name=u'btnAtualizar', parent=self.pnlVeiculo,
              pos=wx.Point(24, 224), size=wx.Size(76, 25), style=0)

        self.btnExcluir = wx.lib.buttons.GenButton(id=wxID_FRMVEICULOBTNEXCLUIR,
              label=u'Excluir', name=u'btnExcluir', parent=self.pnlVeiculo,
              pos=wx.Point(24, 272), size=wx.Size(76, 25), style=0)

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

    def OnLstTipoChoice(self, event):
        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
