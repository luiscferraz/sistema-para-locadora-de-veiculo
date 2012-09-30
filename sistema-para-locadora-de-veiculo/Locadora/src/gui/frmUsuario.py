# -*- coding: latin-1 -*-
#Boa:Frame:Frame1

import wx
import wx.lib.buttons

from negocio.Usuario import *
from db.UsuarioDAO import *

import frmLogin

def create(parent):
    return frmUsuario(parent)

[wxID_FRAME1, wxID_FRAME1GENBUTTON1, wxID_FRAME1GENBUTTON2, 
 wxID_FRAME1GENBUTTON3, wxID_FRAME1PANEL1, wxID_FRAME1BACKGROUND, wxID_FRAME1STATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class frmUsuario(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(300, 126), size=wx.Size(953, 453),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX, title='Usuário')
        self.SetClientSize(wx.Size(929, 415))
        self.SetIcon(wx.Icon(u'../gui/icon/logo.ico',wx.BITMAP_TYPE_ICO))

        self.pnlUsuario = wx.Panel(id=wxID_FRAME1PANEL1, name='pnlUsuario', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(929, 415),
              style=wx.TAB_TRAVERSAL)
        
        self.background = wx.StaticBitmap(bitmap=wx.Bitmap(u'../gui/images/back.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1BACKGROUND,
              name=u'background', parent=self.pnlUsuario, pos=wx.Point(150,
              24), size=wx.Size(767, 381), style=0)
        
        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1, label=u'',
              name='staticBox1', parent=self.pnlUsuario, pos=wx.Point(168, 8),
              size=wx.Size(750, 400), style=0)

        self.btnEntrar = wx.lib.buttons.GenButton(id=wxID_FRAME1GENBUTTON1,
              label=u'Entrar no sistema', name='btnEntrar', parent=self.pnlUsuario,
              pos=wx.Point(16, 24), size=wx.Size(136, 32), style=0)
        self.btnEntrar.Bind(wx.EVT_BUTTON, self.OnBtnEntrarButton,
              id=wxID_FRAME1GENBUTTON1)

        
    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def OnBtnEntrarButton(self, event):
        telaLogin = frmLogin.create(None)
        telaLogin.Show()
        telaLogin.Center()
        self.Destroy()
    
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()

