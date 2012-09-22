#Boa:Frame:frmDevolucao

import wx
import wx.lib.stattext
import wx.lib.masked.textctrl
import wx.lib.buttons

def create(parent):
    return frmDevolucao(parent)

[wxID_FRMDEVOLUCAO, wxID_FRMDEVOLUCAOBTNCALCULAR, 
 wxID_FRMDEVOLUCAOBTNCANCELAR, wxID_FRMDEVOLUCAOBTNCPF, 
 wxID_FRMDEVOLUCAOBTNFINALIZAR, wxID_FRMDEVOLUCAOBTNPLACA, 
 wxID_FRMDEVOLUCAOLBLCPF, wxID_FRMDEVOLUCAOLBLPLACA, 
 wxID_FRMDEVOLUCAOLSTBUSCA, wxID_FRMDEVOLUCAOPNLDEVOLUCAO, 
 wxID_FRMDEVOLUCAOSTBUSCAR, wxID_FRMDEVOLUCAOSTCALCULAR, 
 wxID_FRMDEVOLUCAOSTKMCHEGADA, wxID_FRMDEVOLUCAOSTRESULTADO, 
 wxID_FRMDEVOLUCAOSTTOTAL, wxID_FRMDEVOLUCAOSTVALOR, wxID_FRMDEVOLUCAOTXTCPF, 
 wxID_FRMDEVOLUCAOTXTKMCHEGADA, wxID_FRMDEVOLUCAOTXTPLACA, 
] = [wx.NewId() for _init_ctrls in range(19)]

