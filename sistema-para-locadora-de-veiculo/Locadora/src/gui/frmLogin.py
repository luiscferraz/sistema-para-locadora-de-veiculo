#Boa:Frame:Frame1

import wx
import wx.lib.buttons

from db.UsuarioDAO import *

import frmPrincipal

def create(parent):
    return frmLogin(parent)

[wxID_FRAME1, wxID_FRAME1GENBUTTON1, wxID_FRAME1GENBUTTON2, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(8)]

class frmLogin(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(526, 193), size=wx.Size(284, 226),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX, title='Login')
        self.SetClientSize(wx.Size(258, 183))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(268, 188),
              style=wx.TAB_TRAVERSAL)

        self.textLogin = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textLogin',
              parent=self.panel1, pos=wx.Point(64, 32), size=wx.Size(100, 21),
              style=0, value='')

        self.textSenha = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textSenha',
              parent=self.panel1, pos=wx.Point(64, 80), size=wx.Size(100, 21),
              style=wx.TE_PASSWORD, value='')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Login', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 32), size=wx.Size(26, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Senha', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 80), size=wx.Size(31, 13), style=0)

        self.btnOk = wx.lib.buttons.GenButton(id=wxID_FRAME1GENBUTTON1,
              label=u'OK', name='genButton1', parent=self.panel1,
              pos=wx.Point(24, 128), size=wx.Size(76, 25), style=0)
        self.btnOk.Bind(wx.EVT_BUTTON, self.efetuarLogin,
              id=wxID_FRAME1GENBUTTON1)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRAME1GENBUTTON2,
              label=u'Cancelar', name='btnCancelar', parent=self.panel1,
              pos=wx.Point(120, 128), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.onBtnCancelar,
              id=wxID_FRAME1GENBUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def efetuarLogin(self, event):
        if UsuarioDAO().verificarExistenciaUsuario(self.textLogin.GetValue(), self.textSenha.GetValue()):
            #print "Usuario verificado com sucesso"
            telaPrincipal = frmPrincipal.create(None)
            telaPrincipal.Show()
            self.Destroy()
        else:
            aviso = wx.MessageDialog(self, "Login ou senha invalidos", "Atencao", wx.OK, (100,100))
            aviso.ShowModal()
    
    def onBtnCancelar(self, event):
        self.Destroy()
        
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()

