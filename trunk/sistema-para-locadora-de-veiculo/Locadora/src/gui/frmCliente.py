#Boa:Frame:frmCliente

import wx
import wx.lib.buttons
import wx.lib.masked.textctrl

def create(parent):
    return frmCliente(parent)

[wxID_FRMCLIENTE, wxID_FRMCLIENTEBTNAUALIZAR, wxID_FRMCLIENTEBTNCANCELAR, 
 wxID_FRMCLIENTEBTNEDITAR, wxID_FRMCLIENTEBTNEXCLUIR, 
 wxID_FRMCLIENTEBTNINCLUIR, wxID_FRMCLIENTEBTNPESQUISAR, 
 wxID_FRMCLIENTELSTCLIENTES, wxID_FRMCLIENTELSTESTADOS, 
 wxID_FRMCLIENTEPNLCLIENTE, wxID_FRMCLIENTESTBAIRRO, wxID_FRMCLIENTESTCEP, 
 wxID_FRMCLIENTESTCIDADE, wxID_FRMCLIENTESTCLIENTE, wxID_FRMCLIENTESTCPF, 
 wxID_FRMCLIENTESTEMAIL, wxID_FRMCLIENTESTENDERECO, wxID_FRMCLIENTESTNOME, 
 wxID_FRMCLIENTESTPESQUISA, wxID_FRMCLIENTESTTELEFONE, wxID_FRMCLIENTESTUF, 
 wxID_FRMCLIENTETXTBAIRRO, wxID_FRMCLIENTETXTCEP, wxID_FRMCLIENTETXTCIDADE, 
 wxID_FRMCLIENTETXTCPF, wxID_FRMCLIENTETXTEMAIL, wxID_FRMCLIENTETXTENDERECO, 
 wxID_FRMCLIENTETXTNOME, wxID_FRMCLIENTETXTPESQUISA, 
 wxID_FRMCLIENTETXTTELEFONE, 
] = [wx.NewId() for _init_ctrls in range(30)]

