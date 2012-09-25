# -*- coding: latin-1 -*-
#Boa:Frame:Frame1

import wx
import wx.lib.stattext
import wx.lib.masked.textctrl
import wx.lib.buttons

def create(parent):
    return frmHistorico(parent)

[wxID_FRMHISTORICO, wxID_FRMHISTORICOBTNPESQUISARCPF, 
 wxID_FRMHISTORICOBTNPESQUISARPLACA, wxID_FRMHISTORICOBTNCANCELAR, wxID_FRMHISTORICOLBLCPF, 
 wxID_FRMHISTORICOLBLPLACA, wxID_FRMHISTORICOLISTCTRLBUSCA, wxID_FRMHISTORICOPNLHISTORICO, 
 wxID_FRMHISTORICOSTHISTORICO, wxID_FRMHISTORICOSTBUSCAR, wxID_FRMHISTORICOTXTCPF, 
 wxID_FRMHISTORICOTXTPLACA, 
] = [wx.NewId() for _init_ctrls in range(12)]

class frmHistorico(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMHISTORICO, name='', parent=prnt,
              pos=wx.Point(115, 42), size=wx.Size(1132, 580),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Histórico')
        self.SetClientSize(wx.Size(1116, 542))

        self.pnlHistorico = wx.Panel(id=wxID_FRMHISTORICOPNLHISTORICO, name='pnlHistorico', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1116, 542),
              style=wx.TAB_TRAVERSAL)

        self.stHistorico = wx.StaticBox(id=wxID_FRMHISTORICOSTHISTORICO,
              label=u'Histórico', name='stHistorico', parent=self.pnlHistorico,
              pos=wx.Point(144, 184), size=wx.Size(936, 328), style=0)

        self.stBuscar = wx.StaticBox(id=wxID_FRMHISTORICOSTBUSCAR,
              label=u'Buscar Loca\xe7\xe3o finalizada', name='stBuscar',
              parent=self.pnlHistorico, pos=wx.Point(144, 32), size=wx.Size(936, 120),
              style=0)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMHISTORICOBTNCANCELAR,
              label=u'Cancelar', name='btnCancelar', parent=self.pnlHistorico,
              pos=wx.Point(24, 40), size=wx.Size(96, 25), style=0)

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
              parent=self.pnlHistorico, pos=wx.Point(160, 224), size=wx.Size(904,
              264), style=wx.LC_ICON)

    def __init__(self, parent):
        self._init_ctrls(parent)
    
    def OnBtnPesquisarCpfButton(self, event):
        event.Skip()
    
    def OnBtnPesquisarPlacaButton(self, event):
        event.Skip()

    def OnGenBitmapToggleButton2Button(self, event):
        event.Skip()
        
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
        
                