class frmDevolucao(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMDEVOLUCAO, name=u'frmDevolucao',
              parent=prnt, pos=wx.Point(454, 116), size=wx.Size(786, 459),
              style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION,
              title=u'Devolu\xe7\xe3o')
        self.SetClientSize(wx.Size(770, 424))
        self.SetIcon(wx.Icon(u'C:/Users/luisc/workspace/sistema-para-locadora-de-veiculo/sistema-para-locadora-de-veiculo/Locadora/src/gui/icon/logo.ico',
              wx.BITMAP_TYPE_ICO))

        self.pnlDevolucao = wx.Panel(id=wxID_FRMDEVOLUCAOPNLDEVOLUCAO,
              name=u'pnlDevolucao', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(770, 424), style=wx.TAB_TRAVERSAL)

        self.stBuscar = wx.StaticBox(id=wxID_FRMDEVOLUCAOSTBUSCAR,
              label=u'Buscar Loca\xe7\xe3o', name=u'stBuscar',
              parent=self.pnlDevolucao, pos=wx.Point(128, 8), size=wx.Size(632,
              96), style=0)

        self.btnFinalizar = wx.lib.buttons.GenButton(id=wxID_FRMDEVOLUCAOBTNFINALIZAR,
              label=u'Finalizar', name=u'btnFinalizar',
              parent=self.pnlDevolucao, pos=wx.Point(24, 24), size=wx.Size(76,
              25), style=0)
        self.btnFinalizar.Bind(wx.EVT_BUTTON, self.OnBtnFinalizarButton,
              id=wxID_FRMDEVOLUCAOBTNFINALIZAR)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMDEVOLUCAOBTNCANCELAR,
              label=u'Cancelar', name=u'btnCancelar', parent=self.pnlDevolucao,
              pos=wx.Point(24, 64), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnGenButton1Button,
              id=wxID_FRMDEVOLUCAOBTNCANCELAR)

        self.txtCpf = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMDEVOLUCAOTXTCPF,
              name=u'txtCpf', parent=self.pnlDevolucao, pos=wx.Point(144, 56),
              size=wx.Size(160, 21), style=0, value='')
        self.txtCpf.SetMask(u'XXX.XXX.XXX-XX')
        self.txtCpf.SetAutoformat('')
        self.txtCpf.SetDatestyle('MDY')
        self.txtCpf.SetFormatcodes('')
        self.txtCpf.SetDescription('')
        self.txtCpf.SetExcludeChars('')
        self.txtCpf.SetValidRegex('')
        self.txtCpf.SetMaxLength(14)

        self.lblCpf = wx.lib.stattext.GenStaticText(ID=wxID_FRMDEVOLUCAOLBLCPF,
              label=u'CPF :', name=u'lblCpf', parent=self.pnlDevolucao,
              pos=wx.Point(144, 40), size=wx.Size(27, 13), style=0)

        self.lblPlaca = wx.lib.stattext.GenStaticText(ID=wxID_FRMDEVOLUCAOLBLPLACA,
              label=u'Placa :', name=u'lblPlaca', parent=self.pnlDevolucao,
              pos=wx.Point(376, 40), size=wx.Size(33, 13), style=0)

        self.txtPlaca = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMDEVOLUCAOTXTPLACA,
              name=u'txtPlaca', parent=self.pnlDevolucao, pos=wx.Point(376, 56),
              size=wx.Size(152, 21), style=0, value=u'   -    ')
        self.txtPlaca.SetMaxLength(8)
        self.txtPlaca.SetMask(u'XXX-XXXX')
        self.txtPlaca.SetAutoformat('')
        self.txtPlaca.SetDatestyle('MDY')
        self.txtPlaca.SetFormatcodes('')
        self.txtPlaca.SetDescription('')
        self.txtPlaca.SetExcludeChars('')
        self.txtPlaca.SetValidRegex('')

        self.lstBusca = wx.ListCtrl(id=wxID_FRMDEVOLUCAOLSTBUSCA,
              name=u'lstBusca', parent=self.pnlDevolucao, pos=wx.Point(144,
              136), size=wx.Size(600, 160), style=wx.LC_ICON)

        self.stKmChegada = wx.StaticText(id=wxID_FRMDEVOLUCAOSTKMCHEGADA,
              label=u'KM Chegada :', name=u'stKmChegada',
              parent=self.pnlDevolucao, pos=wx.Point(144, 352), size=wx.Size(68,
              16), style=0)

        self.txtKmChegada = wx.TextCtrl(id=wxID_FRMDEVOLUCAOTXTKMCHEGADA,
              name=u'txtKmChegada', parent=self.pnlDevolucao, pos=wx.Point(144,
              368), size=wx.Size(160, 21), style=0, value=u'')

        self.btnCalcular = wx.lib.buttons.GenButton(id=wxID_FRMDEVOLUCAOBTNCALCULAR,
              label=u'Calcular', name=u'btnCalcular', parent=self.pnlDevolucao,
              pos=wx.Point(320, 360), size=wx.Size(76, 32), style=0)
        self.btnCalcular.Bind(wx.EVT_BUTTON, self.OnBtnCalcularButton,
              id=wxID_FRMDEVOLUCAOBTNCALCULAR)

        self.stValor = wx.StaticText(id=wxID_FRMDEVOLUCAOSTVALOR,
              label=u'Valor a Pagar :', name=u'stValor',
              parent=self.pnlDevolucao, pos=wx.Point(464, 352), size=wx.Size(72,
              13), style=0)

        self.stTotal = wx.StaticText(id=wxID_FRMDEVOLUCAOSTTOTAL,
              label=u'R$ 100,00', name=u'stTotal', parent=self.pnlDevolucao,
              pos=wx.Point(464, 368), size=wx.Size(82, 19), style=0)
        self.stTotal.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.btnCpf = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'C:/Users/luisc/workspace/sistema-para-locadora-de-veiculo/sistema-para-locadora-de-veiculo/Locadora/src/gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMDEVOLUCAOBTNCPF, name=u'btnCpf',
              parent=self.pnlDevolucao, pos=wx.Point(312, 48), size=wx.Size(32,
              32), style=0)

        self.btnPlaca = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'C:/Users/luisc/workspace/sistema-para-locadora-de-veiculo/sistema-para-locadora-de-veiculo/Locadora/src/gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMDEVOLUCAOBTNPLACA,
              name=u'btnPlaca', parent=self.pnlDevolucao, pos=wx.Point(536, 48),
              size=wx.Size(32, 32), style=0)

        self.stResultado = wx.StaticBox(id=wxID_FRMDEVOLUCAOSTRESULTADO,
              label=u'Resultado da busca', name=u'stResultado',
              parent=self.pnlDevolucao, pos=wx.Point(128, 112),
              size=wx.Size(632, 200), style=0)

        self.stCalcular = wx.StaticBox(id=wxID_FRMDEVOLUCAOSTCALCULAR,
              label=u'Calcular Pagamento', name=u'stCalcular',
              parent=self.pnlDevolucao, pos=wx.Point(128, 320),
              size=wx.Size(632, 96), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtnFinalizarButton(self, event):
        event.Skip()

    def OnGenButton1Button(self, event):
        event.Skip()

    def OnBtnCalcularButton(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
