#Boa:Frame:Frame1

import wx
import wx.lib.stattext
import wx.lib.masked.textctrl
import wx.lib.buttons

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPTOGGLEBUTTON1, 
 wxID_FRAME1GENBITMAPTOGGLEBUTTON2, wxID_FRAME1GENBUTTON1, wxID_FRAME1LBLCPF, 
 wxID_FRAME1LBLPLACA, wxID_FRAME1LISTCTRL1, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, wxID_FRAME1TXTCPF, 
 wxID_FRAME1TXTPLACA, 
] = [wx.NewId() for _init_ctrls in range(12)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(105, 56), size=wx.Size(1132, 580),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Historico')
        self.SetClientSize(wx.Size(1116, 542))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1116, 542),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Historico', name='staticBox1', parent=self.panel1,
              pos=wx.Point(144, 184), size=wx.Size(936, 328), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Pesquisar por', name='staticBox2', parent=self.panel1,
              pos=wx.Point(144, 32), size=wx.Size(936, 120), style=0)

        self.genButton1 = wx.lib.buttons.GenButton(id=wxID_FRAME1GENBUTTON1,
              label=u'Cancelar', name='genButton1', parent=self.panel1,
              pos=wx.Point(24, 40), size=wx.Size(96, 25), style=0)

        self.txtCpf = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAME1LBLCPF,
              name=u'txtCpf', parent=self.panel1, pos=wx.Point(168, 88),
              size=wx.Size(160, 21), style=0, value='')
        self.txtCpf.SetMask(u'XXX.XXX.XXX-XX')
        self.txtCpf.SetAutoformat('')
        self.txtCpf.SetDatestyle('MDY')
        self.txtCpf.SetFormatcodes('')
        self.txtCpf.SetDescription('')
        self.txtCpf.SetExcludeChars('')
        self.txtCpf.SetValidRegex('')
        self.txtCpf.SetMaxLength(14)

        self.lblCpf = wx.lib.stattext.GenStaticText(ID=wxID_FRAME1LBLCPF,
              label=u'CPF :', name=u'lblCpf', parent=self.panel1,
              pos=wx.Point(168, 72), size=wx.Size(27, 13), style=0)

        self.lblPlaca = wx.lib.stattext.GenStaticText(ID=wxID_FRAME1LBLPLACA,
              label=u'Placa :', name=u'lblPlaca', parent=self.panel1,
              pos=wx.Point(392, 72), size=wx.Size(33, 13), style=0)

        self.txtPlaca = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAME1LBLPLACA,
              name=u'txtPlaca', parent=self.panel1, pos=wx.Point(392, 88),
              size=wx.Size(152, 21), style=0, value=u'   -    ')
        self.txtPlaca.SetMaxLength(8)
        self.txtPlaca.SetMask(u'XXX-XXXX')
        self.txtPlaca.SetAutoformat('')
        self.txtPlaca.SetDatestyle('MDY')
        self.txtPlaca.SetFormatcodes('')
        self.txtPlaca.SetDescription('')
        self.txtPlaca.SetExcludeChars('')
        self.txtPlaca.SetValidRegex('')

        self.genBitmapToggleButton1 = wx.lib.buttons.GenBitmapToggleButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1GENBITMAPTOGGLEBUTTON1,
              name='genBitmapToggleButton1', parent=self.panel1,
              pos=wx.Point(336, 80), size=wx.Size(31, 30), style=0)

        self.genBitmapToggleButton2 = wx.lib.buttons.GenBitmapToggleButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1GENBITMAPTOGGLEBUTTON2,
              name='genBitmapToggleButton2', parent=self.panel1,
              pos=wx.Point(552, 80), size=wx.Size(31, 30), style=0)
        self.genBitmapToggleButton2.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapToggleButton2Button,
              id=wxID_FRAME1GENBITMAPTOGGLEBUTTON2)

        self.listCtrl1 = wx.ListCtrl(id=wxID_FRAME1LISTCTRL1, name='listCtrl1',
              parent=self.panel1, pos=wx.Point(160, 224), size=wx.Size(904,
              264), style=wx.LC_ICON)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapToggleButton2Button(self, event):
        event.Skip()
