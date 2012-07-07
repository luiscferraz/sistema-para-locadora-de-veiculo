#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frmVeiculo

modules ={u'frmVeiculo': [1, 'Main frame of Application', u'frmVeiculo.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frmVeiculo.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
