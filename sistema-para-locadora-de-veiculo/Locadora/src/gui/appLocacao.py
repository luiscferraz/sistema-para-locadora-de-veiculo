#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frmDevolucao

modules ={u'frmDevolucao': [1, 'Main frame of Application', u'frmDevolucao.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frmDevolucao.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()