class frmCliente(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRMCLIENTE, name=u'frmCliente',
              parent=prnt, pos=wx.Point(430, 98), size=wx.Size(641, 526),
              style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX,
              title=u'Cadastro de Cliente')
        self.SetClientSize(wx.Size(625, 488))

        self.pnlCliente = wx.Panel(id=wxID_FRMCLIENTEPNLCLIENTE,
              name=u'pnlCliente', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(625, 488), style=wx.TAB_TRAVERSAL)

        self.stCliente = wx.StaticBox(id=wxID_FRMCLIENTESTCLIENTE,
              label=u'Dados Pessoais', name=u'stCliente',
              parent=self.pnlCliente, pos=wx.Point(128, 8), size=wx.Size(488,
              232), style=0)

        self.txtCpf = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMCLIENTETXTCPF,
              name=u'txtCpf', parent=self.pnlCliente, pos=wx.Point(144, 56),
              size=wx.Size(152, 21), style=0, value='')
        self.txtCpf.SetMask(u'XXX.XXX.XXX-XX')
        self.txtCpf.SetAutoformat('')
        self.txtCpf.SetDatestyle('MDY')
        self.txtCpf.SetFormatcodes('')
        self.txtCpf.SetDescription('')
        self.txtCpf.SetExcludeChars('')
        self.txtCpf.SetValidRegex('')
        self.txtCpf.SetMaxLength(14)
        self.txtCpf.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.stCpf = wx.StaticText(id=wxID_FRMCLIENTESTCPF, label=u'CPF :',
              name=u'stCpf', parent=self.pnlCliente, pos=wx.Point(144, 40),
              size=wx.Size(27, 13), style=0)

        self.stNome = wx.StaticText(id=wxID_FRMCLIENTESTNOME, label=u'Nome :',
              name=u'stNome', parent=self.pnlCliente, pos=wx.Point(320, 40),
              size=wx.Size(35, 13), style=0)

        self.txtNome = wx.TextCtrl(id=wxID_FRMCLIENTETXTNOME, name=u'txtNome',
              parent=self.pnlCliente, pos=wx.Point(320, 56), size=wx.Size(280,
              21), style=0, value=u'')

        self.txtEndereco = wx.TextCtrl(id=wxID_FRMCLIENTETXTENDERECO,
              name=u'txtEndereco', parent=self.pnlCliente, pos=wx.Point(144,
              104), size=wx.Size(280, 21), style=0, value=u'')

        self.stEndereco = wx.StaticText(id=wxID_FRMCLIENTESTENDERECO,
              label=u'Endere\xe7o :', name=u'stEndereco',
              parent=self.pnlCliente, pos=wx.Point(144, 88), size=wx.Size(53,
              13), style=0)

        self.txtBairro = wx.TextCtrl(id=wxID_FRMCLIENTETXTBAIRRO,
              name=u'txtBairro', parent=self.pnlCliente, pos=wx.Point(448, 104),
              size=wx.Size(152, 21), style=0, value=u'')

        self.stBairro = wx.StaticText(id=wxID_FRMCLIENTESTBAIRRO,
              label=u'Bairro :', name=u'stBairro', parent=self.pnlCliente,
              pos=wx.Point(448, 88), size=wx.Size(36, 13), style=0)

        self.stCidade = wx.StaticText(id=wxID_FRMCLIENTESTCIDADE,
              label=u'Cidade :', name=u'stCidade', parent=self.pnlCliente,
              pos=wx.Point(144, 136), size=wx.Size(41, 13), style=0)

        self.txtCidade = wx.TextCtrl(id=wxID_FRMCLIENTETXTCIDADE,
              name=u'txtCidade', parent=self.pnlCliente, pos=wx.Point(144, 152),
              size=wx.Size(192, 21), style=0, value=u'')

        self.txtCep = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMCLIENTETXTCEP,
              name=u'txtCep', parent=self.pnlCliente, pos=wx.Point(360, 152),
              size=wx.Size(152, 21), style=0, value=u'  .   -   ')
        self.txtCep.SetAutoformat('')
        self.txtCep.SetMask(u'XX.XXX-XXX')
        self.txtCep.SetDatestyle('MDY')
        self.txtCep.SetFormatcodes('')
        self.txtCep.SetDescription('')
        self.txtCep.SetExcludeChars('')
        self.txtCep.SetValidRegex('')
        self.txtCep.SetMaxLength(10)
        self.txtCep.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.txtCep.SetInsertionPoint(9)

        self.lstEstados = wx.Choice(choices=["AC", "AL", "AP", "AM", "BA", "CE",
              "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE",
              "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"],
              id=wxID_FRMCLIENTELSTESTADOS, name=u'lstEstados',
              parent=self.pnlCliente, pos=wx.Point(536, 152), size=wx.Size(64,
              21), style=0)
        self.lstEstados.Bind(wx.EVT_CHOICE, self.OnLstEstadosChoice,
              id=wxID_FRMCLIENTELSTESTADOS)

        self.stUf = wx.StaticText(id=wxID_FRMCLIENTESTUF, label=u'UF :',
              name=u'stUf', parent=self.pnlCliente, pos=wx.Point(536, 136),
              size=wx.Size(21, 13), style=0)

        self.stTelefone = wx.StaticText(id=wxID_FRMCLIENTESTTELEFONE,
              label=u'Telefone :', name=u'stTelefone', parent=self.pnlCliente,
              pos=wx.Point(144, 184), size=wx.Size(50, 13), style=0)

        self.txtTelefone = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRMCLIENTETXTTELEFONE,
              name=u'txtTelefone', parent=self.pnlCliente, pos=wx.Point(144,
              200), size=wx.Size(208, 21), style=0, value='')
        self.txtTelefone.SetAutoformat('')
        self.txtTelefone.SetMask(u'+55 ( XX ) XXXX-XXXX')
        self.txtTelefone.SetDatestyle('MDY')
        self.txtTelefone.SetFormatcodes('')
        self.txtTelefone.SetDescription('')
        self.txtTelefone.SetExcludeChars('')
        self.txtTelefone.SetValidRegex('')
        self.txtTelefone.SetMaxLength(20)
        self.txtTelefone.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.txtEmail = wx.TextCtrl(id=wxID_FRMCLIENTETXTEMAIL,
              name=u'txtEmail', parent=self.pnlCliente, pos=wx.Point(376, 200),
              size=wx.Size(224, 21), style=0, value=u'')

        self.txtPesquisa = wx.TextCtrl(id=wxID_FRMCLIENTETXTPESQUISA,
              name=u'txtPesquisa', parent=self.pnlCliente, pos=wx.Point(144,
              288), size=wx.Size(400, 21), style=0, value=u'')

        self.btnPesquisar = wx.lib.buttons.GenBitmapButton(bitmap=wx.Bitmap(u'../gui/icon/search.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRMCLIENTEBTNPESQUISAR,
              name=u'btnPesquisar', parent=self.pnlCliente, pos=wx.Point(568,
              280), size=wx.Size(31, 32), style=0)
        self.btnPesquisar.Bind(wx.EVT_BUTTON, self.OnBtnPesquisarButton,
              id=wxID_FRMCLIENTEBTNPESQUISAR)

        self.stEmail = wx.StaticText(id=wxID_FRMCLIENTESTEMAIL,
              label=u'E-mail :', name=u'stEmail', parent=self.pnlCliente,
              pos=wx.Point(376, 184), size=wx.Size(36, 13), style=0)

        self.btnIncluir = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNINCLUIR,
              label=u'Incluir', name=u'btnIncluir', parent=self.pnlCliente,
              pos=wx.Point(24, 24), size=wx.Size(76, 25), style=0)
        self.btnIncluir.Bind(wx.EVT_BUTTON, self.OnBtnIncluirButton,
              id=wxID_FRMCLIENTEBTNINCLUIR)

        self.btnEditar = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNEDITAR,
              label=u'Editar', name=u'btnEditar', parent=self.pnlCliente,
              pos=wx.Point(24, 272), size=wx.Size(76, 25), style=0)
        self.btnEditar.Bind(wx.EVT_BUTTON, self.OnBtnEditarButton,
              id=wxID_FRMCLIENTEBTNEDITAR)

        self.btnAualizar = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNAUALIZAR,
              label=u'Atualizar', name=u'btnAualizar', parent=self.pnlCliente,
              pos=wx.Point(24, 312), size=wx.Size(76, 25), style=0)
        self.btnAualizar.Bind(wx.EVT_BUTTON, self.OnBtnAualizarButton,
              id=wxID_FRMCLIENTEBTNAUALIZAR)

        self.btnExcluir = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNEXCLUIR,
              label=u'Excluir', name=u'btnExcluir', parent=self.pnlCliente,
              pos=wx.Point(24, 360), size=wx.Size(76, 25), style=0)
        self.btnExcluir.Bind(wx.EVT_BUTTON, self.OnBtnExcluirButton,
              id=wxID_FRMCLIENTEBTNEXCLUIR)

        self.btnCancelar = wx.lib.buttons.GenButton(id=wxID_FRMCLIENTEBTNCANCELAR,
              label=u'Cancelar', name=u'btnCancelar', parent=self.pnlCliente,
              pos=wx.Point(24, 64), size=wx.Size(76, 25), style=0)
        self.btnCancelar.Bind(wx.EVT_BUTTON, self.OnBtnCancelarButton,
              id=wxID_FRMCLIENTEBTNCANCELAR)

        self.stPesquisa = wx.StaticBox(id=wxID_FRMCLIENTESTPESQUISA,
              label=u'Pesquisa por CPF', name=u'stPesquisa',
              parent=self.pnlCliente, pos=wx.Point(128, 256), size=wx.Size(488,
              224), style=0)

        self.lstClientes = wx.ListCtrl(id=wxID_FRMCLIENTELSTCLIENTES,
              name=u'lstClientes', parent=self.pnlCliente, pos=wx.Point(144,
              328), size=wx.Size(456, 128), style=wx.LC_ICON)

        self.stCep = wx.StaticText(id=wxID_FRMCLIENTESTCEP, label=u'CEP :',
              name=u'stCep', parent=self.pnlCliente, pos=wx.Point(360, 136),
              size=wx.Size(27, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnLstEstadosChoice(self, event):
        event.Skip()
    
    def clearTextfield(self):
        #Método responsável por limpar os campos
        self.txtCpf.Clear()
        self.txtNome.Clear()
        self.txtEndereco.Clear()
        self.txtTelefone.Clear()
        self.txtCep.Clear()
        self.txtBairro.Clear()
        self.txtCidade.Clear()
        self.txtEmail.Clear()
        self.lstEstados.Clear()
        
    def obterDadosInformados(self):
        #Método para obter os dados fornecidos
        cpf = self.txtCpf.GetValue()
        nome = self.txtNome.GetValue()
        endereco = self.txtEndereco.GetValue()
        telefone = self.txtTelefone.GetValue()
        cep = self.txtCep.GetValue()
        bairro = self.txtBairro.GetValue()
        cidade = self.txtCidade.GetValue()
        email = self.txtEmail.GetValue()        
        uf = self.lstEstados.GetLabelText()
        
        #a lista será usada posteriormente na ação do botão de incluir um cliente
        lista = [nome,endereco,telefone,cep,bairro,cidade,uf,email,cpf]
        
        return lista

    def OnBtnIncluirButton(self, event):
        event.Skip()

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

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
